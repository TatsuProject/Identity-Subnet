import json
import requests
import time
import scoring
import bittensor as bt
def get_user_data(username):
  # Set the base URL for the GitHub API
  base_url = "https://api.github.com/users/"

  # Construct the URL for the user's public data
  url = base_url + username

  # Send a GET request to the API
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Parse the JSON response
    user_data = json.dumps(response.json())
    return user_data
  else:
    print("Failed to retrieve user data.")
    return -1



GITHUB_API_URL = 'https://api.github.com'

def get_repositories(user):
    repos = []
    page = 1
    while True:
        url = f'{GITHUB_API_URL}/users/{user}/repos?per_page=1000&page={page}'
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f'Error fetching repositories: {response.json()}')
        data = response.json()
        if not data:
            break
        repos.extend([(repo['owner']['login'], repo['name']) for repo in data])
        page += 1
        time.sleep(1)  # To avoid hitting rate limits
    return repos

def get_commit_count(owner, repo, user):
    url = f'{GITHUB_API_URL}/repos/{owner}/{repo}/commits?author={user}&per_page=1000'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Error fetching commits for {repo}: {response.json()}')
    # Get the 'Link' header to find the total number of pages
    link_header = response.headers.get('Link')
    if not link_header:
        return len(response.json())
    last_page_url = [link for link in link_header.split(',') if 'rel="last"' in link]
    if not last_page_url:
        return len(response.json())
    # Extract the last page number
    last_page_url = last_page_url[0].split(';')[0].strip('<>')
    last_page = int(last_page_url.split('page=')[-1])
    # Each page has up to 100 commits
    return last_page * 100

def total_commits(USER):
  repositories = get_repositories(USER)
  total_commits = 0
  for owner, repo in repositories:
      try:
          commit_count = get_commit_count(owner, repo, USER)
          total_commits += commit_count
      except Exception as e:
          time.sleep(1)  # To avoid hitting rate limits
          continue
  return total_commits


api_key = "NMRZYV14D2X7NC349BYR9TUWW6FA2ZDCEG"  



def get_transaction_count(address, api_key):
    url = "https://api.etherscan.io/api"
    start_block = 0
    end_block = 99999999
    page = 1
    offset = 10000  # Using a smaller offset to stay within the limits
    total_transactions = 0

    while True:
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": "asc",
            "apikey": api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == '1':
            transactions = data['result']
            total_transactions += len(transactions)
            if len(transactions) < offset:
                break
            page += 1
        else:
            print(f"Error: {data['message']}")
            break

    return total_transactions

def get_balance(address, api_key):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        balance = int(data['result']) / 10**18  # Convert balance from Wei to Ether
        return balance
    else:
        print(f"Error: {data['message']}")
        return 0

def get_account_info(address):
    api_key = "NMRZYV14D2X7NC349BYR9TUWW6FA2ZDCEG"
    transaction_count = get_transaction_count(address, api_key)
    balance = get_balance(address, api_key)
    account_info = {
        "transaction_count": transaction_count,
        "balance": balance
    }
    return account_info

def get_tao_balance(coldkey):
    sub = bt.subtensor( network = 'finney' )
    balance = sub.get_balance(address = coldkey)
    return balance

