from kappamodels import *

def set_info(guild_id, num_messages, channel_id, counter):
    query = KappaData.select().where(KappaData.guild_id == guild_id)
    if len(query) == 0:
        KappaData.create(guild_id=guild_id, num_messages=num_messages, channel_id=channel_id, counter=counter)
    else:
        new_query = KappaData.update(num_messages=num_messages, channel_id=channel_id, counter=counter).where(
            KappaData.guild_id == guild_id
        )
        return new_query.execute()

def get_info(guild_id):
    query = KappaData.select().where(KappaData.guild_id == guild_id)
    if len(query) == 0:
        return None
    else:
        for item in query:
            return [item.num_messages, item.channel_id, item.counter]
    