import disnake
from disnake.ext import commands
import re
import asyncio

class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="timer", description="Set a timer")
    async def timer(self, inter: disnake.ApplicationCommandInteraction, time: str):
        await inter.response.defer()

        matches = re.findall(r'(\d+)([smh])', time.lower())
        if not matches:
            await inter.followup.send("Invalid time format! Use something like `10s`, `5m`, `2h`, or mix them like `1h30m`")
            return

        total_seconds = 0
        for amount, unit in matches:
            amount = int(amount)
            if unit == 's':
                total_seconds += amount
            elif unit == 'm':
                total_seconds += amount * 60
            elif unit == 'h':
                total_seconds += amount * 3600

        if total_seconds <= 0:
            await inter.followup.send("Time must be more than 0 seconds")
            return

        await inter.followup.send(f"Timer set for {time}. I'll ping you when time is up")
        await asyncio.sleep(total_seconds)
        await inter.followup.send(f"{inter.author.mention}, time is up")

def setup(bot):
    bot.add_cog(Timer(bot))