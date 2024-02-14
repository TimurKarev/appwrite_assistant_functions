import os
from .some import print_some

def main(context):
    context.error("Main ")
    print_some(context)
    # print_error(context)
