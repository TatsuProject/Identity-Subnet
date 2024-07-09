import bittensor as bt
from CID.protocol import ProfileSynapse
import scoring



async def miner_forward(self, synapse: ProfileSynapse) -> ProfileSynapse:
    """
    Processes the incoming 'ProfileSynapse' synapse by performing a predefined operation on the input data.

    Args:
        synapse (CID.protocol.ProfileSynapse): The synapse object containing the task data.

    Returns:
        CID.protocol.ProfileSynapse: The synapse object with the 'answer' field set to the answer from miner.
    """
    #get data from synapse
    _public_repos = synapse.public_repos
    _created_at = synapse.created_at
    _total_commits = synapse.total_commits
    _eth_balance = synapse.eth_balance
    _tao_balance = synapse.tao_balance
    _tao_staked = synapse.tao_staked
    _no_of_transactions = synapse.no_of_transactions
    
    #calculate score
    score = scoring.calculate_score(_public_repos, _created_at, _total_commits, _eth_balance, _tao_balance, _tao_staked, _no_of_transactions)
    synapse.score = score
    return synapse