"""Helper functions to address the reaction roles REST API"""

import os

HOST = (
    f"http://{os.environ.get('REACTION_ROLES_HOST', 'localhost')}:"
    f"{os.environ.get('REACTION_ROLES_PORT', '8000')}"
)
URLS = {
    "reaction_roles_message":f"{HOST}/api/v1/message/",
}

async def new_reaction_roles(bot, user_id, guild_id, channel_id, message_id):
    """Create new reaction roles message"""
    return await bot.web_client.post(
        f"{URLS['reaction_roles_message']}", 
        headers={"Invoker": str(user_id)},
        json={
            "guild_id": guild_id, 
            "channel_id": channel_id, 
            "message_id": message_id,
        },
    )
    