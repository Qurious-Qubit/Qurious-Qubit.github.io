@echo off
echo ==============================================
echo Extracting all physics study materials...
echo ==============================================

set "SEVENZIP=C:\Program Files\7-Zip\7z.exe"
if not exist "%SEVENZIP%" (
    where 7z >nul 2>&1
    if %ERRORLEVEL% equ 0 (
        set "SEVENZIP=7z"
    ) else (
        echo Error: 7-Zip is not installed or not in PATH.
        echo Please install 7-Zip from https://www.7-zip.org/
        pause
        exit /b 1
    )
)

for /d %%D in (*) do (
    if exist "%%D\%%~nxD.7z.001" (
        echo [Extracting] %%D...
        "%SEVENZIP%" x -y -o"%%D" "%%D\%%~nxD.7z.001"
    ) else if exist "%%D\%%~nxD.7z" (
        echo [Extracting] %%D...
        "%SEVENZIP%" x -y -o"%%D" "%%D\%%~nxD.7z"
    )
)

echo.
echo All archives extracted successfully!
pause
