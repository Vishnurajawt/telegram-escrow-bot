from telethon import TelegramClient, events

# API details (tere actual values)
api_id = 14563912
api_hash = 'bfbb51393ce7377d017fe6c7a76bd174'
bot_token = '7571710790:AAGIXpTprxtzITCmV7nxSDqXfFUIiLU0rLQ'
group_id = -1002630965800  # ye teri group id

# Client start
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Event listener for new messages in the group
@client.on(events.NewMessage(chats=group_id))
async def edit_incoming_message(event):
    try:
        await client.edit_message(
            entity=group_id,
            message=event.message.id,
            text="Wanna do Escrow? [Click me 👉🧡](https://t.me/+uGGr_-oKjUpkNjA1)",
            parse_mode='md'
        )
        print(f"✅ Message {event.message.id} edited.")
    except Exception as e:
        print(f"❌ Failed to edit: {e}")

print("🚀 Bot is running...")
client.run_until_disconnected()
