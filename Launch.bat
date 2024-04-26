@echo off

if not defined PYTHON (set PYTHON=python)
if not defined VENV_DIR (set "VENV_DIR=%~dp0%venv")

set SD_WEBUI_RESTART=tmp/restart
set ERROR_REPORTING=FALSE

mkdir tmp 2>NUL

%PYTHON% -c "" >tmp/stdout.txt 2>tmp/stderr.txt
if %ERRORLEVEL% == 0 goto :check_pip
echo Couldn't launch python
goto :show_stdout_stderr

:check_pip
%PYTHON% -mpip --help >tmp/stdout.txt 2>tmp/stderr.txt
if %ERRORLEVEL% == 0 goto :check_venv
echo Couldn't install pip
goto :show_stdout_stderr

:check_venv
if exist %VENV_DIR% (goto :activate_venv)
PYTHON -m venv venv
goto :activate_venv

:activate_venv
cd %VENV_DIR%/Scripts
call activate.bat
pip install -r %~dp0%requirements.txt
set PYTHON="%VENV_DIR%\Scripts\Pythonw.exe"
%PYTHON% %~dp0%/UI/blenderLauncher.py
goto:end

:show_stdout_stderr

echo.
echo exit code: %errorlevel%

for /f %%i in ("tmp\stdout.txt") do set size=%%~zi
if %size% equ 0 goto :show_stderr
echo.
echo stdout:
type tmp\stdout.txt

:show_stderr
for /f %%i in ("tmp\stderr.txt") do set size=%%~zi
if %size% equ 0 goto :show_stderr
echo.
echo stderr:
type tmp\stderr.txt
pause

:end
pause