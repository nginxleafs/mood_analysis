install:
    python -m pip install -r requirements.txt

gui:
    python "$(find . -name "app.py" -not -path './.venv/*')" 

term:
    python "$(find . -name "main.py" -not -path './.venv/*' )"

build:
    python -m pip install pyinstaller
    pyinstaller --onefile "$(find . -name "app.py" -not -path './.venv/*' )" --name moodanalysis-gui
    pyinstaller --onefile "$(find . -name "main.py" -not -path './.venv/*' )" --name moodanalysis
    cp -r "$(find . -name moodanalysis-gui -not -path './.venv/*' )" ~/.local/bin/
    cp -r "$(find . -name moodanalysis -not -path './.venv/*' )" ~/.local/bin/

run: install gui
run-term: install term
