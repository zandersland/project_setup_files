
# * Printing list of args
# import sys

# if __name__ == "__main__":
#     print(f"Arguments count: {len(sys.argv)}")
#     print(f"Args list: {sys.argv}")
#     for i, arg in enumerate(sys.argv):
#         print(f"Argument {i:>6}: {arg}")


# * Reversing args
# import sys

# try:
#     arg = sys.argv[1]
# except IndexError:
#     raise SystemExit(f"Usage: {sys.argv[0]} <string_to_reverse>")
# print(arg[::-1])


# * Hashing args
# import os
# import sys
# import hashlib

# data = os.fsencode(sys.argv[1])
# m = hashlib.sha1()
# m.update(data)
# print(m.hexdigest())


# * Using logic in reading args
# import sys

# opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
# args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# if "-c" in opts:
#     print(" ".join(arg.capitalize() for arg in args))
# elif "-u" in opts:
#     print(" ".join(arg.upper() for arg in args))
# elif "-l" in opts:
#     print(" ".join(arg.lower() for arg in args))
# else:
#     raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")


# * Trying argparse
import sys
import argparse

# Initialize argparse
my_parser = argparse.ArgumentParser(prog='testing_argparse',
                                    # usage='%(prog)s [options]',
                                    description='Trying argparse',
                                    allow_abbrev=False
                                    )

# Add arguments
# my_parser.add_argument('Print_item',
#                        type=str,
#                        help='Item to print',
#                        action='store'
#                        )

my_parser.add_argument('-p',
                       '--python',
                       help='Sets project type to Python',
                       action='store',
                       nargs=argparse.REMAINDER
                       )

my_parser.add_argument('-r',
                       '--react',
                       help='Sets project type to React',
                       action='store',
                       nargs=argparse.REMAINDER
                       )


# Execute parse_args()
args = my_parser.parse_args()

# input_print_item = args.Print_item
# input_twice_item = args.twice

print(vars(args))
# print(input_print_item)
# if input_twice_item == True:
#     print(input_print_item)
# if args.banana == True:
#     print("BANANA!!!!!")









# ! Not functional, to be used as reference
def args_parser():
    usage_string = f"Usage: {sys.argv[0]} SETUP [-h] (-p, --python | -r, --react) <arguments>...\n" \
        f"Usage: {sys.argv[0]} UNDO <arguments>...\n" \
        f"Usage: {sys.argv[0]} UPDATE <arguments>...\n"

    try:
        first_option = sys.argv[1]
    except IndexError:
        raise SystemExit(usage_string)

    if "SETUP" == first_option:
        print(f"Poping items from sys.argv: {sys.argv.pop(1)}")

        my_parser = argparse.ArgumentParser(prog='testing_argparse',
                                            # usage='%(prog)s [options]',
                                            description='Trying argparse',
                                            allow_abbrev=False
                                            )
        my_parser.add_argument('-p',
                               '--python',
                               help='Sets project type to Python',
                               action='store',
                               nargs=argparse.REMAINDER
                               )
        my_parser.add_argument('-r',
                               '--react',
                               help='Sets project type to React',
                               action='store',
                               nargs=argparse.REMAINDER
                               )
        args = my_parser.parse_args()
        print(vars(args))
    elif "UNDO" == first_option:
        raise NotImplementedError
    elif "UPDATE" == first_option:
        raise NotImplementedError
    else:
        raise SystemExit(usage_string)


# ! Not functional, to be used as reference
def better_args_parser():
    usage_string = f"Usage: {sys.argv[0]} (python | react)"

    parser = argparse.ArgumentParser(prog='project_setup',
                                     description='Setup a project environment from a template',
                                     allow_abbrev=False
                                     )

    subparser = parser.add_subparsers()
    project_template_subparser = subparser.add_parser('project_template')
    project_template_subparser.add_argument('project_options')

    # project_group = parser.add_mutually_exclusive_group(required=True)
    # project_group.add_argument('-p', '--python', action='store_true')
    # project_group.add_argument('-r', '--react', action='store_true')

    args = parser.parse_args()
