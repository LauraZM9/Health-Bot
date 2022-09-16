import os
# Use the package we installed
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']

app = App(token=SLACK_BOT_TOKEN)

# Initializes your app with your bot token and signing secret
# app = App(
#     token=os.environ.get("SLACK_BOT_TOKEN"),
#     signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
# )

# Add functionality here
# @app.event("app_home_opened") etc


# Start your app
# if __name__ == "__main__":
#     app.start(port=int(os.environ.get("PORT", 3000)))

if __name__ == "__main__":
  handler = SocketModeHandler(app, SLACK_APP_TOKEN)
  handler.start()