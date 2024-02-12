#!/bin/bash

# Check if Allure CLI is already installed
if ! command -v allure &> /dev/null
then
    echo "Allure CLI could not be found. Attempting to install..."
    # Attempt to install Allure CLI globally using npm
    npm install -g allure-commandline || { echo 'Failed to install Allure CLI. Please install it manually.'; exit 1; }
else
    echo "Allure CLI is already installed."
fi

# Function to initialize and activate virtual environment
create_and_activate_venv() {
    # Create virtual environment
    $1 -m venv venv
    echo "Virtual environment created."

    # Activate virtual environment
    source venv/bin/activate
    echo "Virtual environment activated."
}

# Check for Python3 or Python and create virtual environment
if command -v python3 &>/dev/null; then
    echo "Using python3 to create virtual environment."
    create_and_activate_venv python3
elif command -v python &>/dev/null; then
    echo "Using python to create virtual environment."
    create_and_activate_venv python
else
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Install requirements
echo "Installing requirements from requirements.txt..."
pip install -r requirements.txt
echo "Requirements installed."

echo "Setup completed successfully."
