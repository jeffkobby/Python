from flask import Flask, render_template
import requests
from post import Post
from pprint import pp

BLOG_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
blog_api_response = requests.get(url=BLOG_ENDPOINT)
blog_api_data = blog_api_response.json()

post_objects = []
for post in blog_api_data:
    post_object = Post(id=post['id'], title=post['title'], subtitle=post['subtitle'],
                       body=post['body'])
    post_objects.append(post_object)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def blog_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
