import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from yin_resume_api.models.desc import Desc  # noqa: E501
from yin_resume_api.models.education import Education  # noqa: E501
from yin_resume_api.models.skill import Skill  # noqa: E501
from yin_resume_api.models.social_network import SocialNetwork  # noqa: E501
from yin_resume_api.models.work import Work  # noqa: E501
from yin_resume_api import util

from yin_resume_api.bussiness_logical.bl_resume import bl_get_all_descs, bl_get_all_educations, bl_get_all_works, bl_get_all_skills, bl_get_all_social_networks


def get_descs(name_id=None):  # noqa: E501
    """Find person description by ID

    Get the text about self description # noqa: E501

    :param name_id: ID of the person
    :type name_id: str

    :rtype: Union[Desc, Tuple[Desc, int], Tuple[Desc, int, Dict[str, str]]
    """
    if name_id:
        return bl_get_all_descs(name_id=name_id)
    return bl_get_all_descs()


def get_educations(name_id=None):  # noqa: E501
    """Find person description by ID

    Get all education info for a person by ID # noqa: E501

    :param name_id: ID of the person
    :type name_id: str

    :rtype: Union[Education, Tuple[Education, int], Tuple[Education, int, Dict[str, str]]
    """
    if name_id:
        return bl_get_all_educations(name_id=name_id)
    return bl_get_all_educations()


def get_works(name_id=None):  # noqa: E501
    """Find person description by ID

    Get all work info for a person by ID # noqa: E501

    :param name_id: ID of the person
    :type name_id: str

    :rtype: Union[Work, Tuple[Work, int], Tuple[Work, int, Dict[str, str]]
    """
    if name_id:
        return bl_get_all_works(name_id=name_id)
    return bl_get_all_works()


def get_skills(name_id=None):  # noqa: E501
    """Find person description by ID

    Get all skills info for a person by ID # noqa: E501

    :param name_id: ID of the person
    :type name_id: str

    :rtype: Union[Skill, Tuple[Skill, int], Tuple[Skill, int, Dict[str, str]]
    """
    if name_id:
        return bl_get_all_skills(name_id=name_id)
    return bl_get_all_skills()


def get_social_networks(name_id=None):  # noqa: E501
    """Find person description by ID

    Get all work info for a person by ID # noqa: E501

    :param name_id: ID of the person
    :type name_id: str

    :rtype: Union[Work, Tuple[Work, int], Tuple[Work, int, Dict[str, str]]
    """
    if name_id:
        return bl_get_all_social_networks(name_id=name_id)
    return bl_get_all_social_networks()
