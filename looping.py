import requests
from bs4 import beatifulsoup as bs
github_user = input("git hub user:")
url='https://github.com/'+github_user
r=requests.get(url)
soup=bs(r.content, 'html.parser')
profile_image=soup.find('img',{'alt':'avatar'})['src']
print(profile_image)