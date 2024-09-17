# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import time
import typing
import bittensor as bt

# Bittensor Miner Template:
import CID

# import base miner class which takes care of most of the boilerplate
from CID.base.miner import BaseMinerNeuron
from CID.miner.miner_forward import miner_forward

class Miner(BaseMinerNeuron):
    """
    Your miner neuron class. You should use this class to define your miner's behavior. In particular, you should replace the forward function with your own logic. You may also want to override the blacklist and priority functions according to your needs.

    This class inherits from the BaseMinerNeuron class, which in turn inherits from BaseNeuron. The BaseNeuron class takes care of routine tasks such as setting up wallet, subtensor, metagraph, logging directory, parsing config, etc. You can override any of the methods in BaseNeuron if you need to customize the behavior.

    This class provides reasonable default behavior for a miner such as blacklisting unrecognized hotkeys, prioritizing requests based on stake, and forwarding requests to the forward function. If you need to define custom
    """

    def __init__(self, config=None):
        bt.logging.debug("Started")
        super(Miner, self).__init__(config=config)
        bt.logging.debug("Init done")

        # TODO(developer): Anything specific to your use case you can do here

    async def forward(
        self, synapse: CID.protocol.ProfileSynapse
    ) -> CID.protocol.ProfileSynapse:
        """
        Processes the incoming ProfileSynapse by calculating a score based on various user attributes.

        Args:
            synapse (CID.protocol.ProfileSynapse): The synapse object containing the user data.

        Returns:
            CID.protocol.ProfileSynapse: The synapse object with the 'score' field set to the calculated score.
        """
        bt.logging.debug(f"Received synapse: {synapse}")
        
        # Use the miner_forward function from CID.miner.miner_forward
        processed_synapse = await miner_forward(self, synapse)
        
        bt.logging.debug(f"Processed synapse with score: {processed_synapse.score}")
        return processed_synapse

    async def blacklist(
        self, synapse: CID.protocol.ProfileSynapse
    ) -> typing.Tuple[bool, str]:
        """
        Determines whether an incoming request should be blacklisted and thus ignored.

        Args:
            synapse (CID.protocol.ProfileSynapse): A synapse object constructed from the headers of the incoming request.

        Returns:
            Tuple[bool, str]: A tuple containing a boolean indicating whether the synapse's hotkey is blacklisted,
                            and a string providing the reason for the decision.
        """
        if synapse.dendrite is None or synapse.dendrite.hotkey is None:
            bt.logging.warning("Received a request without a dendrite or hotkey.")
            return True, "Missing dendrite or hotkey"

        uid = self.metagraph.hotkeys.index(synapse.dendrite.hotkey)
        if (
            not self.config.blacklist.allow_non_registered
            and synapse.dendrite.hotkey not in self.metagraph.hotkeys
        ):
            bt.logging.trace(
                f"Blacklisting un-registered hotkey {synapse.dendrite.hotkey}"
            )
            return True, "Unrecognized hotkey"

        if self.config.blacklist.force_validator_permit:
            if not self.metagraph.validator_permit[uid]:
                bt.logging.warning(
                    f"Blacklisting a request from non-validator hotkey {synapse.dendrite.hotkey}"
                )
                return True, "Non-validator hotkey"

        bt.logging.trace(
            f"Not Blacklisting recognized hotkey {synapse.dendrite.hotkey}"
        )
        return False, "Hotkey recognized!"

    async def priority(self, synapse: CID.protocol.ProfileSynapse) -> float:
        """
        Determines the priority of an incoming request based on the stake of the calling entity.

        Args:
            synapse (CID.protocol.ProfileSynapse): The synapse object that contains metadata about the incoming request.

        Returns:
            float: A priority score derived from the stake of the calling entity.
        """
        if synapse.dendrite is None or synapse.dendrite.hotkey is None:
            bt.logging.warning("Received a request without a dendrite or hotkey.")
            return 0.0
        
        caller_uid = self.metagraph.hotkeys.index(synapse.dendrite.hotkey)
        priority = float(self.metagraph.S[caller_uid])
        bt.logging.trace(
            f"Prioritizing {synapse.dendrite.hotkey} with value: {priority}"
        )
        return priority


# This is the main function, which runs the miner.
if __name__ == "__main__":
    with Miner() as miner:
        while True:
            bt.logging.info(f"Miner running... {time.time()}")
            time.sleep(5)
