#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """ Queries to Reddit API """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                      'Chrome/91.0.4472.124 Safari/537.36'
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    try:
        dic = res.json()
        hot_posts = dic['data']['children']
        for post in hot_posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)
