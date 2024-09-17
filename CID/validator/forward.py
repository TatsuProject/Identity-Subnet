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
from CID.protocol import ProfileSynapse
from datetime import datetime, time
from time import sleep

fake = Faker()

def get_random_data() -> ProfileSynapse:
    _id = str(uuid.uuid4())
    _public_repos = random.randint(0, 1000)
    _github_created_at = int(fake.date_time_between(start_date='-6y', end_date='now').timestamp())
    _total_commits = random.randint(0, 10000)
    _eth_balance = random.uniform(0, 10)
    _tao_balance = random.uniform(0, 1000)
    _eth_transactions = random.randint(0, 100)
    _tao_transactions = random.randint(0, 100)
    _x_followers = random.randint(0, 10000)
    _insta_followers = random.randint(0, 10000)
    _tiktok_followers = random.randint(0, 10000)
    _fb_followers = random.randint(0, 5000)
    _reddit_post_karma = random.randint(0, 50000)
    _reddit_comment_karma = random.randint(0, 50000)
    _x_created_at = int(fake.date_time_between(start_date='-10y', end_date='now').timestamp())
    _reddit_created_at = int(fake.date_time_between(start_date='-15y', end_date='now').timestamp())
    _insta_created_at = int(fake.date_time_between(start_date='-10y', end_date='now').timestamp())
    _linkedin_created_at = int(fake.date_time_between(start_date='-15y', end_date='now').timestamp())
    _is_linkedin_email_verified = random.choice([True, False])
    _is_reddit_email_verified = random.choice([True, False])
    _is_x_email_verified = random.choice([True, False])
    _is_insta_email_verified = random.choice([True, False])
    _is_tiktok_email_verified = random.choice([True, False])
    
    return ProfileSynapse(
        id=_id,
        type="generated",
        public_repos=_public_repos,
        github_created_at=_github_created_at,
        total_commits=_total_commits,
        eth_balance=_eth_balance,
        tao_balance=_tao_balance,
        eth_transactions=_eth_transactions,
        tao_transactions=_tao_transactions,
        x_followers=_x_followers,
        insta_followers=_insta_followers,
        tiktok_followers=_tiktok_followers,
        fb_followers=_fb_followers,
        reddit_post_karma=_reddit_post_karma,
        reddit_comment_karma=_reddit_comment_karma,
        x_created_at=_x_created_at,
        reddit_created_at=_reddit_created_at,
        insta_created_at=_insta_created_at,
        linkedin_created_at=_linkedin_created_at,
        is_linkedin_email_verified=_is_linkedin_email_verified,
        is_reddit_email_verified=_is_reddit_email_verified,
        is_x_email_verified=_is_x_email_verified,
        is_insta_email_verified=_is_insta_email_verified,
        is_tiktok_email_verified=_is_tiktok_email_verified,
        score=0  # The score will be calculated by the miner
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

    miner_rewards = get_rewards(
        self, ground_truth, responses
    )

    bt.logging.debug("Miner Rewards")
    bt.logging.debug(miner_rewards)

    printRecords = [
        [
            "UID",
            "IP:Port",
            "Status Code",
            "Profile Score",
            "Ground Truth",
            "Reward",
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
                response.score,  # Calculated Score
                ground_truth,  # Ground Truth Score
                f"{miner_rewards[i]}",  # Reward
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

    self.update_scores(miner_rewards, miner_uids)
    sleep(5)