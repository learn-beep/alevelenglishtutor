@echo off
rem Unzips the site source into this folder and the crops into public\img
cd /d "%~dp0"
powershell -NoProfile -Command "Expand-Archive -Force alevelenglishtutor-source.zip ."
for %%f in (alevelenglishtutor-img-*.zip) do powershell -NoProfile -Command "Expand-Archive -Force %%f public"
echo Done.
pause
