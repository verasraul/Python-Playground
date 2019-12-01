__author__ = 'verasraul'
import requests
import json

# https://api.github.com/usrs/:gitUser
def git_user_api(User):
    site = requests.get(f"https://api.github.com/users/{User}")
    siteResponse = site.json()
    return json.dumps(siteResponse, indent=4, sort_keys=True)


def gemini():
    site = requests.get("https://api.gemini.com/v1/pubticker/btcusd")
    siteResponse = site.json()
    return json.dumps(siteResponse, indent=4, sort_keys=True)


print(git_user_api("verasraul"))
# print(gemini())