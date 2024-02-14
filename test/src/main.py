import os
from  ai_assistant import test

def main(context):
    context.error(test.get_test())

    return context.res.empt
