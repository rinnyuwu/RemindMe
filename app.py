import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def load_cogs():
    for root, dirs, files in os.walk('./cogs'):
        for file in files:
            if file.endswith('.py'):
                try:
                    extension = os.path.join(root, file).replace('./', '').replace('/', '.').replace('\\', '.').removesuffix('.py')
                    bot.load_extension(extension)
                except Exception as e:
                    print(f"er {extension}: {e}")

@bot.event
async def on_ready():
    await load_cogs()

bot.run(os.getenv("TOKEN"))