from fabric import Connection, task
from fabric.exceptions import CommandError
import os
from datetime import datetime

# Define your server's SSH connection details
HOST = 'your_server_ip'
USER = 'your_ssh_username'
PRIVATE_KEY = '/path/to/your/private/key'  # Path to your private key file

# Define your deployment directory and Git repository details
DEPLOY_DIR = '/path/to/deployment/directory'
GIT_REPO = 'git@github.com:user/repo.git'
GIT_BRANCH = 'master'  # Change to the branch you want to deploy

# Fabric connection object
conn = Connection(host=HOST, user=USER, connect_kwargs={'key_filename': PRIVATE_KEY})


@task
def deploy():
    print("Starting deployment...")
    backup_previous_code()
    clone_from_git()
    install_dependencies()
    print("Deployment completed successfully!")


def backup_previous_code():
    print("Backing up previous code...")
    try:
        # Create a timestamped directory for backup
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_dir = os.path.join(DEPLOY_DIR, f'backup_{timestamp}')
        conn.run(f'mkdir -p {backup_dir}')

        # Copy existing code to backup directory
        conn.run(f'cp -r {DEPLOY_DIR}/* {backup_dir}')

        print("Backup completed successfully!")
    except CommandError as e:
        print(f"Backup failed: {e}")


def clone_from_git():
    print(f"Cloning {GIT_BRANCH} branch from Git...")
    try:
        # Clone the specified branch from Git repository using SSH URL
        conn.run(f'cd {DEPLOY_DIR} && git clone -b {GIT_BRANCH} {GIT_REPO} .')

        print("Git clone completed successfully!")
    except CommandError as e:
        print(f"Git clone failed: {e}")


def install_dependencies():
    print("Installing dependencies...")
    try:
        # Change directory to the Rails app directory
        conn.run(f'cd {DEPLOY_DIR}')

        # Install Ruby dependencies with bundle
        conn.run(f'cd {DEPLOY_DIR} && bundle install --without development test')

        # Install Node.js dependencies with npm
        conn.run(f'cd {DEPLOY_DIR} && npm install')

        print("Dependency installation completed successfully!")
    except CommandError as e:
        print(f"Dependency installation failed: {e}")
