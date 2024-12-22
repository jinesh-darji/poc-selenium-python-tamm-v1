from framework.configuration import config
from buy_a_home.configuration import config as project_config

for key, value in project_config.__dict__.items():
    config.__dict__[key] = value