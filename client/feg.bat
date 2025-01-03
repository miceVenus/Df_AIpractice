@echo off
setlocal

set PARAM=
set CURRENT_DIR=%~dp0

:parse_args
if "%1" == "-h" (
    set PARAM=%PARAM% -h
    goto end_parse
)
if "%1" == "-v" (
    set PARAM=%PARAM% -v
    goto end_parse
)
if "%1" == "--verbose" (
    set PARAM=%PARAM% --verbose
    goto end_parse
)

if "%2" == "" (
    set PARAM=%PARAM% -o %1
    goto end_parse
)

set PARAM=%PARAM% -i %1
shift
goto parse_args

:end_parse

python %CURRENT_DIR%feg.py %PARAM%

endlocal