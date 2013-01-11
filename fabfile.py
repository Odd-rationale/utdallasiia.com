from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['utdallasiia@utdallasiia.webfactional.com']
env.directory = '/home/utdallasiia/webapps/utdallasiia_site/utdallasiia'
env.activate = 'source /home/utdallasiia/env/utdallasiia/bin/activate'

def prepare_deploy():
    local("git add . && git commit")
    local("git push origin master")

def deploy():
    with cd(env.directory):
        with prefix(env.activate):
            run("git pull")
            run("python manage.py collectstatic")
            run("~/bin/utdallasiia_site_admin restart")