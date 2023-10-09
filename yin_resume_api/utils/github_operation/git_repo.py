from yin_resume_api.utils.api import get_data_from_url
from yin_resume_api.utils.github_operation.git import GithubBaseController

import os
import logging
from tqdm import tqdm

logging.getLogger().setLevel(logging.INFO)


class GithubRepoController(GithubBaseController):   # operations of GitHub API
    def __init__(self, id="github", base_url="https://api.github.com",
                 token_name="GITHUB_ACCESS_TOKEN",
                 username_name="GITHUB_USERNAME",
                 **kwargs) -> None:
        super().__init__(id, base_url, token_name, username_name, **kwargs)
        self.headers = {
            'Authorization': 'Bearer {}'.format(self.token),
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        self.inited = False
        self.repos = []
        self.language_repo = {}
        self.language_count = {}
        self.language_percentage = {}
        self.branch_repo = {}

    def init(self):
        logging.info("Initing Github Controller ...")
        logging.info("Retrieving all repos ...")
        self.get_all_repo()
        logging.info("Retrieving all branches ...")
        self.get_branches_repos()
        logging.info("Analysing language of all repos ...")
        self.get_language_repo()
        logging.info("Counting bytes of each language for all repos ...")
        self.get_language_count()
        logging.info("Calculating language percentage ...")
        self.get_language_percentage()
        self.inited = True

    # get name list of all repos
    def get_all_repo(self) -> list:
        if len(self.repos):
            return self.repos
        url = os.path.join(self.base_url, "users/{}/repos".format(self.username))
        status, data = get_data_from_url(url, self.headers)
        self.repos = data if status == 200 else self.repos
        return self.repos
    
    # get branches of all repos
    def get_branches_repos(self) -> list:
        if self.branch_repo:
            return self.branch_repo
        self.get_all_repo()
        repo_names = [repo["name"] for repo in self.repos]
        for repo_name in tqdm(repo_names):
            url = os.path.join(self.base_url, "repos/{}/{}/branches".format(self.username, repo_name))
            status, data = get_data_from_url(url, self.headers)
            if status == 200:
                self.branch_repo[repo_name] = data
        return self.branch_repo

    # get the bytes count of each language used in a repo
    def get_language_repo(self) -> dict:
        if self.language_repo:
            return self.language_repo
        self.get_all_repo()
        repo_names = [repo["name"] for repo in self.repos]
        for repo_name in tqdm(repo_names):
            url = os.path.join(self.base_url, "repos/{}/{}/languages".format(self.username, repo_name))
            status, data = get_data_from_url(url, self.headers)
            if status == 200:
                self.language_repo[repo_name] = data
        return self.language_repo
    
    # get bytes count of each language in all repos
    def get_language_count(self) -> dict:
        if self.language_count:
            return self.language_count
        self.get_language_repo()
        total_language_dict = {}
        for repo, language_dict in tqdm(self.language_repo.items()):
            for language, byte_number in language_dict.items():
                if language not in total_language_dict:
                    total_language_dict[language] = byte_number
                else:
                    total_language_dict[language] += byte_number
        self.language_count = total_language_dict
        return total_language_dict
    
    # get percentage of each language (by bytes count) in all repos
    def get_language_percentage(self) -> dict:
        if self.language_percentage:
            return self.language_percentage
        self.get_language_count()
        total_bytes = sum(self.language_count.values())
        if not total_bytes:
            return {}
        for language, count in tqdm(self.language_count.items()):
            self.language_percentage[language] = round(count / total_bytes * 100, 2) 
        return self.language_percentage