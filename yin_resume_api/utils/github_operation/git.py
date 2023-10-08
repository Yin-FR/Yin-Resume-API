import os


class GithubBaseController:
    def __init__(self, id, base_url, username, **kwargs) -> None:
        self.id = id
        self.base_url = base_url
        self.username = username

        for k, w in kwargs.items():
            self[k] = w

        self.headers = {}