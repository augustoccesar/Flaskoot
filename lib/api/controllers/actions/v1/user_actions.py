from lib.api.services import user_services


def get_users():
    return user_services.get_users()


def get_user_by_id(id: str):
    return user_services.get_user_by_id(id)
