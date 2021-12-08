set this_dir=%~dp0

pushd "%this_dir%"
call ".venv\Scripts\activate.bat"
python "screen_text_snip.py" %*
call ".venv\Scripts\deactivate.bat"
popd