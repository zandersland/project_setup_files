#!./venv/bin/python3
import os
import shutil
# import subprocess
import datetime
import argparse
import sys


class program_variables():
    directory_list = [".vscode", "scripts", "data", "models",
                    "configs", "docs", "tests", "archive", "temp"]
    file_list = [".vscode/settings.json",
                "docker-compose.yml"]
    command_list = []
    venv_path = 'venv/bin'
    gitignore_text = ''


# * This Class is for all the project templates
class project_templates():
    # TODO Create project templates
    # List of projects:
    # - Python
    # - Python api with flask
    # - React
    # - Python with postgres database in docker
    # - Docker

    def project_python():
        program_variables.gitignore_text += "\n# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# C extensions\n*.so\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\npip-wheel-metadata/\nshare/python-wheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# PyInstaller\n#  Usually these files are written by a python script from a template\n#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.nox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n*.py,cover\n.hypothesis/\n.pytest_cache/\n\n# Translations\n*.mo\n*.pot\n\n# Django stuff:\n*.log\nlocal_settings.py\ndb.sqlite3\ndb.sqlite3-journal\n\n# Flask stuff:\ninstance/\n.webassets-cache\n\n# Scrapy stuff:\n.scrapy\n\n# Sphinx documentation\ndocs/_build/\n\n# PyBuilder\ntarget/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# IPython\nprofile_default/\nipython_config.py\n\n# pyenv\n.python-version\n\n# pipenv\n#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n#   install all needed dependencies.\n#Pipfile.lock\n\n# PEP 582; used by e.g. github.com/David-OConnor/pyflow\n__pypackages__/\n\n# Celery stuff\ncelerybeat-schedule\ncelerybeat.pid\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# Spyder project settings\n.spyderproject\n.spyproject\n\n# Rope project settings\n.ropeproject\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n.dmypy.json\ndmypy.json\n\n# Pyre type checker\n.pyre/\nnode_modules\n\ndocker/data/\n\n"

        # mkdir_list.append()

        program_variables.file_list.append("requirements.txt")
        program_variables.file_list.append("setup.py")


    def project_python_venv():
        if os.path.exists('venv'):
            program_variables.command_list.append("rm -rf venv")
        program_variables.command_list.append("virtualenv -p python3 venv")
        program_variables.command_list.append(
            f"./{program_variables.venv_path}/pip3 install -r requirements.txt")
        program_variables.command_list.append(
            f"./{program_variables.venv_path}/python --version")
        program_variables.command_list.append(f"./{program_variables.venv_path}/pip3 list")



# * This Class is for the create functions
class create_functions():
    def create_folders():
        create_functions.log("Creating folders")
        for dir_item in program_variables.directory_list:
            if not os.path.isdir("./{}".format(dir_item)):
                os.system("mkdir ./{}".format(dir_item))


    def create_files():
        create_functions.log("Creating files")
        for file_item in program_variables.file_list:
            if not os.path.isfile("./{}".format(file_item)):
                os.system("touch ./{}".format(file_item))


    def create_gitignore():
        create_functions.log("Creating .gitignore")
        with open('./.gitignore', 'w') as f:
            f.write(program_variables.gitignore_text)


    def execute_commands():
        create_functions.log("Executing commands")
        for y in program_variables.command_list:
            create_functions.log(f"Running command: ({y})")
            os.system(y)


    def log(_event):
        cur_datetime=datetime.datetime.now()
        print("\nINFO AT " + str(cur_datetime) + ": " + _event + "\n")


# * This function will be for parsing args
def simple_args_parser():
    # Create parser
    parser=argparse.ArgumentParser(
        prog='simple_project_setup',
        description='Setup a project environment from a template',
        allow_abbrev=False
    )

    # Optional arguments
    parser.add_argument('-p',
                        '--python',
                        action='store_true',
                        help='Creates basic python files and folder structure'
                        )

    parser.add_argument('-a',
                        '--api',
                        action='store_true',
                        help='Creates python api files and folder structure'
                        )

    parser.add_argument('-v',
                        '--venv',
                        action='store_true',
                        help='Creates a python venv'
                        )

    parser.add_argument('-r',
                        '--react',
                        action='store_true',
                        help='Creates a React environment'
                        )

    # Parse arguments
    args=parser.parse_args()

    # Logic for going through each argument
    if args.python:
        print('Basic python')
        project_templates.project_python()
    if args.venv:
        print('Python venv')
        project_templates.project_python_venv()
    if args.api:
        print('Python api')
    if args.react:
        print('React environment')


# * This is the function that executes everything
def main():
    simple_args_parser()

    create_functions.create_files()
    create_functions.create_folders()
    create_functions.create_gitignore()
    create_functions.execute_commands()


if __name__ == "__main__":
    create_functions.log("Script starting...")
    # main_func()
    main()
    create_functions.log("...Script completed")
