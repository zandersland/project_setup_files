# project_setup_files

A repo for storing different setup files

## Running the script

 `python3 project_setup.py -h`

## Adding new projects

* Add a new parser argument under the others (we will be using the base python option as an example):

```python
parser.add_argument('-p','--python',action='store_true',help='Creates basic python files and folder structure'
```

* Change the action to `'store'` if you need a variable passed in
* Add a new `if` statement under the others:

``` python
if args.react:
    print('Basic python')
    file_list.append(('setup.py', ''))
```

* Thats it!
