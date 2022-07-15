from flask import Flask, render_template
import datetime as dt
from jinja_markdown import MarkdownExtension


class Post:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date.strftime('%Y-%m-%d')

    def render(self):
        return {
            'title': self.title,
            'content': self.content,
            'date': self.date
        }


class Blog(Flask):
    def __init__(self, title, description, author, *args, **kwargs):
        self.title = title
        self.description = description
        self.author = author
        self.posts = []

        super(Blog, self).__init__(__name__, *args, **kwargs)

        self.jinja_env.add_extension(MarkdownExtension)

        self.add_generic_template(
            path='/', 
            title='Home', 
            template='index.html', 
            blog_title=self.title,
            description=self.description,
            author=self.author,
        )

    def add(self, title, content, date=dt.datetime.now()):
        post = Post(title, content, date)
        self.posts.append(post)

    def add_generic_template(self, path, title, template, **kwargs):
        def add_func():
            return render_template(template, posts=self.posts, **kwargs)

        self.add_url_rule(path, title, add_func)

