"""{
  "name": "String Generator by Alpha",
  "description": "Telegram bot to generate Pyrogram & Telethon StringSession Made By Alpha",
  "logo": "https://te.legra.ph/file/ac72a0208034b15f04c18.jpg",
  "keywords": [
    "telegram",
    "bot",
    "python",
    "pyrogram"
  ],
    "buildpacks": [{
    "url": "heroku/python"
  }],
  "formation": {
    "worker": {
      "quantity": 1,
      "size": "free"
    }
  },
  "addons": [
      {
         "options": {
            "version": "12"
         },
         "plan": "heroku-postgresql"
      }
   ],
  "repository": "https://github.com/theend-alpha/StringBot",
  "env": {
    "ENVIRONMENT": {
      "description": "Don't change ANYTHING.",
      "required": true,
      "value": "ANYTHING"
    },
    "API_ID": {
      "description": "Get this value from my.telegram.org.",
      "required": true,
      "value": ""
    },
    "API_HASH": {
      "description": "Get this value from my.telegram.org.",
      "required": true,
      "value": ""
    },
    "BOT_TOKEN": {
      "description": "Obtain a Telegram bot token by contacting @BotFather",
      "required": true,
      "value": ""
    },
    "MONGO_DB_URL": {
      "description": "omfoo db url",
      "required": true,
      "value": ""
    }
  }
}
"""
