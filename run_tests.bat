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

REM Run pytest and collect Allure results
pytest tests/ --alluredir=%results_dir%

REM Generate the Allure report in a specific directory
npx allure-commandline generate %results_dir% -o %report_dir% --clean

echo Allure report generated in %report_dir%
