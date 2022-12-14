import os
from discord.ext import commands
from discord import app_commands
from cogs.Modules.button import Button
from cogs.Modules.clip_functions import *

guild_id = os.getenv('GUILD_ID')


class soundboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="soundboard", description="Displays a Soundboard for your listening pleasure :3")
    async def soundboard(self, interaction: discord.Interaction):
        view = discord.ui.View()
        view.add_item(Button("Gai", gai_clip))
        view.add_item(Button("Cri", cri_clip))
        view.add_item(Button("Ehh", ehh_clip))
        view.add_item(Button("Luca", luca_clip))
        view.add_item(Button("OwO", owo_clip))
        view.add_item(Button("Wtf", wtf_clip))
        view.add_item(Button("Amb", amb_clip))
        view.add_item(Button("Boy", boy_clip))
        view.add_item(Button("Dic", dic_clip))
        view.add_item(Button("Mouth", mouth_clip))
        view.add_item(Button("Arf", arf_clip))
        view.add_item(Button("Women", women_clip))
        view.add_item(Button("UwU", funny_yawn))
        view.add_item(Button("Boba", boba_clip))
        view.add_item(Button("Dom", dom_clip))
        view.add_item(Button("Yawn", yawn_clip, discord.ButtonStyle.green, "<a:captainsippycup:1004071026918948884>"))

        await interaction.response.send_message("Here you go ^_^", view=view, ephemeral=True)


async def setup(bot):
    await bot.add_cog(soundboard(bot), guilds=[discord.Object(id=guild_id)])
