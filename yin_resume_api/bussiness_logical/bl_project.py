from yin_resume_api.utils.github_operation.git_repo import GithubRepoController
from yin_resume_api.utils.api import get_data_from_url
from flask import jsonify


def bl_get_all_repos(username):
    grc = GithubRepoController(username)
    repos = grc.get_all_repo()
    result = []
    for each_repo in repos:
        title = " ".join([word.capitalize() for word in each_repo["name"].split("-")])
        language = get_data_from_url(each_repo["languages_url"])[1]
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