from appwrite.client import Client
import os


# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    TIM_TWITTER_API_KEY = context.res.send(os.environ['TIM_TWITTER_API_KEY'])
    TIM_TWITTER_API_SECRET = context.res.send(os.environ['TIM_TWITTER_API_SECRET'])
    TIM_TWITTER_ACCESS_TOKEN = context.res.send(os.environ['TIM_TWITTER_ACCESS_TOKEN'])
    TIM_TWITTER_ACCESS_TOKEN_SECRET = context.res.send(os.environ['TIM_TWITTER_ACCESS_TOKEN_SECRET'])
    TIM_BEARER_TOKEN = context.res.send(os.environ['TIM_BEARER_TOKEN'])


    # You can log messages to the console
    context.log('TIM_TWITTER_API_KEY')

    # If something goes wrong, log an error
    context.error("Hello, Errors!")

    # The `ctx.req` object contains the request data
    if context.req.method == "GET":
        # Send a response with the res object helpers
        # `ctx.res.send()` dispatches a string back to the client
        return context.res.send("Hello, World!")

    # `ctx.res.json()` is a handy helper for sending JSON
    return context.res.json(
        {
            "motto": "Build like a team of hundreds_",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )
