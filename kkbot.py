import discord
from discord.ext import commands
import random

MISSION_STATEMENT = ['Mission Statement', "Kappa Kappa Psi is a co-educational fraternal organization that advances college \
and university bands for the benefit of its members and society through dedicated \
service and support to bands, encouragement of musical growth, lifelong educational \
experiences, leadership opportunities, and recognition"]

VISION_STATEMENT = ['Vision Statement', "Kappa Kappa Psi empowers and influences the vibrant and diverse college band\
movement through purposeful programming, unified messaging, and excellence in \
service and operations."]

PREAMBLE = ['Preamble To The National Constitution Of Kappa Kappa Psi', "Be it known that Kappa Kappa Psi, National Honorary Band Fraternity for College \
Bandmembers, is an organization operating exclusively in the field of the college and \
university bands, and for the following several purposes: \n \
(1) To promote the existence and welfare of the college and university bands and to \
cultivate at large a wholesome respect for their activities and achievements. \n \
(2) To honor outstanding bandmembers through privilege of membership extended as a \
reward for technical achievement and appreciation for the best in music. \n \
(3) To stimulate campus leadership and promulgate an uncompromising respect through \
the medium of the college band for gracious conduct, good taste and unswerving loyalty. \n \
(4) To foster a close relationship between college bands and promote a high average of \
attainment by the performance of good music and selection of worthwhile projects. \n \
(5) To provide a pleasant and helpful social experience for all engaged in college band \
work and to cooperate with other musical organizations in any manner consistent with the \
purposes of the institution at which chapters are located."]


CREED = ['Creed', "We, the brothers of Kappa Kappa Psi, believe that service to the college or university \
band program fosters responsibility, loyalty, and leadership; that a spirit of brotherhood \
is enhanced by the participation in a band program; that music is a universal language \
and truly the greatest of the arts; and that through fraternal participation, each member \
will strive for the highest"]

MUSICIANSHIP = ['Musicianship', "Musicianship in Kappa Kappa Psi begins with \
the appreciation of music as an art-form through \
the desire for the best in artistic performances, our \
knowledge, skill, and artistic sensitivity. As brothers, \
we must support our fellow musicians through \
encouragement and helping weaker performers"]

LEADERSHIP = ['Leadership', "Leadership is a cornerstone to Kappa Kappa Psi, \
and brothers possess an agreeable and enthusiastic attitude \
through the lessons learned in the ritual. As brothers we are \
more capable, more concerned, and more interested in the \
band program due to the proven dependability of the chapter."]

SERVICE = ['Service', "Service is accomplished through the result of coordinated \
endeavors. The service component of Kappa Kappa Psi is vital to the \
very breadth of the organization. We exist in our current state due to \
the service nature of the fraternity to the college and university band \
programs. "]

BROTHERHOOD = ['Brotherhood', "Brotherhood is part of a greater educational and service \
activity devoted to strengthening the team and individual into the \
best they can be. Our brotherhood requires optimism, enthusiasm, \
and a cooperative spirit. Through chapter and district events, our \
brotherhood grows and develops each year"]

MOTTO = ['Motto Of Kappa Kappa Psi', 'Strive for the Highest']

FLOWER = ['Official Flower Of Kappa Kappa Psi', 'Red Carnation']

FIRST_PURPOSE = ['The First Purpose', "To promote the existence and welfare of the college and university bands and to \
cultivate at large a wholesome respect for their activities and achievements. "]

SECOND_PURPOSE = ['The Second Purpose', "To honor outstanding band members through privilege of membership, extended as \
a reward for technical achievement and appreciation for the best in music."]

THIRD_PURPOSE = ['The Third Purpose', "To stimulate campus leadership and promulgate an uncompromising respect through \
the medium of the college band, for gracious conduct, good taste, and unswerving \
loyalty."]

FOURTH_PURPOSE = ['The Fourth Purpose', "To foster a close relationship between college bands and promote a high average of \
attainment by the performance of good music and selection of worthwhile projects."]

FIFTH_PURPOSE = ['The Fifth Purpose', "To provide a pleasant and helpful social experience for all engaged \
in college band work and to cooperate with other musical \
organizations in any manner consistent with the purposes of the \
institution at which chapters are located."]

GUIDING_SPIRIT = ['The Guiding Spirit of Kappa Kappa Psi', "Bohumil Makovsky, Director of Bands and Head of the Music Department, Oklahoma Agricultural & Mechanical College"]

FOUNDERS = ['The Ten Founders of Kappa Kappa Psi', "A. Frank Martin, William \
A. Scroggs, Raymond D. Shannon, Carl A. Stevens, Clyde Haston, Clayton E. Soule, \
William H. Coppedge, Asher Hendrickson, Dick Hurst, and Iron Hawthorne Nelson"]

