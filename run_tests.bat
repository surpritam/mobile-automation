@echo off

REM Set directories for Allure results and reports
set results_dir=allure-results
set report_dir=allure-report

REM Clean up the previous Allure results
if exist %results_dir% rmdir /s /q %results_dir%
if exist %report_dir% rmdir /s /q %report_dir%

REM Create a new, empty Allure results directory
mkdir %results_dir%
mkdir %report_dir%

REM Check if no argument is provided
if "%~1"=="" (
    echo Running all tests...
    set TEST_COMMAND=tests/
) else (
    REM Check if the first argument indicates a marker
    echo Argument 1: %1
    if "%1"=="-m" (
        echo Running tests with marker: %2
        set TEST_COMMAND=tests/ %1 %2
    ) else (
        echo Running specific test suite: %1
        set TEST_COMMAND=tests/%1
    )
)

REM Execute pytest with the constructed command
pytest %TEST_COMMAND% --alluredir=%results_dir%

REM Generate the Allure report in a specific directory
npx allure-commandline generate %results_dir% -o %report_dir% --clean

echo Allure report generated in %report_dir%
