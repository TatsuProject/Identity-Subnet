from datetime import datetime

def commit_points(commits) -> float:
  if commits <= 10:
    return 0.1
  elif commits <= 50:
    return 0.3
  elif commits <= 200:
    return 0.5
  elif commits <= 500:
    return 0.7
  else:
    return 1.0

def follower_points(followers) -> float:
  if followers <= 5:
    return 0.1
  elif followers <= 20:
    return 0.3
  elif followers <= 50:
    return 0.5
  elif followers <= 100:
    return 0.7
  else:
    return 1.0


def calculate_account_age_points(created_at:int) -> float:
  years = (datetime.now().timestamp() - created_at)/(60*60*24*365)
  if years < 1:
    return 0.2
  elif years <= 2:
    return 0.4
  elif years <= 3:
    return 0.6
  elif years <= 5:
    return 0.8
  else:
    return 1.0

def calculate_repo_points(repos) -> float:
  if repos <= 2:
    return 0.1
  elif repos <= 10:
    return 0.3
  elif repos <= 20:
    return 0.5
  elif repos <= 50:
    return 0.7
  else:
    return 1.0


def crypto_score(balance) -> float:
  score = 0
  if balance > 1:
      score += 0.5
  else:
      score = balance/2
  return score

def transaction_score(transactions) -> float:
  if transactions <= 5:
    return 0.1 * transactions
  else:
    return 0.5

def staked_score(staked) -> float:
  if staked <= 1:
    return 0.1
  elif staked <= 10:
    return 0.3
  elif staked <= 20:
    return 0.5
  elif staked <= 50:
    return 0.7
  else:
    return 1.0
  

def linkedin_email_score(verified) -> float:
  if verified == True:
    return 1.0
  else:
    return 0
  
def eth_nft_score(balance: int) -> float:
  if balance >= 2:
    return 1.0
  elif balance == 1:
    return 0.5
  else:
    return 0.0
