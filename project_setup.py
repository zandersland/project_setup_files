import os
import datetime


# User inputs
print("\n\n+++++++++++++++ Enter y or n for the following questions +++++++++++++++\n")

inputYN_basic_folder_structure = input("Create basic folder structure?: ").lower()
# Allow for user to verify pwd
if inputYN_basic_folder_structure == "y":
    check_1 = input("Are you in the right folder? (All folders and files are created from \"./\"): ").lower()
    if check_1 == "y":
        pass
    else:
        print("Answered: ({}).   Exiting...".format(check_1))
        exit(1)



def log(_event):
    cur_datetime = datetime.datetime.now()
    print("\nLOG ITEM AT " + str(cur_datetime) + ": " + _event + "\n")


def gitignore_creation():
    gitignore_text = "# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# C extensions\n*.so\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\npip-wheel-metadata/\nshare/python-wheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# PyInstaller\n#  Usually these files are written by a python script from a template\n#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.nox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n*.py,cover\n.hypothesis/\n.pytest_cache/\n\n# Translations\n*.mo\n*.pot\n\n# Django stuff:\n*.log\nlocal_settings.py\ndb.sqlite3\ndb.sqlite3-journal\n\n# Flask stuff:\ninstance/\n.webassets-cache\n\n# Scrapy stuff:\n.scrapy\n\n# Sphinx documentation\ndocs/_build/\n\n# PyBuilder\ntarget/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# IPython\nprofile_default/\nipython_config.py\n\n# pyenv\n.python-version\n\n# pipenv\n#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n#   install all needed dependencies.\n#Pipfile.lock\n\n# PEP 582; used by e.g. github.com/David-OConnor/pyflow\n__pypackages__/\n\n# Celery stuff\ncelerybeat-schedule\ncelerybeat.pid\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# Spyder project settings\n.spyderproject\n.spyproject\n\n# Rope project settings\n.ropeproject\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n.dmypy.json\ndmypy.json\n\n# Pyre type checker\n.pyre/\nnode_modules\n\ndocker/data/\n\n"
    if not os.path.isfile("./.gitignore"):
        with open("./.gitignore", "w") as _gitignore:
            _gitignore.write(gitignore_text)


def basic_folder_structure():
    # TODO print message saying make sure your in the folder to create these folders
    mkdir_list = ["docker", ".vscode", "scripts", "data", "models",
                  "client", "configs", "docs", "tests", "src", "archive", "temp"]
    touch_list = ["config.cfg", "requirements.txt", ".vscode/settings.json"]


    log("Creating .gitignore")
    gitignore_creation()

    log("Creating folders")
    for dir_item in mkdir_list:
        if not os.path.isdir("./{}".format(dir_item)):
            os.system("mkdir ./{}".format(dir_item))
    for file_item in touch_list:
        if not os.path.isfile("./{}".format(file_item)):
            os.system("touch ./{}".format(file_item))


def main_func():
    if inputYN_basic_folder_structure == "y":
        basic_folder_structure()


if __name__ == "__main__":
    main_func()
    log("...Script done")
