#!/bin/bash

# Server SSH connection details
HOST="your_server_ip"
USER="your_ssh_username"
PRIVATE_KEY="/path/to/your/private/key"

# Deployment directory and Git repository details
DEPLOY_DIR="/path/to/deployment/directory"
GIT_REPO="git@github.com:user/repo.git"
GIT_BRANCH="master"

# Function to take backup of previous code
backup_previous_code() {
    echo "Backing up previous code..."
    timestamp=$(date +"%Y%m%d%H%M%S")
    backup_dir="$DEPLOY_DIR/backup_$timestamp"
    mkdir -p "$backup_dir"
    cp -r "$DEPLOY_DIR"/* "$backup_dir"
    echo "Backup completed successfully!"
}

# Function to clone from Git repository
clone_from_git() {
    echo "Cloning $GIT_BRANCH branch from Git..."
    cd "$DEPLOY_DIR" || exit
    git clone -b "$GIT_BRANCH" "$GIT_REPO" .
    echo "Git clone completed successfully!"
}

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    cd "$DEPLOY_DIR" || exit
    bundle install --without development test
    npm install
    echo "Dependency installation completed successfully!"
}

# SSH to the server and execute deployment steps
echo "Starting deployment..."
ssh -i "$PRIVATE_KEY" "$USER"@"$HOST" "$(typeset -f backup_previous_code); backup_previous_code"
ssh -i "$PRIVATE_KEY" "$USER"@"$HOST" "$(typeset -f clone_from_git); clone_from_git"
ssh -i "$PRIVATE_KEY" "$USER"@"$HOST" "$(typeset -f install_dependencies); install_dependencies"
echo "Deployment completed successfully!"
