import praw
import datetime
import csv
from collections import defaultdict

# Reddit API 認證
reddit = praw.Reddit(
    client_id="ZgZyyq7EZwJdQwmyDDYBcA",          # 填入你的 client_id
    client_secret="Uv0HTtJr2jg5A07eBHWh69CLTSbhcg",  # 填入你的 client_secret
    user_agent="ShibaScraper by /u/BeautifulTight5272"  # 自訂 user_agent
)

# 定義查詢參數
subreddit_name = "cryptocurrency"  # 搜尋的子版

# 定義查詢字串
queries = [
    "Shib OR Shiba Inu",  # 查詢 Shib 和 Shiba Inu
    "Doge OR Dogecoin",  # 查詢 Doge 和 Dogecoin
    "BabyDoge OR Baby Doge Coin",  # 查詢 BabyDoge 和 Baby Doge Coin
    "Floki OR Floki Inu",  # 查詢 Floki 和 Floki Inu
    "Pepe OR Pepecoin",  # 查詢 Pepe 和 Pepecoin
    "Kishu OR Kishu Inu",  # 查詢 Kishu 和 Kishu Inu
    "Akita OR Akita Inu",  # 查詢 Akita 和 Akita Inu
    "Samoyed OR Samoyedcoin",  # 查詢 Samoyed 和 Samoyedcoin
    "Dogelon OR Dogelon Mars",  # 查詢 Dogelon 和 Dogelon Mars
    "Hoge OR Hoge Finance"  # 查詢 Hoge 和 Hoge Finance
]

# 使用 OR 將所有變體連接成單一查詢字串
#query = " OR ".join(meme_coins)  # 測試部分關鍵字
#print(query)


start_date = "2024-01-01"          # 開始日期
end_date = "2024-12-31"            # 結束日期

# 轉換日期為時間戳（UNIX 時間）
start_timestamp = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp())
end_timestamp = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp())

"""
# 搜尋貼文
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.search(
    query=query,
    time_filter="all",  # 搜尋所有時間範圍內的貼文
    sort="new"
)
"""

# 初始化每日貼文計數
daily_post_counts = defaultdict(int)

# 執行每個查詢
for query in queries:
    # 搜尋貼文
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.search(
        query=query,
        time_filter="all",  # 搜尋所有時間範圍內的貼文
        sort="new"
    )

    all_posts = list(posts)  # 將生成器內容轉為列表
    
    # 計算每天的貼文數量
    for post in all_posts:
        post_time = int(post.created_utc)
        if start_timestamp <= post_time <= end_timestamp:
            post_date = datetime.datetime.fromtimestamp(post_time).strftime("%Y-%m-%d")
            daily_post_counts[post_date] += 1

# 初始化每日貼文計數
#daily_post_counts = defaultdict(int)

# 輸出每日貼文數量
print("Daily post counts:")
for date, count in sorted(daily_post_counts.items()):
    print(f"{date}: {count}")

# 儲存每日貼文數量到 CSV
with open("daily_meme_coin_post_counts.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Post Count"])
    for date, count in sorted(daily_post_counts.items()):
        writer.writerow([date, count])

print(f"Saved daily post counts to 'daily_meme_coin_post_counts.csv'")