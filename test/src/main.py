import os
from .some import print_some
from .shared import print_error

def main(context):
    context.error("Main ")
    print_some(context)
    print_error(context)

    return context.res.empty()