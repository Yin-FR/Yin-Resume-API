from yin_resume_api.utils.github_operation import grc
from yin_resume_api.utils.api import get_data_from_url
from flask import jsonify


def bl_get_all_repos(username):
    repos = grc.get_all_repo()
    languages = grc.get_language_repo()
    branches = grc.get_branches_repos()
    result = []
    for each_repo in repos:
        branches_info = branches[each_repo["name"]]
        main_branch_name = "main"
        for each_branch in branches_info:
            if each_branch["name"] == "master":
                main_branch_name = "master"
        cover_url = each_repo["html_url"] + "/blob/{}/static/imgs/demo.png?raw=true".format(main_branch_name)
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
            "main_language": main_language,
            "cover_url": cover_url
        })
    return jsonify(result), 200