HEADQUARTERS = ['The Headquarters of Kappa Kappa Psi', 'Stillwater Station in Stillwater, Oklahoma']


LIST = [MISSION_STATEMENT, VISION_STATEMENT, PREAMBLE, CREED, FIRST_PURPOSE, SECOND_PURPOSE, THIRD_PURPOSE, FOURTH_PURPOSE, FIFTH_PURPOSE, MUSICIANSHIP, SERVICE, LEADERSHIP, BROTHERHOOD, MOTTO, FLOWER, GUIDING_SPIRIT, FOUNDERS, HEADQUARTERS]

CONTINUOUS_FACTS = 0

CONTINUOUS_CHANNEL = None

COUNTER = 0

client = commands.Bot(command_prefix='!')


@client.command()
async def mission(ctx):
    await _sendEmbed(ctx, MISSION_STATEMENT)

@client.command()
async def vision(ctx):
    await _sendEmbed(ctx, VISION_STATEMENT)

@client.command()
async def preamble(ctx):
    await _sendEmbed(ctx, PREAMBLE)

@client.command()
async def creed(ctx):
    await _sendEmbed(ctx, CREED)

@client.command()
async def musicianship(ctx):
    await _sendEmbed(ctx, MUSICIANSHIP)

@client.command()
async def leadership(ctx):
    await _sendEmbed(ctx, LEADERSHIP)

@client.command()
async def service(ctx):
    await _sendEmbed(ctx, SERVICE)

@client.command()
async def brotherhood(ctx):
    await _sendEmbed(ctx, BROTHERHOOD)

@client.command()
async def flag(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/777521776213098499/777525150522408980/unknown.png')

@client.command()
async def motto(ctx):
    await _sendEmbed(ctx, MOTTO)

@client.command()
async def flower(ctx):
    await _sendEmbed(ctx, FLOWER)

@client.command()
async def firstpurpose(ctx):
    await _sendEmbed(ctx, FIRST_PURPOSE)

@client.command()
async def secondpurpose(ctx):
    await _sendEmbed(ctx, SECOND_PURPOSE)

@client.command()
async def thirdpurpose(ctx):
    await _sendEmbed(ctx, THIRD_PURPOSE)

@client.command()
async def fourthpurpose(ctx):
    await _sendEmbed(ctx, FOURTH_PURPOSE)

@client.command()
async def fifthpurpose(ctx):
    await _sendEmbed(ctx, FIFTH_PURPOSE)

@client.command()
async def guidingspirit(ctx):
    await _sendEmbed(ctx, GUIDING_SPIRIT)

@client.command()
async def founders(ctx):
    await _sendEmbed(ctx, FOUNDERS)

@client.command()
async def headquarters(ctx):
    await _sendEmbed(ctx, HEADQUARTERS)

@client.command()
async def shrine(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/777521776213098499/777528990353195028/unknown.png')



@client.command()
async def random_fact(ctx):
    fact = _give_random_fact()
    await _sendEmbed(ctx, fact)

def _give_random_fact():
    return LIST[random.randint(0, len(LIST) - 1)]


@client.command()
async def continuous_facts(ctx, num_messages:int, channel:discord.TextChannel):
    global CONTINUOUS_CHANNEL
    global CONTINUOUS_FACTS
    CONTINUOUS_FACTS = num_messages
    CONTINUOUS_CHANNEL = channel
    await ctx.send(f'Got it, the channel {channel.name} will now recieve random facts every {num_messages} messages.')



@client.event
async def on_message(message):
    if CONTINUOUS_FACTS > 0 and CONTINUOUS_CHANNEL != None:
        global COUNTER
        if COUNTER == CONTINUOUS_FACTS:
            COUNTER = 0
            await _sendEmbedChannel(CONTINUOUS_CHANNEL, _give_random_fact())
            COUNTER = 0
        COUNTER = COUNTER + 1

    await client.process_commands(message)


async def _sendEmbed(ctx, tuple):
    embed = discord.Embed(
        title=tuple[0],
        description=tuple[1],
        colour=discord.Colour.from_rgb(0, 22, 137)
    )
    await ctx.send(embed=embed)

async def _sendEmbedChannel(channel, tuple):
    embed = discord.Embed(
        title=tuple[0],
        description=tuple[1],
        colour=discord.Colour.from_rgb(0, 22, 137)
    )
    await channel.send(embed=embed)


client.run('Nzc3NTIwMTU1NTQyMjkwNDMz.X7EoEg.lMP6ZPwXrxhxcNqtZoynIn9olR4')