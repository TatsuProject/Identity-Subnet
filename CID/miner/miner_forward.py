import bittensor as bt
from CID.protocol import ProfileSynapse
from CID.validator import scoring

async def miner_forward(self, synapse: ProfileSynapse) -> ProfileSynapse:
    """
    Processes the incoming 'ProfileSynapse' synapse by calculating a score based on various user attributes.

    Args:
        synapse (CID.protocol.ProfileSynapse): The synapse object containing the user data.

    Returns:
        CID.protocol.ProfileSynapse: The synapse object with the 'score' field set to the calculated score.
    """
    # Calculate GitHub-related scores
    github_score = (
        scoring.calculate_repo_points(synapse.public_repos) +
        scoring.github_account_age_points(synapse.github_created_at) +
        scoring.commit_points(synapse.total_commits)
    )

    # Calculate crypto-related scores
    crypto_score = (
        scoring.eth_crypto_score(synapse.eth_balance) +
        scoring.tao_crypto_score(synapse.tao_balance) +
        scoring.eth_transaction_score(synapse.eth_transactions) +
        scoring.tao_transaction_score(synapse.tao_transactions)
    )

    # Calculate social media-related scores
    social_score = (
        scoring.x_follower_points(synapse.x_followers) +
        scoring.insta_follower_points(synapse.insta_followers) +
        scoring.tiktok_follower_points(synapse.tiktok_followers) +
        scoring.fb_follower_points(synapse.fb_followers) +
        scoring.reddit_post_karma(synapse.reddit_post_karma) +
        scoring.reddit_comment_karma(synapse.reddit_comment_karma)
    )

    # Calculate account age scores
    age_score = (
        scoring.x_account_age_points(synapse.x_created_at) +
        scoring.reddit_account_age_points(synapse.reddit_created_at) +
        scoring.insta_account_age_points(synapse.insta_created_at) +
        scoring.linkedin_account_age_points(synapse.linkedin_created_at)
    )

    # Calculate email verification scores
    email_score = (
        scoring.linkedin_email_score(synapse.is_linkedin_email_verified) +
        scoring.reddit_email_score(synapse.is_reddit_email_verified) +
        scoring.x_email_score(synapse.is_x_email_verified) +
        scoring.insta_email_score(synapse.is_insta_email_verified) +
        scoring.tiktok_email_score(synapse.is_tiktok_email_verified)
    )

    # Calculate total score
    total_score = github_score + crypto_score + social_score + age_score + email_score

    # Normalize the score (assuming max possible score is 22)
    normalized_score = total_score / 22

    # Set the calculated score in the synapse object
    synapse.score = normalized_score

    return synapse