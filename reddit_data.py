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

# 市值前十大的迷因幣及變體關鍵字
meme_coins = [
    "Shib", "Shiba Inu", 
    "Doge", "Dogecoin", 
    "BabyDoge", "Baby Doge Coin", 
    "Floki", "Floki Inu", 
    "Pepe", "Pepecoin",
    "Kishu", "Kishu Inu", 
    "Akita", "Akita Inu", 
    "Samoyed", "Samoyedcoin",
    "Dogelon", "Dogelon Mars",
    "Hoge", "Hoge Finance"
]

# 使用 OR 將所有變體連接成單一查詢字串
query = "Shib OR Doge OR Floki"  # 測試部分關鍵字


start_date = "2024-01-01"          # 開始日期
end_date = "2024-12-31"            # 結束日期

# 轉換日期為時間戳（UNIX 時間）
start_timestamp = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp())
end_timestamp = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp())

# 搜尋貼文
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.search(
    query=query,
    time_filter="all",  # 搜尋所有時間範圍內的貼文
    sort="new"
)

all_posts = list(posts)  # 將生成器內容轉為列表

# 初始化每日貼文計數
daily_post_counts = defaultdict(int)

# 計算每天的貼文數量
for post in all_posts:
    post_time = int(post.created_utc)
    if start_timestamp <= post_time <= end_timestamp:
        post_date = datetime.datetime.fromtimestamp(post_time).strftime("%Y-%m-%d")
        daily_post_counts[post_date] += 1

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
