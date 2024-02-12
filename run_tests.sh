#!/bin/bash

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

# Set directories for Allure results and reports
results_dir="allure-results"
report_dir="allure-report"

# Clean up the previous Allure results
rm -rf "$results_dir"
rm -rf "$report_dir"

# Create new, empty Allure results and reports directories
mkdir "$results_dir"
mkdir "$report_dir"

# Check if no argument is provided
if [ -z "$1" ]; then
    echo "Running all tests..."
    TEST_COMMAND="tests/"
else
    # Check if the first argument indicates a marker
    echo "Argument 1: $1"
    if [ "$1" == "-m" ]; then
        echo "Running tests with marker: $2"
        TEST_COMMAND="tests/ $1 $2"
    else
        echo "Running specific test suite: $1"
        TEST_COMMAND="tests/$1"
    fi
fi

# Execute pytest with the constructed command
pytest $TEST_COMMAND --alluredir=$results_dir

# Generate the Allure report in a specific directory
npx allure-commandline generate $results_dir -o $report_dir --clean
echo "Allure report generated in $report_dir"

# Automatically open the Allure report
echo "Opening Allure report..."
npx allure-commandline open $report_dir
