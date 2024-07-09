# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Set your name
# Copyright © 2023 <your name>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import random
import bittensor as bt
from typing import Tuple
from faker import Faker
import CID.validator.scoring as scoring
import uuid
from tabulate import tabulate
from CID.protocol import ProfileSynapse
from CID.validator.reward import get_rewards
from CID.utils.uids import get_random_uids
from protocol import ProfileSynapse
from datetime import datetime,time

fake = Faker()

def get_random_data() -> ProfileSynapse:
    _public_repos = random.randint(0,1000)
    _created_at = fake.date_between(start_date='-6y', end_date='today')
    _created_at_datetime = datetime.combine(_created_at, time())
    _created_at = int(_created_at_datetime.timestamp())
    _total_commits = random.randint(0,1000)
    _eth_balance = (random.randint(1,1000)/1000)
    _tao_balance = (random.randint(1,1000)/100)
    _tao_staked = (random.randint(1,int(_tao_balance)))
    _no_of_transactions = random.randint(0,5)
    _score = 0
    bt.logging.debug(f"Score = {_score}")
    _score = scoring.calculate_repo_points(_public_repos) + scoring.calculate_account_age_points(_created_at) + scoring.commit_points(_total_commits) + scoring.crypto_score(_eth_balance) + scoring.crypto_score(_tao_balance) + scoring.transaction_score(_no_of_transactions) + scoring.staked_score(_tao_staked)
    bt.logging.debug(f"Score = {_score}")
    _id = str(uuid.uuid4())
    
    return ProfileSynapse(
        id = _id,
        type = "generated",
        public_repos = _public_repos,
        created_at = _created_at,
        total_commits = _total_commits,
        eth_balance = _eth_balance,
        tao_balance = _tao_balance,
        tao_staked = _tao_staked,
        no_of_transactions = _no_of_transactions,
        score = _score
    )

def generate_task() -> Tuple[ProfileSynapse, str]:
    """
    Generate a random task to be sent to the miners.
    Returns:
        ProfileSynapse: A randomly generated profile.
    """
    task = get_random_data()
    task_type = "generated"

    # Log the generated task for monitoring purposes.
    bt.logging.debug(f"Task: {task.id} - Generated task type: {task_type}")

    printable_task = task.to_dict()
    bt.logging.debug(f"Task: {task.id} - Task: {printable_task}")

    return task, task_type


async def forward(self):
    """
    The forward function is called by the validator every time step. In this case it is called every 10 seconds.

    It is responsible for querying the network and scoring the responses.

    Args:
        self (:obj:`bittensor.neuron.Neuron`): The neuron object which contains all the necessary state for the validator.
    """

    bt.logging.debug("Forwarding task to miners")
    miner_uids = get_random_uids(self, k=self.config.neuron.sample_size)

    # Generate a task to be sent to the miners.
    task = None
    task_type = None
    try:
        task, task_type = generate_task()
    except Exception as e:
        bt.logging.error(f"Error generating task: {e} \n Retrying...")
        return
    bt.logging.debug("task Generated")
    ground_truth = task.score
    task.score = 0

    bt.logging.debug(
        f"Task: {task.id} - Sending task to miners with timeout {self.config.neuron.timeout}"
    )
    bt.logging.debug(f"Task: {task.id} - Chosen Miner IDs: {miner_uids}")
    # The dendrite client queries the network.
    responses = await self.dendrite(
        # Send the query to selected miner axons in the network.
        axons=[self.metagraph.axons[uid] for uid in miner_uids],
        synapse=task,
        timeout=self.config.neuron.timeout,
        # All responses have the deserialize function called on them before returning.
        # You are encouraged to define your own deserialization function.
        deserialize=True,
    )

    is_correct_answer = get_rewards(
        self, ground_truth, responses
    )
    printRecords = [
        [
            "UID",
            "IP:Port",
            "Status Code",
            "Selected Answer",
            "Is Answer Correct",
        ]
    ]
    for i, response in enumerate(responses):
        printRecords.append(
            [
                f"{miner_uids[i]}",  # Miner UID
                f"{response.axon.ip}:{response.axon.port}",  # Miner IP:Port
                (
                    response.axon.status_code if response.axon.status_code else "408"
                ),  # Status Code of the response
                response.score,  # Selected Answer
                f"{is_correct_answer[i]}",  # is answer correct
            ]
        )

    print(
        tabulate(
            tabular_data=printRecords,
            headers="firstrow",
            tablefmt="fancy_grid",
        )
    )
    # Update the scores based on the rewards. You may want to define your own update_scores function for custom behavior.
    self.update_scores(is_correct_answer, miner_uids)