from yin_resume_api.utils.github_operation import grc
from yin_resume_api.utils.api import get_data_from_url
from flask import jsonify


def bl_get_all_repos(username):
    repos = grc.get_all_repo()
    languages = grc.get_language_repo()
    result = []
    for each_repo in repos:
        title = " ".join([word.capitalize() for word in each_repo["name"].split("-")])
        language = languages[each_repo["name"]]
        if language:
            main_language = max(language, key=language.get)
        else:
            main_language = None
        description = each_repo["description"]
        result.append({
            "title": title,
            "language": language,
            "description": description,
            "main_language": main_language
        })
    return jsonify(result), 200