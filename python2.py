import instaloader

loader = instaloader.Instaloader()


username = "galgotiasmoments"


profile = instaloader.Profile.from_username(loader.context, username)


posts = profile.get_posts()


for post in posts:

    post_id = post.mediaid

    post_url = post.url
   
    caption = post.caption

    likes = post.likes
    
    comments = post.comments


   
    print(f"Post ID: {post_id}")
    print(f"Post URL: {post_url}")
    print(f"Caption: {caption}")
    print(f"Likes: {likes}")
    print(f"Comments: {comments}")

    print("")


for post in posts:
    loader.download_post(post, target=username)