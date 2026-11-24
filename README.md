Moodanalysis - application with that you can analyse your mood during the days, and then you can analyse created .csv file by your own.
Application has both the GUI and terminal mode.

---

Dependencies:
  - ```python just```
  - Arch:  ```sudo pacman -S python just```
  - Debian: ```sudo apt install python just```
  - Fedora: ```sudo dnf install python just```

How to run:
  - Specify path in .env you want your statistics to be saved.
  - Then run ```just run``` inside your venv

Usage case:
  You might want to realize how changes your mood during the days, what affects it, so that application does exactly that, pass questions during one month at least and then analyse resulting .csv data with pandas in python or other tool.


