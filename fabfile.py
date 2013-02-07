from os import path
from pepa.conf.environments import env

env.platform = 'php'
env.project = ''


# You can specify environments here
# def testing():
#     env.name = 'testing'
#     env.url = 'site-dev.testing.com'
#     env.hosts = env.roledefs['testing']
#     env.path = path.join(env.web_root, env.url)
#     env.database = 'site_test'
#     env.require_password = True


def staging():
    env.name = 'staging'
    env.url = 'mikekierstead.com'
    env.hosts = ['rackdev.erskinedev.com:22']
    env.path = path.join(env.web_root, env.url)
    env.database = 'mikekierstead'
    env.require_password = False


# def production():
#     env.name = 'production'
#     env.url = 'site.com'
#     env.hosts = env.roledefs['production']
#     env.path = path.join(env.web_root, env.url)
#     env.database = 'site'
#     env.require_password = False


# Do not edit below this line
from pepa import *
