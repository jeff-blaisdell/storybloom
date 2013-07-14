from fabric.api import local

def deploy():
    local("git add -p")
    local("git commit")
    local("git push")