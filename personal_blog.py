import tumbleweed as td


blog = td.Blog(
        title="Emil's Blog",
        description="My new blog!",
        author="Emil Kovacev"
        )

blog.add('Post #1', 
    """### Welcome to my blog! 

    This is the first **post**, and
    as you can see it seems to be working pretty well :)
    just a *few things* right now, returns look like
    this 

    and this is a newline?"""
)

blog.add('Post #2', 'another post!')


blog.run(port=8000)
