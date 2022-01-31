from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Sends the help message"),
            types.BotCommand("help", "Help"),
            types.BotCommand('list', 'Sends list of photos'),
            types.BotCommand('rules', 'Sends the rules'),
        ]
    )
