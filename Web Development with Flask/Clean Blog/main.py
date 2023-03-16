from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

my_email = "jeffreydevelops@gmail.com"
my_password = "@Kobby766!"


class Post:
    def __init__(self, id, subtitle, title, body):
        self.id = id
        self.subtitle = subtitle
        self.title = title
        self.body = body


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, email, email_message)


BLOG_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
blog_data = requests.get(url=BLOG_ENDPOINT).json()

post_objects = []
for data in blog_data:
    post = Post(data['id'], data['subtitle'], data['title'], data['body'])
    post_objects.append(post)


@app.route('/')
def homepage():
    return render_template('index.html', all_posts=post_objects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form_data = request.form
        send_email(form_data['name'], form_data['email'], form_data['phone'], form_data['message'])
        return render_template('contact.html', message_sent=True)
    return render_template('contact.html', message_sent=False)


@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for post in post_objects:
        if post_id == post.id:
            requested_post = post

    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
