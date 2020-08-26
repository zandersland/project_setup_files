#!./venv/bin/python3
import os
import shutil
import datetime
import argparse
import sys
import logging
import subprocess

# * ==============================================================================

# Program variables
directory_list = []
command_list = []
venv_path = 'venv/bin'
gitignore_text = ''
requirements_txt_text = ''
file_list = []
docker_compose_text = ''

# * ==============================================================================

if '-sD' in sys.argv:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s', datefmt="%H:%M:%S (UTC %z)")
else:
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(message)s', datefmt="%H:%M:%S (UTC %z)")


def create_folder(_folder_name: str, _args_script_debug=False):
    """Create a folder

    Args:
        _folder_name (str): Name of folder to create
        _args_script_debug (bool, optional): A paramater for the -sD option. Defaults to False.
    """
    logging.debug(f'Creating folder ({_folder_name})')
    # If the -sD option was not set, create folder without showing output or errors
    if not _args_script_debug:
        subprocess.run(f"mkdir {_folder_name}", shell=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif _args_script_debug:
        subprocess.run(f"mkdir {_folder_name}", shell=True)


def create_file(_file_name: str, _file_content: str):
    """Create a file

    Args:
        _file_name (str): Name of file to create
        _file_content (str): What to put in the file
    """
    logging.debug(f'Creating file ({_file_name})')
    with open(_file_name, 'w') as f:
        f.write(_file_content)


def execute_command(_cmd: str, _args_script_debug=False):
    """Execute a bash command

    Args:
        _cmd (str): The command to execute
        _args_script_debug (bool, optional): A parameter for the -sD option. Defaults to False.
    """
    logging.debug(f'Running command ({_cmd})')
    # If the -sD option was not set, execute command without showing output or errors
    if not _args_script_debug:
        subprocess.run(_cmd, shell=True, stdout=subprocess.DEVNULL)
    elif _args_script_debug:
        subprocess.run(_cmd, shell=True)


# * ==============================================================================


if __name__ == "__main__":
    logging.info("Script starting...")

    # * ==========================================================================

    # Create parser
    parser = argparse.ArgumentParser(
        prog='simple_project_setup',
        description='Setup a project environment from a template',
        allow_abbrev=False
    )
    # Optional arguments
    # TODO Add Docker options
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
    parser.add_argument('-sW',
                        '--script_windows',
                        action='store_true',
                        help='Will open terminal windows and vscode where applicable'
                        )
    parser.add_argument('-sD',
                        '--script_debug',
                        action='store_true',
                        help='Prints more lines out'
                        )
    parser.add_argument('-b',
                        '--basic',
                        action='store_true',
                        help='Creates basic folder and file structure'
                        )
    parser.add_argument('-d',
                        '--docker',
                        action='store_true',
                        help='Will create a docker-compose.yml file. This option is needed for any docker environments'
                        )
    parser.add_argument('-dP',
                        '--docker_postgres',
                        action='store_true',
                        help='Adds Postgres configs to docker-compose.yml'
                        )
    # Parse arguments
    args = parser.parse_args()

    # print(vars(args))

    # * ==============================================================================

    print('\nThese arguments were set:')

    # Logic for going through each argument
    if args.react:
        print('React')
        # Run create-react-app with a name specified in the arguments
        command_list.append(f"npx create-react-app {args.react}")
        if args.script_windows:
            # Start the React app in another window
            command_list.append(
                f'gnome-terminal -- /bin/bash -c "cd ./{args.react} && npm start"')
    if args.basic:
        print('Basic folder structure')
        # Add folders to be created
        directory_list.append('./.vscode')
        directory_list.append('./scripts')
        directory_list.append('./configs')
        directory_list.append('./docs')
        directory_list.append('./archive')
        directory_list.append('./temp')
        # Add a file to be created
        file_list.append(('./.vscode/settings.json', '{\n    \n}'))
    if args.python:
        print('Basic python')
        # Add text to ./.gitignore
        gitignore_text += "\n# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# C extensions\n*.so\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\npip-wheel-metadata/\nshare/python-wheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# PyInstaller\n#  Usually these files are written by a python script from a template\n#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.nox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n*.py,cover\n.hypothesis/\n.pytest_cache/\n\n# Translations\n*.mo\n*.pot\n\n# Django stuff:\n*.log\nlocal_settings.py\ndb.sqlite3\ndb.sqlite3-journal\n\n# Flask stuff:\ninstance/\n.webassets-cache\n\n# Scrapy stuff:\n.scrapy\n\n# Sphinx documentation\ndocs/_build/\n\n# PyBuilder\ntarget/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# IPython\nprofile_default/\nipython_config.py\n\n# pyenv\n.python-version\n\n# pipenv\n#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n#   install all needed dependencies.\n#Pipfile.lock\n\n# PEP 582; used by e.g. github.com/David-OConnor/pyflow\n__pypackages__/\n\n# Celery stuff\ncelerybeat-schedule\ncelerybeat.pid\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# Spyder project settings\n.spyderproject\n.spyproject\n\n# Rope project settings\n.ropeproject\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/\n.dmypy.json\ndmypy.json\n\n# Pyre type checker\n.pyre/\nnode_modules\n\ndocker/data/\n\n"
        # Add a file to be created
        file_list.append(('./setup.py', ''))
    if args.venv:
        # Create requirements.txt if it doesn't exist so that the `pip3 install -r requirements.txt` doesn't blow up
        if not os.path.exists('requirements.txt'):
            file_list.append(('requirements.txt', ''))
        # If theres an existing venv, remove it
        if os.path.exists('venv'):
            command_list.append("rm -rf venv")
        # Create venv
        command_list.append("virtualenv -p python3 venv")
        # Install items from requirements.txt into the venv
        command_list.append(
            f"./{venv_path}/pip3 install -r requirements.txt")
        # List python version
        command_list.append(
            f"./{venv_path}/python --version")
        # List items installed in the venv pip3
        command_list.append(f"./{venv_path}/pip3 list")
    if args.api:
        print('Python api')
        # Add text to ./requirements.txt
        requirements_txt_text += '\nclick==7.1.2\nFlask==1.1.2\nitsdangerous==1.1.0\nJinja2==2.11.2\nMarkupSafe==1.1.1\nWerkzeug==1.0.1\n'
        # Add folders to be created
        directory_list.append('./templates')
        directory_list.append('./static')
        # Add files to be created
        file_list.append(('./app.py', "from flask import Flask, render_template\napp = Flask(__name__)\napp.secret_key = b\'CHANGEME!!!!!!!!!!!!\'\n@app.route(\'/\')\ndef index():\n    return render_template(\'index.html\')\nif __name__ == \"__main__\":\n    app.debug = True\n    app.run(host=\'0.0.0.0\', port=5000, threaded=True)\n"))
        file_list.append(('./templates/index.html', '<!DOCTYPE html>\n<html lang="en">\n    <head>\n        <title>App</title>\n        <link rel="stylesheet" href="static/main.css">\n        <link rel="shortcut icon" href="static/favicon.ico" type="image/x-icon">\n    </head>\n    <body>\n        <h1 style="text-align: center;">Welcome to my app!</h1>\n    </body>\n</html>\n'))
        file_list.append(
            ('./static/main.css', "* {\n    margin: 0;\n}\n"))
        # if -sW was set, open a terminal running the api python file
        if args.script_windows:
            command_list.append(
                "gnome-terminal -- /bin/bash -c \"sudo ./venv/bin/python3 ./app.py\"")
            command_list.append('xdg-open http://localhost:5000')
    if args.script_windows:
        print('script_windows')
    if args.script_debug:
        print('script_debug')
    if args.docker:
        print('docker')
        docker_compose_text += 'version: \'3.3\'\nservices:\n  postgres:'
        if args.docker_postgres:
            print('    docker_postgres')
            docker_compose_text += '\n    image: "postgres"\n    ports:\n      - 5432:5432\n    restart: always\n    environment: \n      POSTGRES_USER: "admin"\n      POSTGRES_PASSWORD: "admin"\n      POSTGRES_DB: admin\n    volumes: \n      - ./data/postgres:/var/lib/postgresql/data\n'
        if args.script_windows and args.script_debug:
            # if -sW and -sD was set, open a text editor to edit the docker-compose.yml before starting it
            command_list.append("nano ./docker-compose.yml")
            command_list.append(
                "gnome-terminal -- /bin/bash -c \"docker-compose up\"")

    print('')

    # * ==========================================================================

    # Creating files, folders, and executing commands

    if directory_list:
        logging.info('Creating folders')
        for _folder in directory_list:
            create_folder(_folder, _args_script_debug=args.script_debug)
    if file_list:
        logging.info('Creating files')
        for _file in file_list:
            create_file(_file[0], _file[1])
    if requirements_txt_text is not '':
        logging.info('Creating ./requirements.txt')
        with open('./requirements.txt', 'a') as f:
            f.write(requirements_txt_text)
    if gitignore_text is not '':
        logging.info('Creating ./.gitignore')
        with open('./.gitignore', 'a') as f:
            f.write(gitignore_text)
    if docker_compose_text is not '':
        logging.info('Creating ./docker-compose.yml')
        with open('./docker-compose.yml', 'a') as f:
            f.write(docker_compose_text)
    if command_list:
        logging.info('Executing commands')
        for _cmd in command_list:
            execute_command(_cmd, _args_script_debug=args.script_debug)

    # * ======================================================================

    if args.script_windows:
        if args.script_debug:
            subprocess.run('git add ./* .vscode .gitignore')
            subprocess.run(
                'git commit -m "Initial project setup\n- (This was run by project_setup.py)"')
            subprocess.run('git push')
        subprocess.run('code -n .', shell=True)

    logging.info("...Script completed")
