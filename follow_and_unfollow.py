from flask import Flask, jsonify, request
from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


app = flask(__name__)

app.id_count     = 1
app.users        = {}
app.tweets       = []
app.json_encoder = CustomJSONEncoder


@app.route('/follow',methods='POST')
def follow():
    payload           = request.json
    user_id           = int(payload['id'])
    user_id_to_follow = int(payload['follow'])

    if user_id not in app.users or user_id_to_follow not in app.users:
        return "사용자가 존재하지 않습니다.", 400

    user = app.users[user_id]
    user.setdefault('follow', set()).add(user_id_to_follow)

    return jsonify


@app.route('/unfollow', methods='POST')
def unfollow():
    payload         = request.json
    user_id         = int(payload['id'])
    user_id_to_follow = int(payload['unfollow'])

    if user_id not in app.users or user_id_to_follow not in app.users:
        return "사용자가 존재하지 않습니다.", 400

    user = app.users[user_id]
    user.setdefault('follow', set()).discard(user_id_to_follow)  
        #remove 는 없는 값 버리면 오류나지만, discard 는 없으면 그냥 무시하기 때문에 사용.

    return jsonify(user)

    