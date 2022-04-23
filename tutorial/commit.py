import requests
import pandas as pd

df = pd.read_csv("sample.csv")
fullname= df['fullname']
uname="HDoleker"
token="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"
for i in range(len(fullname)):
 url= 'https://api.github.com/repos/{}/comits'.format(fullname[i])
 commit_info=requests.get(url,auth=(uname,token)).json()
 print(commit_info)
 for each in commit_info:
  print(each["commit"]["message"])
