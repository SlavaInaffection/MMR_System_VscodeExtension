import requests
from dotenv import load_dotenv
import os
from datetime import timedelta, datetime, date
import json

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
        
        repo_list.append(repo_name)
        repos_response = requests.get(f'https://api.github.com/repos/{USERNAME}/{repo_name}/commits', headers=headers)
    

        commits = repos_response.json()
        for commit in commits:
            commit_date = commit['commit']['author']['date']
            mod_commit_date = commit_date.split('T')
            date_list.append(mod_commit_date[0])
    
    return(date_list,repo_list)

def get_rank(mmr):
    if mmr >= 9000:
        return "Immortal"
    elif mmr >= 7000:
        return "Divine"
    elif mmr >= 5000:
        return "Ancient"
    elif mmr >= 3500:
        return "Legend"
    elif mmr >= 2000:
        return "Archon"
    elif mmr >= 1000:
        return "Crusader"
    elif mmr >= 500:
        return "Guardian"
    else:
        return "Herald"

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

    
    mmr = mmr + len(dates)*10 + max_streak*30 + len(repo_list)* 100
    
    last_commit = max(unique_dates)
    today = date.today()
    last_commit_1 = datetime.strptime(last_commit, "%Y-%m-%d").date()
    today_diff = today - last_commit_1
    if today_diff.days >= 4:
        
        mmr = mmr - today_diff.days * 10

    dates, repo_list = fetching_repo()
    # ... all your mmr calculation code ...
    
    # at the end, still inside mmr_counting:
    rank = get_rank(mmr)
    data = {
        "mmr": mmr,
        "rank": rank,
        "last_commit": last_commit,
        "streak": max_streak
    }
    with open("mmr.json", "w") as f:
        json.dump(data, f)
    print(f"{rank} — {mmr} MMR")


        


mmr_counting()
