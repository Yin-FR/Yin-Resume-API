from yin_resume_api.utils.github_operation import grc
from yin_resume_api.utils.formatting_tools import get_repos_formatted
from yin_resume_api.orm_mongodb.github_repo import GithubRepo
from tqdm import tqdm
from flask import jsonify


def bl_get_all_repos(username):
    if not username:
        return "Invalid username", 500
    repos = grc.get_all_repo()
    languages = grc.get_language_repo()
    branches = grc.get_branches_repos()
    result = get_repos_formatted(repos, languages, branches)
    for index_repo in tqdm(range(len(result))):
        each_formatted_repo = result[index_repo]
        repo_in_db = GithubRepo.objects(title=each_formatted_repo["title"]).count()
        if not repo_in_db:
            github_repo = GithubRepo(
                cover_url=each_formatted_repo["cover_url"],
                language=each_formatted_repo["language"],
                description=each_formatted_repo["description"],
                main_language=each_formatted_repo["main_language"],
                title=each_formatted_repo["title"],
                demo_url=each_formatted_repo["demo_url"],
                url=each_formatted_repo["url"]
            )
            github_repo.save()
        else:
            repo_in_db = GithubRepo.objects(title=each_formatted_repo["title"])[0]
            demo_url = repo_in_db.demo_url
            result[index_repo]["demo_url"] = demo_url
    return jsonify(result), 200
