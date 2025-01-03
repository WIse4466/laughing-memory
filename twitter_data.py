import tweepy
import csv

# 使用 Twitter API V2 認證
client = tweepy.Client(
    bearer_token='AAAAAAAAAAAAAAAAAAAAAJ6GxwEAAAAA7K%2BJVt8U7BtNxYdxBEE92%2F2kxig%3DzXxiP9LYY3ToLXUYOBweCixAaFjQJ58JdIeyAWeqDtQWb1Pd3j'
)

# 查詢推文
query = 'SHIB'
start_time = '2024-12-31T00:00:00Z'  # 2024年1月1日
end_time = '2024-12-31T23:59:59Z'  # 2024年12月31日

tweets = client.search_recent_tweets(query=query, max_results=100)

for tweet in tweets.data:
    print(f"Tweet: {tweet.text}")
    print("-" * 50)

# 將推文存儲到 CSV 檔案
with open('shib_2024_tweets.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tweet', 'Created At'])  # 寫入標題行

    for tweet in tweets.data:
        writer.writerow([tweet.text, tweet.created_at])

print("已成功將推文保存為 shib_2024_tweets.csv")

"""import tweepy

# 使用 Twitter API V2 認證
client = tweepy.Client(
    bearer_token='AAAAAAAAAAAAAAAAAAAAAJ6GxwEAAAAA7K%2BJVt8U7BtNxYdxBEE92%2F2kxig%3DzXxiP9LYY3ToLXUYOBweCixAaFjQJ58JdIeyAWeqDtQWb1Pd3j'
)

# 查詢推文
query = 'PEPE'
tweets = client.search_recent_tweets(query=query, max_results=100)

for tweet in tweets.data:
    print(f"Tweet: {tweet.text}")
    print("-" * 50)"""

"""import tweepy

# 使用你的 API 金鑰設置認證
consumer_key = "QTxN5y1NBhHwt0L2oZl05Wzzn"
consumer_secret = "CuVy9jDmpe4GjbnRdpVeh0fRtAiyMu5XPFwGR8f0Qg3BYskueI"
access_token = "1008935527800717312-oaZeLqKo5s3RHxaR4xRrZobUQ0xxQT"
access_token_secret = "FMGZdV2fkSoxZrFQyIH4YreGlLUCq7y9bi0a7Zz4XbZcV"

# 設置認證
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# 定義關鍵字
query = 'PEPE'

# 使用 Cursor 爬取推文
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="zh", tweet_mode='extended').items(100)

for tweet in tweets:
    print(f"Tweet: {tweet.full_text}")
    print(f"Likes: {tweet.favorite_count}")
    print(f"Retweets: {tweet.retweet_count}")
    print("-" * 50)"""
"""import ssl
import snscrape.modules.twitter as sntwitter

# 禁用 SSL 驗證
ssl._create_default_https_context = ssl._create_unverified_context

query = 'PEPE'
tweets = sntwitter.TwitterSearchScraper(query).get_items()

for tweet in tweets:
    print(tweet.content)"""


'''query = 'PEPE since:2024-01-01 until:2024-12-31'
tweets = sntwitter.TwitterSearchScraper(query).get_items()

for tweet in tweets:
    print(f"Tweet: {tweet.content}")
    print(f"Likes: {tweet.likeCount}")
    print(f"Retweets: {tweet.retweetCount}")
    print("-" * 50)
import csv

# 儲存為 CSV
with open('pepe_tweets.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tweet', 'Likes', 'Retweets'])
    for tweet in tweets:
        writer.writerow([tweet.full_text, tweet.favorite_count, tweet.retweet_count])
    
    print("Data has been saved to 'pepe_tweets_2024.csv'.")'''
