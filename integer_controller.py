from flask import g
from database import user_integer_map


# methods for accessing integers and modifying them
def set_integer_value(data):
    user_integer_map[g.email]["integer_value"] = data.get("current")


def get_incremented_integer():
    user_integer_map[g.email]["integer_value"] += 1
    return user_integer_map[g.email]["integer_value"]


def get_current_integer():
    print user_integer_map
    return user_integer_map[g.email]["integer_value"]


