import os
from quart import Quart, request
from paho.mqtt.client import topic_matches_sub

# EXAMPLE:
# AUTH = 'kipe:salasana:location/{user},battery/{user}|example:password:test/#'
AUTH = [
    [
        user,
        password,
        list(filter(None, [topic.strip() for topic in topics.split(',') if topic]))
    ]
    for user, password, topics in [
        x.split(':')
        for x in filter(None, os.environ.get('AUTH', '').strip().split('|'))
    ]
]


app = Quart('emqx-auth')

@app.route('/auth')
async def auth():
    for user, password, _ in AUTH:
        if user == request.args.get('user') and password == request.args.get('password'):
            return '', 200
    return '', 403


@app.route('/acl')
async def acl():
    for user, _, topics in AUTH:
        if user == request.args.get('user'):
            acl_topic = request.args.get('topic')
            for topic in topics:
                if topic_matches_sub(topic.format(user=user), acl_topic):
                    return '', 200
    return '', 403


if __name__ == '__main__':
    app.run()
