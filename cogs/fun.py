import discord
import datetime
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, BucketType.user)
    async def reverse(self, ctx, *, msg: str):
        '''Reverses stuff'''
        em = discord.Embed(title="Finished reversing...", description=msg[::-1], color=0xFDDEAB, timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=em)

    @reverse.error
    async def reverse_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            em = discord.Embed(color=discord.Color.blurple())
            em.add_field(name='Cooldown Initiated!', value=f'Try again in {a} seconds.')
            await ctx.send(embed=em)
        elif isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(color=discord.Color.blurple())
            em.add_field(name="Missing Argument", value="One or more arguments are missing.")
            await ctx.send(embed=em, delete_after=10)
        else:
            raise(error)
