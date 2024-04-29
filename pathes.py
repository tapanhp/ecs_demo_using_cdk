import os

def get_modules_path()->str:
    return os.path.dirname(__file__)

def get_iam_docker_path()->str:
    return os.path.join(get_modules_path(), 'IAM_docker')