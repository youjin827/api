from flask import jsonify, Flask, request

app = Flask(__name__)
app.users = {}
app.id_count = 1
app.tweets = []

@app.route('/tweet',methods=['POST'])
def tweet():
    user_tweet = request.json
    tweet   = user_tweet['tweet']

    '''if user_id not in app.users:
        return '사용자가 존재하지 않습니다.', 400
'''

    if len(tweet) > 300:
        return '300자를 초과했습니다.', 400

    app.database.execute(text("""
    
        user_id,
        tweet
    ) values (
        :id,
        :tweet
    )
"""), user_tweet)

    return '',200