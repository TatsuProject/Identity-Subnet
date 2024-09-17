from datetime import datetime,time

def commit_points(commits) -> float:
    if commits <= 10:
        return 0.1
    elif commits <= 25:
        return 0.2
    elif commits <= 50:
        return 0.3
    elif commits <= 100:
        return 0.4
    elif commits <= 250:
        return 0.5
    elif commits <= 500:
        return 0.6
    elif commits <= 1000:
        return 0.7
    elif commits <= 2500:
        return 0.8
    elif commits <= 5000:
        return 0.9
    else:
        return 1.0

def x_follower_points(followers) -> float:
  if followers <= 20:
    return 0.1
  elif followers <= 50:
    return 0.2
  elif followers <= 75:
    return 0.3
  elif followers <= 100:
    return 0.4
  elif followers <= 200:
    return 0.5
  elif followers <= 500:
    return 0.6
  elif followers <= 1000:
    return 0.7
  elif followers <= 2000:
    return 0.8
  elif followers <= 5000:
    return 0.9
  else:
    return 1.0


def insta_follower_points(followers) -> float:
  if followers <= 20:
    return 0.1
  elif followers <= 50:
    return 0.2
  elif followers <= 75:
    return 0.3
  elif followers <= 100:
    return 0.4
  elif followers <= 200:
    return 0.5
  elif followers <= 500:
    return 0.6
  elif followers <= 1000:
    return 0.7
  elif followers <= 2000:
    return 0.8
  elif followers <= 5000:
    return 0.9
  else:
    return 1.0


def tiktok_follower_points(followers) -> float:
  if followers <= 20:
    return 0.1
  elif followers <= 50:
    return 0.2
  elif followers <= 75:
    return 0.3
  elif followers <= 100:
    return 0.4
  elif followers <= 200:
    return 0.5
  elif followers <= 500:
    return 0.6
  elif followers <= 1000:
    return 0.7
  elif followers <= 2000:
    return 0.8
  elif followers <= 5000:
    return 0.9
  else:
    return 1.0


def fb_follower_points(followers) -> float:
  if followers <= 20:
    return 0.1
  elif followers <= 50:
    return 0.2
  elif followers <= 75:
    return 0.3
  elif followers <= 100:
    return 0.4
  elif followers <= 200:
    return 0.5
  elif followers <= 500:
    return 0.6
  elif followers <= 1000:
    return 0.7
  elif followers <= 2000:
    return 0.8
  elif followers <= 5000:
    return 0.9
  else:
    return 1.0

def reddit_post_karma(karma) -> float:
    if karma <= 50:
        return 0.1
    elif karma <= 100:
        return 0.2
    elif karma <= 250:
        return 0.3
    elif karma <= 500:
        return 0.4
    elif karma <= 1000:
        return 0.5
    elif karma <= 2500:
        return 0.6
    elif karma <= 5000:
        return 0.7
    elif karma <= 10000:
        return 0.8
    elif karma <= 50000:
        return 0.9
    else:
        return 1.0


def reddit_comment_karma(karma) -> float:
    if karma <= 50:
        return 0.1
    elif karma <= 100:
        return 0.2
    elif karma <= 250:
        return 0.3
    elif karma <= 500:
        return 0.4
    elif karma <= 1000:
        return 0.5
    elif karma <= 2500:
        return 0.6
    elif karma <= 5000:
        return 0.7
    elif karma <= 10000:
        return 0.8
    elif karma <= 50000:
        return 0.9
    else:
        return 1.0



def x_account_age_points(created_at:int) -> float:
    years = (datetime.now().timestamp() - created_at)/(60*60*24*365)
    if years < 1:
        return 0.1
    elif years < 2:
        return 0.2
    elif years < 3:
        return 0.3
    elif years < 4:
        return 0.4
    elif years < 5:
        return 0.5
    elif years < 6:
        return 0.6
    elif years < 7:
        return 0.7
    elif years < 8:
        return 0.8
    elif years < 9:
        return 0.9
    else:
        return 1.0


def github_account_age_points(created_at:int) -> float:
    years = (datetime.now().timestamp() - created_at)/(60*60*24*365)
    if years < 1:
        return 0.1
    elif years < 2:
        return 0.2
    elif years < 3:
        return 0.3
    elif years < 4:
        return 0.4
    elif years < 5:
        return 0.5
    elif years < 6:
        return 0.6
    elif years < 7:
        return 0.7
    elif years < 8:
        return 0.8
    elif years < 9:
        return 0.9
    else:
        return 1.0


def reddit_account_age_points(created_at:int) -> float:
    years = (datetime.now().timestamp() - created_at)/(60*60*24*365)
    if years < 1:
        return 0.1
    elif years < 2:
        return 0.2
    elif years < 3:
        return 0.3
    elif years < 4:
        return 0.4
    elif years < 5:
        return 0.5
    elif years < 6:
        return 0.6
    elif years < 7:
        return 0.7
    elif years < 8:
        return 0.8
    elif years < 9:
        return 0.9
    else:
        return 1.0


def insta_account_age_points(created_at:int) -> float:
    years = (datetime.now().timestamp() - created_at)/(60*60*24*365)
    if years < 1:
        return 0.1
    elif years < 2:
        return 0.2
    elif years < 3:
        return 0.3
    elif years < 4:
        return 0.4
    elif years < 5:
        return 0.5
    elif years < 6:
        return 0.6
    elif years < 7:
        return 0.7
    elif years < 8:
        return 0.8
    elif years < 9:
        return 0.9
    else:
        return 1.0


def linkedin_account_age_points(created_at:int) -> float:
    years = (datetime.now().timestamp() - created_at)/(60*60*24*365)
    if years < 1:
        return 0.1
    elif years < 2:
        return 0.2
    elif years < 3:
        return 0.3
    elif years < 4:
        return 0.4
    elif years < 5:
        return 0.5
    elif years < 6:
        return 0.6
    elif years < 7:
        return 0.7
    elif years < 8:
        return 0.8
    elif years < 9:
        return 0.9
    else:
        return 1.0


def calculate_repo_points(repos) -> float:
    if repos <= 2:
        return 0.1
    elif repos <= 5:
        return 0.2
    elif repos <= 10:
        return 0.3
    elif repos <= 20:
        return 0.4
    elif repos <= 35:
        return 0.5
    elif repos <= 50:
        return 0.6
    elif repos <= 70:
        return 0.7
    elif repos <= 100:
        return 0.8
    elif repos <= 200:
        return 0.9
    else:
        return 1.0


def tao_crypto_score(balance) -> float:
  score = 0
  if balance > 1:
      score += 0.5
  else:
      score = balance/2
  return score

def eth_crypto_score(balance) -> float:
  score = 0
  if balance > 0.1:
      score += 0.5
  else:
      score = balance/2
  return score

def tao_transaction_score(transactions) -> (float):
  if transactions <= 5:
    return 0.1 * transactions
  else:
    return 0.5

def eth_transaction_score(transactions) -> (float):
  if transactions <= 5:
    return 0.1 * transactions
  else:
    return 0.5


def linkedin_email_score(verified) -> (float):
  if verified == True:
    return 1.0
  else:
    return 0
  

def reddit_email_score(verified) -> (float):
  if verified == True:
    return 1.0
  else:
    return 0
  

def x_email_score(verified) -> (float):
  if verified == True:
    return 1.0
  else:
    return 0
  

def insta_email_score(verified) -> (float):
  if verified == True:
    return 1.0
  else:
    return 0
  

def tiktok_email_score(verified) -> (float):
  if verified == True:
    return 1.0
  else:
    return 0
  