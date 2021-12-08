set this_dir=%~dp0

pushd "%this_dir%"
rem call ".venv\Scripts\activate.bat"
python screen_text_snip.py %*
rem call ".venv\Scripts\deactivate.bat"
popd