from flask import Flask
from redis import Redis

app = Flask(__name__)
# We connect to the hostname 'redis'. Docker Compose's DNS handles this resolution.
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():    
    # Increment the 'hits' counter in Redis
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    # 0.0.0.0 allows connection from outside this container (e.g., from Nginx)
    app.run(host="0.0.0.0", debug=True)