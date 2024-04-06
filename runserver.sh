# Variables
PROJECT_DIR="/c/Users/MrKumar/myproj/sims"
REQUIREMENTS_FILE="/c/Users/MrKumar/myproj/sims/requirements.txt"  # Update this path
VENV_DIR="$PROJECT_DIR/venv"
MANAGE_PY="$PROJECT_DIR/manage.py"

# Function to display error and exit
function display_error {
    echo "Error: $1"
    exit 1
}

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    # Create virtual environment
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR" || display_error "Failed to create virtual environment"
fi

# Activate virtual environment (for Git Bash)
source "$VENV_DIR/scripts/activate" || display_error "Failed to activate virtual environment"

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r "$REQUIREMENTS_FILE" || display_error "Failed to install dependencies"

echo "Virtual environment created and dependencies installed successfully!"

# Make migrations
echo "Making migrations..."
python "$MANAGE_PY" makemigrations || display_error "Failed to make migrations"

# Migrate to the database
echo "Migrating to the database..."
python "$MANAGE_PY" migrate || display_error "Failed to migrate to the database"

# Run the server
echo "Running the server..."
python "$MANAGE_PY" runserver || display_error "Failed to run the server"
# Variables
PROJECT_DIR="/sims"
REQUIREMENTS_FILE="/c/Users/MrKumar/myproj/sims/requirements.txt"  # Update this path
VENV_DIR="$PROJECT_DIR/venv"
MANAGE_PY="$PROJECT_DIR/manage.py"

# Function to display error and exit
function display_error {
    echo "Error: $1"
    exit 1
}

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    # Create virtual environment
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR" || display_error "Failed to create virtual environment"
fi

# Activate virtual environment (for Git Bash)
source "$VENV_DIR/scripts/activate" || display_error "Failed to activate virtual environment"

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r "$REQUIREMENTS_FILE" || display_error "Failed to install dependencies"

echo "Virtual environment created and dependencies installed successfully!"

# Make migrations
echo "Making migrations..."
python "$MANAGE_PY" makemigrations || display_error "Failed to make migrations"

# Migrate to the database
echo "Migrating to the database..."
python "$MANAGE_PY" migrate || display_error "Failed to migrate to the database"

# Run the server
echo "Running the server..."
python "$MANAGE_PY" runserver || display_error "Failed to run the server"
