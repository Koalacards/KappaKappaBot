import discord
from discord.ext import commands
import random
from confidential import RUN_ID
from kappadbfunc import set_info, get_info

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

LINKS = ['Kappa Links!', "Website: https://www.kkpsi.org/ \n \
    Facebook: https://www.facebook.com/KappaKappaPsi/ \n \
    Twitter: https://twitter.com/kappakappapsi?lang=en \n \
    Instagram: https://www.instagram.com/kappa.kappa.psi/?hl=en"]


LIST = [MISSION_STATEMENT, VISION_STATEMENT, PREAMBLE, CREED, FIRST_PURPOSE, SECOND_PURPOSE, THIRD_PURPOSE, FOURTH_PURPOSE, FIFTH_PURPOSE, MUSICIANSHIP, SERVICE, LEADERSHIP, BROTHERHOOD, MOTTO, FLOWER, GUIDING_SPIRIT, FOUNDERS, HEADQUARTERS, LINKS]

class KappaKappaBot(commands.Bot):
    def __init__(self, *, command_prefix: str, intents: discord.Intents) -> None:
        super().__init__(command_prefix=command_prefix, intents=intents)
    
    async def on_ready(self):
        print("ready")
        await self.tree.sync()

    async def on_message(self, message):
        guild_id = message.guild.id
        info_list = get_info(guild_id)
        if info_list is not None:
            num_messages, channel_id, counter = info_list[0], info_list[1], info_list[2]
            if num_messages > 0:
                if counter == num_messages:
                    set_info(guild_id, num_messages, channel_id, 0)
                    await _sendEmbedChannel(channel_id, _give_random_fact())
                    counter = 0
                counter = counter + 1
                set_info(guild_id, num_messages, channel_id, counter)
        await client.process_commands(message)

intents = discord.Intents.default()
intents.messages = True
client = KappaKappaBot(command_prefix='!', intents=intents)

@client.tree.command()
async def mission(interaction:discord.Interaction):
    """What is the kappa mission statement?"""
    await _sendEmbed(interaction, MISSION_STATEMENT)

@client.tree.command()
async def vision(interaction:discord.Interaction):
    """What is the kappa vision statement?"""
    await _sendEmbed(interaction, VISION_STATEMENT)

@client.tree.command()
async def preamble(interaction:discord.Interaction):
    """What is the kappa preamble?"""
    await _sendEmbed(interaction, PREAMBLE)

@client.tree.command()
async def creed(interaction:discord.Interaction):
    """What is the kappa creed?"""
    await _sendEmbed(interaction, CREED)

@client.tree.command()
async def musicianship(interaction:discord.Interaction):
    """Defines musicianship"""
    await _sendEmbed(interaction, MUSICIANSHIP)

@client.tree.command()
async def leadership(interaction:discord.Interaction):
    """Defines leadership"""
    await _sendEmbed(interaction, LEADERSHIP)

@client.tree.command()
async def service(interaction:discord.Interaction):
    """Defines service"""
    await _sendEmbed(interaction, SERVICE)

@client.tree.command()
async def brotherhood(interaction:discord.Interaction):
    """Defines brotherhood"""
    await _sendEmbed(interaction, BROTHERHOOD)

@client.tree.command()
async def flag(interaction:discord.Interaction):
    """What is the kappa flag?"""
    await interaction.response.send_message('https://cdn.discordapp.com/attachments/777521776213098499/777525150522408980/unknown.png')

@client.tree.command()
async def motto(interaction:discord.Interaction):
    """What is the national motto?"""
    await _sendEmbed(interaction, MOTTO)

@client.tree.command()
async def flower(interaction:discord.Interaction):
    """Shows the national flower"""
    await _sendEmbed(interaction, FLOWER)

@client.tree.command()
async def firstpurpose(interaction:discord.Interaction):
    """What is the first purpose?"""
    await _sendEmbed(interaction, FIRST_PURPOSE)

@client.tree.command()
async def secondpurpose(interaction:discord.Interaction):
    """What is the second purpose?"""
    await _sendEmbed(interaction, SECOND_PURPOSE)

@client.tree.command()
async def thirdpurpose(interaction:discord.Interaction):
    """What is the third purpose?"""
    await _sendEmbed(interaction, THIRD_PURPOSE)

@client.tree.command()
async def fourthpurpose(interaction:discord.Interaction):
    """What is the fourth purpose?"""
    await _sendEmbed(interaction, FOURTH_PURPOSE)

@client.tree.command()
async def fifthpurpose(interaction:discord.Interaction):
    """What is the fifth purpose?"""
    await _sendEmbed(interaction, FIFTH_PURPOSE)

@client.tree.command()
async def guidingspirit(interaction:discord.Interaction):
    """Who is our guiding spirit? (dont get this wrong)"""
    await _sendEmbed(interaction, GUIDING_SPIRIT)

@client.tree.command()
async def founders(interaction:discord.Interaction):
    """Who are the founders of kappa?"""
    await _sendEmbed(interaction, FOUNDERS)

@client.tree.command()
async def headquarters(interaction:discord.Interaction):
    """Wheres the headquarters of kappa?"""
    await _sendEmbed(interaction, HEADQUARTERS)

@client.tree.command()
async def links(interaction:discord.Interaction):
    """Shows the links to the website/social media"""
    await _sendEmbed(interaction, LINKS)

@client.tree.command()
async def shrine(interaction:discord.Interaction):
    """Shows the shrine"""
    await interaction.response.send_message('https://cdn.discordapp.com/attachments/777521776213098499/777528990353195028/unknown.png')



@client.tree.command()
async def random_fact(interaction:discord.Interaction):
    """Gives a random kappa fact!"""
    fact = _give_random_fact()
    await _sendEmbed(interaction, fact)

def _give_random_fact():
    return LIST[random.randint(0, len(LIST) - 1)]


@client.tree.command()
async def continuous_facts(interaction:discord.Interaction, num_messages:int, channel:discord.TextChannel):
    """Send continuous facts to a channel (if you want this turned off, set num_messages to 0)"""
    set_info(interaction.guild_id, num_messages, channel.id, 0)
    await interaction.response.send_message(f'Got it, the channel {channel.name} will now recieve random facts every {num_messages} messages.')


async def _sendEmbed(interaction:discord.Interaction, tuple):
    embed = discord.Embed(
        title=tuple[0],
        description=tuple[1],
        colour=discord.Colour.from_rgb(0, 22, 137)
    )
    await interaction.response.send_message(embed=embed)

async def _sendEmbedChannel(channel_id, tuple):
    channel = client.get_channel(channel_id)
    embed = discord.Embed(
        title=tuple[0],
        description=tuple[1],
        colour=discord.Colour.from_rgb(0, 22, 137)
    )
    await channel.send(embed=embed)


client.run(RUN_ID)