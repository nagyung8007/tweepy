# tweepy >= 4.9
# twitter API V2


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




# tweepy.StreamClient 클래스를 상속받는 클래스
class TwitterStream(tweepy.StreamingClient):
    def on_data(self, raw_data):
        print(raw_data)

# 규칙 제거 함수
def delete_all_rules(rules):
    # 규칙 값이 없는 경우 None 으로 들어온다.
    if rules is None or rules.data is None:
        return None
    stream_rules = rules.data
    ids = list(map(lambda rule: rule.id, stream_rules))
    client.delete_rules(ids=ids)

# 스트림 클라이언트 인스터턴스 생성
client = TwitterStream(access_token)

# 모든 규칙 불러오기 - id값을 지정하지 않으면 모든 규칙을 불러옴
rules = client.get_rules()

# 모든 규칙 제거
delete_all_rules(rules)

# 스트림 규칙 추가
client.add_rules(tweepy.StreamRule(value="#Elon_Musk has:images"))

# 스트림 시작
client.filter()

