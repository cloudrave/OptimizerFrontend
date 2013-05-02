from fabric.api import env, cd, require, local, sudo, put
from fabric.contrib.project import rsync_project

LOCAL_DIR = './'
CODE_ROOT = '/var/www/optimizer'
PROJ_FOLDER = 'optimizer'

def production(user):
    '''
    set the environment for production server
    '''
    env.environment = 'production'
    env.hosts = ['140.247.180.47']
    env.user = user
    env.code_root = CODE_ROOT
    env.doc_root = CODE_ROOT + '/htdocs'

def testing(user):
    '''
    set the environment for testing server
    '''
    return False
    env.environment = 'testing'
    env.hosts = ['140.247.180.47']
    env.user = user
    env.code_root = TEST_CODE_ROOT
    env.doc_root = TEST_CODE_ROOT + '/htdocs'

def create_virtual_env():
    '''
    creates virtual environment
    '''
    with cd(env.code_root):
        sudo('virtualenv env')
        env_run('easy_install -U distribute')

def env_run(cmd):
    '''
    runs a command using virtualenv env
    '''
    sudo('source %s/env/bin/activate && %s' % (env.code_root, cmd))

def update_requirements():
    '''
    updates virtual environmnet with requirements
    '''
    with cd(env.code_root):
        env_run('pip install -r requirements.txt')

def bootstrap():
    '''
    bootstrap the server with virtualenv and proper pip installations
    according to requirements.txt
    '''
    create_virtual_env()
    update_requirements()

def sync():
    '''
    use rsync_project to sync files between local and server
    '''
    require('code_root', provided_by=('production'))

    rsync_project(env.code_root, LOCAL_DIR, delete=False, extra_opts="", exclude=('*.pyc', '*.git', '*.gitignore', 'local_settings.py', 'wsgi.py', '/env', PROJ_FOLDER + '/build'))

def touch():
    '''
    touch wsgi file to trigger site reload
    '''
    with cd(env.code_root):
        sudo('touch %s/wsgi.py' % PROJ_FOLDER)

def manage(cmd):
    '''
    helper for manage.py
    '''
    env_run('python %s/%s/manage.py %s' % (env.code_root, PROJ_FOLDER, cmd))

def syncdb():
    '''
    python manage.py syncdb
    '''
    manage('syncdb')

def migrate():
    '''
    use South to migrate
    '''
    manage('migrate')

def collect_static():
    manage('collectstatic')

def restart_server():
    sudo('apachectl restart')

def set_perms():
    sudo('chmod 777 %s; chmod -R 777 %s/%s/media' % (env.code_root, env.code_root, PROJ_FOLDER))

def deploy():
    sync()
    update_requirements()
    syncdb()
    migrate()
    collect_static()
    set_perms()
    restart_server()
