import requests
from dotenv import load_dotenv
import os
from datetime import timedelta, datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

def fetching_repo():
    date_list = []
    headers = {"Authorization": f"token {TOKEN}"}

    response = requests.get(
    "https://api.github.com/user/repos",
    headers=headers)

    print(response.status_code)
    repos = response.json()

    repo_list = []
    for repo in repos:
        repo_name = repo['name']
        print(repo_name)
        repo_list.append(repo_name)
        repos_response = requests.get(f'https://api.github.com/repos/{USERNAME}/{repo_name}/commits', headers=headers)
    

        commits = repos_response.json()
        for commit in commits:
            commit_date = commit['commit']['author']['date']
            mod_commit_date = commit_date.split('T')
            date_list.append(mod_commit_date[0])
    print(date_list)
    return(date_list,repo_list)


def mmr_counting():
 dates, repo_list = fetching_repo()
 #MMR logic 
 mmr = 0
 
 unique_dates = sorted(set(dates))
 streak = 1
 max_streak = 1
 for i in range(1, len(unique_dates)):
        date_string = unique_dates[i]
        date_string2 = unique_dates[i-1]
        date1 = datetime.strptime(date_string, "%Y-%m-%d")

        date2 = datetime.strptime(date_string2, "%Y-%m-%d")
        difference = date1 - date2

        if difference.days == 1:
            streak = streak + 1
        if streak > max_streak:
            max_streak = streak
        else:
            streak = 1 

 print(repo_list)
 mmr = mmr + len(dates)*10 + max_streak*5 + len(repo_list)* 100
 print(mmr)
mmr_counting()
