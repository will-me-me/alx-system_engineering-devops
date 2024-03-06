#!/usr/bin/python3
"""10 Hot Posts Listed Module"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(
        url, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"][:10]
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
