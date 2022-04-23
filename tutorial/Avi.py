import requests
import pandas as pd
df = pd.DataFrame(columns=["fullname","language","num_of_stars"])
results= requests.get("https://api.github.com/search/repositories?q=language:C+stars<100&per_page=10").json()

for repo in results['items']:
 d={'fullname':repo['full_name'], 'language': repo['language'], "num_of_stars":repo['stargazers_count']}
 df=df.append(d,ignore_index=True)
 
df.to_csv("sample.csv",index=False)
