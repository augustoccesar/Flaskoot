from lib.api.models.mongo.user import User

from lib.api.utils.cache import cache


@cache.cached(timeout=60, key_prefix="get_users")
def get_users():
    print('Accessing DB (for demonstrating the cache)')
    return [user for user in User.objects()]


def get_user_by_id(id: str):
    return User.objects(id=id).first()
