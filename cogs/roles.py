import discord
from discord.ext import commands
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

class roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def addRole(self, ctx, user : discord.Member, *, role: discord.Role):

        if role in user.roles:
            await send.ctx(f"{user.mention} already has that role, {role}")
        else:
            await user.add_roles(role)
            await ctx.send(f"Added {role} to {user.mention}")

    @addRole.error
    async def role_error(self, ctx, error):
        if inistance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")


    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def removeRole(self, ctx, user : discord.Member, *, role: discord.Role):

        if role in user.roles:
            await user.remove_roles(role)
            await send.ctx(f"Removed {role} from {user.mention}")
        else:
            await ctx.send(f"{user.mention} doesn't have the role {role}")

    @removeRole.error
    async def removeRole_error(self, ctx, error):
        if inistance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")




def setup(client):
    client.add_(roles(client))