#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():

    # using request to get a website url, using GET
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")

    # if statement to parse the JSON data
    if r.status_code == 200:
        data = r.json()

        # iterate thought the posts of website and prints them
        for post in data:
            print(post["title"])

    else:
        print(f"Status Code: {r.status_code}")


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        data = r.json()

        # Structuring the data into a list of dict
        posts = []
        for post in data:
            posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("open.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)

        print("Data saved to posts.csv")

    else:
        print(f"Status Code: {r.status_code}")
