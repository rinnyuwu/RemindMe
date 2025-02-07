import disnake
from disnake.ext import commands
import re
import asyncio

class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="timer", description="Set a timer")
    async def timer(self, inter: disnake.ApplicationCommandInteraction, time: str):
        matches = re.findall(r'(\d+)([smh])', time.lower())
        if not matches:
            await inter.response.send_message("Invalid time format Use something like `10s`, `5m`, `2h`, or mix them like `1h30m`")
            return

        total_seconds = sum(int(amount) * {"s": 1, "m": 60, "h": 3600}[unit] for amount, unit in matches)

        if total_seconds <= 0:
            await inter.response.send_message("Time must be more than 0 seconds")
            return

        await inter.response.send_message(f"Timer set for {time} I'll ping you when time is up")
        await asyncio.sleep(total_seconds)
        await inter.channel.send(f"{inter.author.mention}, time is up")

def setup(bot):
    bot.add_cog(Timer(bot))
