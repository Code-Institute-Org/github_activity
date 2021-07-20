import os
import requests
from datetime import datetime, timedelta

# checking for env file
if os.path.exists("env.py"):
    import env

# Assigning hidden token
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

# creating header field
headers = {"Authorization": "token {}".format(GITHUB_TOKEN)}


def calc_project_commits(repo_url, timeframe):

    commit_count = 0
    url = f'https://api.github.com/'

    # param checks - checking github domain in url
    if 'https://github.com/' not in repo_url:
        print("Not a github url")
        return commit_count

    # checking timeframe param is an int
    check_date_param = isinstance(timeframe, int)
    if not check_date_param:
        print("Please ensure your timeframe value is an integer")
        return commit_count

    # checking if a value greater than 0 is passed in for timeframe
    if timeframe < 1:
        print("Please ensure your timeframe value is greater than 0")
        return commit_count

    # stripping url
    user = repo_url[19:].split('/')[0]
    repo = repo_url[19:].split('/')[1]


    # creating commits end point
    one_repo_url = f'{url}repos/{user}/{repo}/commits'

    try:
        # getting each commit endpoint
        response = requests.get(one_repo_url, headers=headers)

        # catching error status
        response.raise_for_status()
        commits = response.json()

        # looping through each commit on commits endpoint
        for commit in commits:
            # get commit field
            one_commit = commit['commit']
            # finding date of commit
            date_str = one_commit['author']['date']
            # parsing commit date to be suitable for datetime
            date_str = date_str[0:10].replace('-', ' ')
            # converting commit date to datetime object
            datetimeobj = datetime.strptime(date_str, "%Y %m %d")
            # finding current date
            current_date = datetime.now()
            # getting date in past as dateobject
            past_date = current_date - timedelta(days=timeframe)
            # if commit date comes after past date increase commit count
            if datetimeobj > past_date:
                commit_count = commit_count + 1

    except requests.exceptions.HTTPError as err:
        # catching any errors
        print("unable to connect to repo",  one_repo_url, "error....", err)

    return commit_count



