import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from yin_resume_api.models.repo import Repo  # noqa: E501
from yin_resume_api import util

from yin_resume_api.bussiness_logical.bl_project import bl_get_all_repos


def get_repos(username):  # noqa: E501
    """Get the github repos information by username

    Get the git repos information # noqa: E501

    :param username: Username of github
    :type username: str

    :rtype: Union[List[Repo], Tuple[List[Repo], int], Tuple[List[Repo], int, Dict[str, str]]
    """
    return bl_get_all_repos(username)
