from utils.db_api.mongo import post_db


async def get_links(count=10):
    """
    Get the links from the database.
    """
    links = post_db.find().to_list(count)

    return links