from yin_resume_api.orm_mongodb import db

class GithubRepo(db.Document):
    cover_url = db.StringField()
    description = db.StringField()
    main_language = db.StringField()
    title = db.StringField()
    language = db.DictField()
    demo_url = db.StringField()
    meta = {'collection': 'github_repo'}