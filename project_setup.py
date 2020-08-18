#!./venv/bin/python3
import os
import shutil
import datetime
import argparse
import sys

# * ==============================================================================

# Program variables
directory_list = [".vscode", "scripts",
                  "configs", "docs", "archive", "temp"]
command_list = []
venv_path = 'venv/bin'
gitignore_text = ''
requirements_txt_text = ''
file_list = [(".vscode/settings.json", '{\n    \n}')]

# * ==============================================================================

# This is the log function for reporting stuff to the console


def log(_event):
    cur_datetime = datetime.datetime.now()
    print("\nINFO AT " + str(cur_datetime) + ": " + _event + "\n")


# These 3 are the create functions

def create_folder(_folder_name):
    log(f'Creating folder ({_folder_name})')
    os.system(f"mkdir {_folder_name}")


def create_file(_file_name, _file_content):
    log(f'Creating file ({_file_name})')
    with open(_file_name, 'w') as f:
        f.write(_file_content)


def execute_command(_cmd):
    log(f'Running command ({_cmd})')
    os.system(_cmd)


# * ==============================================================================


if __name__ == "__main__":
    log("Script starting...")

    # * ==========================================================================

    # Create parser
    parser = argparse.ArgumentParser(
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
    parser.add_argument('-pA',
                        '--api',
                        action='store_true',
                        help='Creates python api files and folder structure'
                        )
    parser.add_argument('-pV',
                        '--venv',
                        action='store_true',
                        help='Creates a python venv'
                        )
    parser.add_argument('-r',
                        '--react',
                        action='store',
                        help='Creates a React environment with name as input'
                        )
    parser.add_argument('-w',
                        '--windows',
                        action='store_true',
                        help='Will open terminal windows and vscode where applicable'
                        )
    # Parse arguments
    args = parser.parse_args()

    print(vars(args))

    # * ==============================================================================

    # Logic for going through each argument
    if args.python:
        print('Basic python')
        gitignore_text += "\n# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# C extensions\n*.so\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\npip-wheel-metadata/\nshare/python-wheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# PyInstaller\n#  Usually these files are written by a python script from a template\n#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.nox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n*.py,cover\n.hypothesis/\n.pytest_cache/\n\n# Translations\n*.mo\n*.pot\n\n# Django stuff:\n*.log\nlocal_settings.py\ndb.sqlite3\ndb.sqlite3-journal\n\n# Flask stuff:\ninstance/\n.webassets-cache\n\n# Scrapy stuff:\n.scrapy\n\n# Sphinx documentation\ndocs/_build/\n\n# PyBuilder\ntarget/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# IPython\nprofile_default/\nipython_config.py\n\n# pyenv\n.python-version\n\n# pipenv\n#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n#   install all needed dependencies.\n#Pipfile.lock\n\n# PEP 582; used by e.g. github.com/David-OConnor/pyflow\n__pypackages__/\n\n# Celery stuff\ncelerybeat-schedule\ncelerybeat.pid\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# Spyder project settings\n.spyderproject\n.spyproject\n\n# Rope project settings\n.ropeproject\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n.dmypy.json\ndmypy.json\n\n# Pyre type checker\n.pyre/\nnode_modules\n\ndocker/data/\n\n"
        file_list.append(('setup.py', ''))
    if args.venv:
        if os.path.exists('venv'):
            command_list.append("rm -rf venv")
        command_list.append("virtualenv -p python3 venv")
        command_list.append(
            f"./{venv_path}/pip3 install -r requirements.txt")
        command_list.append(
            f"./{venv_path}/python --version")
        command_list.append(f"./{venv_path}/pip3 list")
    if args.api:
        print('Python api')
        requirements_txt_text += '\nclick==7.1.2\nFlask==1.1.2\nitsdangerous==1.1.0\nJinja2==2.11.2\nMarkupSafe==1.1.1\nWerkzeug==1.0.1\n'
        directory_list.append('templates')
        directory_list.append('static')
        file_list.append(('./app.py', "from flask import Flask, render_template\napp = Flask(__name__)\napp.secret_key = b\'CHANGEME!!!!!!!!!!!!\'\n@app.route(\'/\')\ndef index():\n    return render_template(\'index.html\')\nif __name__ == \"__main__\":\n    app.debug = True\n    app.run(host=\'0.0.0.0\', port=5000, threaded=True)\n"))
        file_list.append(('./templates/index.html', '<!DOCTYPE html>\n<html lang="en">\n    <head>\n        <title>App</title>\n        <link rel="stylesheet" href="static/main.css">\n        <link rel="shortcut icon" href="static/favicon.ico" type="image/x-icon">\n    </head>\n    <body>\n        <h1 style="text-align: center;">Welcome to my app!</h1>\n    </body>\n</html>\n'))
        file_list.append(
            ('./static/main.css', "* {\n    margin: 0;\n}\n"))
        if args.windows:
            command_list.append(
                "gnome-terminal -- sudo ./venv/bin/python3 ./app.py")
    if args.react:
        print('React')
        command_list.append(f"npx create-react-app {args.react}")
        if args.windows:
            command_list.append(
                f'gnome-terminal -- /bin/bash -c "cd ./{args.react} && npm start"')

    # * ==========================================================================

    # Creating files, folders, and executing commands
    log('Creating folders')
    for _folder in directory_list:
        create_folder(_folder)
    log('Creating files')
    for _file in file_list:
        create_file(_file[0], _file[1])
    if requirements_txt_text is not '':
        log('Creating ./requirements.txt')
        with open('./requirements.txt', 'a') as f:
            f.write(requirements_txt_text)
    if gitignore_text is not '':
        log('Creating ./.gitignore')
        with open('./.gitignore', 'a') as f:
            f.write(gitignore_text)
    log('Executing commands')
    for _cmd in command_list:
        execute_command(_cmd)

    # * ======================================================================

    if args.windows:
        os.system('code -n .')

    log("...Script completed")
