# pip install tweepy
import tweepy


# Tweepy 인증 설정
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 검색할 키워드와 트윗 개수 설정
keyword = "Elon Musk"
tweet_count = 10

# 트위터에서 트윗 검색
# 이전 코드...
# tweets = tweepy.Cursor(api.search, q=keyword, lang="en").items(tweet_count)
# 이후 코드...
tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(tweet_count)



# Google Cloud Natural Language API 인증 설정
client = language_v1.LanguageServiceClient.from_service_account_json('cogent-theater-398404-f6d67a3989ed.json')

# 감정 분석 결과 저장
sentiments = {"positive": 0, "negative": 0, "neutral": 0}

for tweet in tweets:
    text = tweet.text
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    score = sentiment.score
    magnitude = sentiment.magnitude

    if score > 0.1:
        sentiments["positive"] += 1
    elif score < -0.1:
        sentiments["negative"] += 1
    else:
        sentiments["neutral"] += 1

# 감정 분석 결과 시각화
labels = list(sentiments.keys())
sizes = list(sentiments.values())

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title(f"Sentiment Analysis for '{keyword}'")
plt.show()

