#!/usr/bin/python3
"""Subscriber Count Module"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    base_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(
        base_url, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
