from yin_resume_api.utils.orm_mongodb.desc import Desc
from yin_resume_api.utils.orm_mongodb.work import Work
from yin_resume_api.utils.orm_mongodb.education import Education
from yin_resume_api.utils.orm_mongodb.skill import Skill
from yin_resume_api.utils.orm_mongodb.social_network import Social_Network
from flask import jsonify


def bl_get_all_descs(**kwargs):
    descs = Desc.objects(**kwargs)
    return jsonify(descs), 200


def bl_get_all_works(**kwargs):
    works = Work.objects(**kwargs)
    return jsonify(works), 200


def bl_get_all_educations(**kwargs):
    educations = Education.objects(**kwargs)
    return jsonify(educations), 200


def bl_get_all_skills(**kwargs):
    skills = Skill.objects(**kwargs)
    return jsonify(skills), 200


def bl_get_all_social_networks(**kwargs):
    social_networks = Social_Network.objects(**kwargs)
    return jsonify(social_networks), 200