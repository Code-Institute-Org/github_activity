import os
import requests
from datetime import datetime, timedelta

# checking for env file
if os.path.exists("env.py"):
    import env

# Assigning hidden token
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN' )

# creating header field
headers = { "Authorization" : "token {}".format(GITHUB_TOKEN)}

# hard coding days in past to check
days = 350

# counting commits
commit_count = 0

# hard coding user for now
user = 'alimgee'
# api url
url = f'https://api.github.com/'

# https://api.github.com/users/alimgee/repos
repo_url = f'{url}users/{user}/repos'

# passing repos end point to repos variable
repos = requests.get(repo_url, headers = headers).json()
# looping through repos variable to get the name of each repo in users repositry
for repo in repos:
    name = repo['name']
    # creating commits end point
    one_repo_url = f'{url}repos/{user}/{name}/commits'
    
    try:
        # getting each commit endpoint
        response =requests.get(one_repo_url, headers = headers)
        # catching error status
        response.raise_for_status()
        commits = response.json()
        # looping through each commit on commits endpoint
        for commit in commits:
            # get commit field
            one_commit =  commit['commit']
            # finding date of commit
            date_str = one_commit['author']['date']
            # parsing commit date to be suitable for datetime
            date_str = date_str[0:10].replace('-' , ' ')
            # converting commit date to datetime object
            datetimeobj=datetime.strptime(date_str, "%Y %m %d")
            # finding current date
            current_date = datetime.now()
            # getting date in past as dateobject
            past_date = current_date - timedelta(days=days)
            # if commit date comes after date in the past increase commit count
            if datetimeobj > past_date:
                commit_count = commit_count + 1

    except requests.exceptions.HTTPError as err:
        # catching any errors       
        print("unable to connect to repo",  one_repo_url, "error....",err)

# printting results
print (f'There are {commit_count} commit(s) in {user}s repo in the last {days} days ') 

