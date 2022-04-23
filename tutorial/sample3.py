from numpy import full
import requests
import pandas as pd

df = pd.read_csv("sample.csv")
fullname = df['fullname']

uname = "vinay-ks"
token = "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"

for i in range(len(fullname)):
    url = 'https://api.github.com/repos/{}/commits'.format(fullname[i])
    commit_info = requests.get(url,auth=(uname,token)).json()
    print(commit_info)
    # print()
    for each in commit_info:
        print(each["commit"]["message"])