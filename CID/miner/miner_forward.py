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
    _eth_nft_balance= synapse.eth_nft_balance
    _tao_balance = synapse.tao_balance
    _tao_staked = synapse.tao_staked
    _no_of_transactions = synapse.no_of_transactions
    _is_linkedin_email_verified = synapse.is_linkedin_email_verified
    
    #calculate score
    _score = scoring.calculate_repo_points(_public_repos) + scoring.calculate_account_age_points(_created_at) + scoring.commit_points(_total_commits) + scoring.crypto_score(_eth_balance) + scoring.eth_nft_score(_eth_nft_balance) + scoring.crypto_score(_tao_balance) + scoring.transaction_score(_no_of_transactions) + scoring.staked_score(_tao_staked) + scoring.linkedin_email_score(_is_linkedin_email_verified)
    synapse.score = _score
    return synapse