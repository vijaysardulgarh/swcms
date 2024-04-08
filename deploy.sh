#!/bin/bash

# Variables
DOMAIN="vijaykumar.fun"
IP="34.131.63.47"
USER="vijaysardulgarh"
PROJECT_NAME="sims"
GITHUB_REPO="https://github.com/vijaysardulgarh/sims.git"
NGINX_CONFIG_DIR="/etc/nginx/sites-available"
NGINX_SITES_ENABLED_DIR="/etc/nginx/sites-enabled"
PROJECT_DIR="/home/$USER/$PROJECT_NAME"
SOCKET_FILE="/run/$PROJECT_NAME.gunicorn.sock"
NGINX_SOCKET_FILE="/etc/systemd/system/$PROJECT_NAME.gunicorn.socket"
NGINX_SERVICE_FILE="/etc/systemd/system/$PROJECT_NAME.gunicorn.service"
GUNICORN_BIN="$PROJECT_DIR/venv/bin/gunicorn"
GUNICORN_WSGI="school.wsgi:application"  # Replace with your project's WSGI module
DATABASE_FILE="$PROJECT_DIR/db.sqlite3"

# Clone or pull project from GitHub
echo "Cloning or pulling project from GitHub"
if [ -d "$PROJECT_DIR" ]; then
    cd $PROJECT_DIR
    git pull origin main
else
    git clone $GITHUB_REPO $PROJECT_DIR
fi


# Check if the database file exists
if [ ! -f "$DATABASE_FILE" ]; then
    echo "Error: Database file '$DATABASE_FILE' not found."
    exit 1
fi

# Change the permissions of the database file
chmod 664 "$DATABASE_FILE"

echo "Permissions of '$DATABASE_FILE' have been changed successfully."



# Create virtual environment
echo "Creating virtual environment"
python3 -m venv $PROJECT_DIR/venv

# Activate virtual environment
source $PROJECT_DIR/venv/bin/activate

# Install project dependencies
echo "Installing project dependencies"
pip install -r $PROJECT_DIR/requirements.txt

# Install Gunicorn
echo "Installing Gunicorn"
pip install gunicorn

# Deactivate virtual environment
deactivate

# Create Nginx socket file
echo "Creating Nginx socket file"
cat << EOF | sudo tee $NGINX_SOCKET_FILE
[Unit]
Description="$PROJECT_NAME.gunicorn socket"

[Socket]
ListenStream=$SOCKET_FILE

[Install]
WantedBy=sockets.target
EOF

# Create Nginx service file
echo "Creating Nginx service file"
cat << EOF | sudo tee $NGINX_SERVICE_FILE
[Unit]
Description=$PROJECT_NAME.gunicorn daemon
Requires=$PROJECT_NAME.gunicorn.socket
After=network.target

[Service]
User=$USER
Group=$USER
WorkingDirectory=$PROJECT_DIR
ExecStart=$GUNICORN_BIN --access-logfile - --workers 3 --bind unix:$SOCKET_FILE $GUNICORN_WSGI

[Install]
WantedBy=multi-user.target
EOF

# Enable and start Gunicorn socket and service
echo "Enabling and starting Gunicorn socket and service"
sudo systemctl enable $PROJECT_NAME.gunicorn.socket
sudo systemctl enable $PROJECT_NAME.gunicorn.service
sudo systemctl start $PROJECT_NAME.gunicorn.socket
sudo systemctl start $PROJECT_NAME.gunicorn.service

# Reload systemd daemon
echo "Reloading systemd daemon"
sudo systemctl daemon-reload


# Remove existing Nginx configuration file if it exists
if [ -f "$NGINX_CONFIG_DIR/$DOMAIN" ]; then
    echo "Removing existing Nginx configuration file"
    sudo rm "$NGINX_CONFIG_DIR/$DOMAIN"
fi

# Create Nginx configuration file
echo "Creating Nginx configuration file"
cat << EOF | sudo tee $NGINX_CONFIG_DIR/$DOMAIN
server {
    listen 80;
    listen [::]:80;
    server_name DOMAIN IP ;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        proxy_set_header Host \$http_host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_pass http://unix:$SOCKET_FILE;
    }

    location /static/ {
        alias $PROJECT_DIR/static/;
    }

    location /media/ {
        alias $PROJECT_DIR/media/;
    }
}
EOF

# Remove existing symbolic link if it exists
if [ -L "$NGINX_SITES_ENABLED_DIR/$DOMAIN" ]; then
    echo "Removing existing symbolic link"
    sudo rm "$NGINX_SITES_ENABLED_DIR/$DOMAIN"
fi

# Enable Nginx site
echo "Enabling Nginx site"
sudo ln -s "$NGINX_CONFIG_DIR/$DOMAIN" "$NGINX_SITES_ENABLED_DIR/$DOMAIN"

# Test Nginx configuration
echo "Testing Nginx configuration"
sudo nginx -t

# Restart Gunicorn
echo "Restarting Gunicorn"
sudo systemctl restart $PROJECT_NAME.gunicorn

# Restart Nginx
echo "Restarting Nginx"
sudo systemctl restart nginx

echo "Deployment completed successfully!"
