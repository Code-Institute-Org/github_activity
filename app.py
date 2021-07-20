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


def count_commits(user, days):
    '''
    function to calulate the amount of commits in a users
    github repositry from a given time span in days from today
    Params should be a github username and the amount of days
    in the past to compare against
    '''
    # building url to get all repo names
    url = f'https://api.github.com/'
    repo_url = f'{url}users/{user}/repos'
    commit_count = 0

    # passing repos end point to repos variable
    repos = requests.get(repo_url, headers=headers).json()

    # checking for valid username
    if 'message' in repos:
        if repos['message'] == 'Not Found':
            print("incorrect value supplied for username")
            return commit_count

    # checking days param is an int
    check_date_param = isinstance(days, int)
    if not check_date_param:
        print("Please ensure your days value is an integer")
        return commit_count

    # checking if a value greater than 0 is passed in for days
    if days < 1 :
        print("Please ensure your days value is greater than 0")
        return commit_count

    # looping through repos variable to get the name of each repo
    for repo in repos:
        name = repo['name']
        # creating commits end point
        one_repo_url = f'{url}repos/{user}/{name}/commits'

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
                past_date = current_date - timedelta(days=days)
                # if commit date comes after past date increase commit count
                if datetimeobj > past_date:
                    commit_count = commit_count + 1

        except requests.exceptions.HTTPError as err:
            # catching any errors
            print("unable to connect to repo",  one_repo_url, "error....", err)

    return commit_count

