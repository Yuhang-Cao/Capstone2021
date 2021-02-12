import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id = "PimQNhTpwjICwQ",
                     client_secret = "bgD8hXMXxWJnhGNnVyz-Uoi-F7A5GQ",
                     password = "tradingalgo99",
                     user_agent = "NKumar",
                     username = "SignalLearn4Free")

subreddit = reddit.subreddit("cryptocurrency")

hot_crypto = subreddit.hot(limit = 10)

# for submission in hot_crypto:
#     if not submission.stickied:
#         print(submission.score)
#         print(submission.title)
#         print(submission.author.name)
#         print()

topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[],
                "num_comms":[],
                "time_created":[],
                "body":[]
            }

# t = 0
# print(dt.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))

def get_date(time):
    return dt.datetime.fromtimestamp(time)



for submission in hot_crypto:
    
    if not submission.stickied:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["num_comms"].append(submission.num_comments)
        time = int(submission.created_utc)
        time = dt.datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
        topics_dict["time_created"].append(time)
        topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(topics_data)
topics_data.to_csv('topics_data')