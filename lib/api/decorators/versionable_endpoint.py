import functools
from flask import request


def versionable_endpoint(versions: list):
    def versionable_endpoint_wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            version_str = request.headers.get('API-Version') \
                or request.args.get('version')

            version = int(version_str) if version_str else None

            if not version or version not in versions:
                version = max(versions)

            return func(*args, **dict(kwargs, version=version))
        return wrapped
    return versionable_endpoint_wrapper
