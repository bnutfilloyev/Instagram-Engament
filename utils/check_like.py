import instaloader
from instaloader import Post

session_path = "<session-file-path>"
L = instaloader.Instaloader()
L.load_session_from_file(username='haminmoshotmi', filename=session_path)


async def get_owner(shortcode):
    post = Post.from_shortcode(context=L.context, shortcode=shortcode)
    return post.owner_username


async def check_like(shortcode):
    username_list = []
    
    post = Post.from_shortcode(context=L.context, shortcode=shortcode)
    for like in post.get_likes():
        username_list.append(like.username)

    if await get_owner(shortcode) in username_list:
        return True

    return False

