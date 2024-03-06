#!/usr/bin/python3
"""Recursive Sorted Reddit API Call Module"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}, i=0):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript,
    but java should not).
    """

    limit = 100
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit={limit}"

    if after:
        url += f"&after={after}"

    if i == 0:
        for word in word_list:
            word_count[word.lower()] = 0

    response = requests.get(
        url, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        i = 1

        for post in posts:
            for word in word_list:
                if word.lower() in post["data"]["title"].lower():
                    word_count[word.lower()] += 1
            hot_list.append(post["data"]["title"])

        if after:
            return count_words(subreddit, word_list, hot_list, after, word_count, i)
        else:
            # Sorting the results
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")

    else:
        return None
