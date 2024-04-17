from typing import Dict

from telegram import Bot, BotCommand


def set_up_commands(bot_instance: Bot) -> None:

    # langs_with_commands: Dict[str, Dict[str, str]] = {
    #     'en': {
    #         'start': 'Start django bot 🚀',
    #         'stats': 'Statistics of bot 📊',
    #         'admin': 'Show admin info ℹ️',
    #         'ask_location': 'Send location 📍',
    #         'broadcast': 'Broadcast message 📨',
    #         'export_users': 'Export users.csv 👥',
    #     },
    #     'ru': {
    #         'start': 'Запустить django бота 🚀',
    #         'stats': 'Статистика бота 📊',
    #         'admin': 'Показать информацию для админов ℹ️',
    #         'broadcast': 'Отправить сообщение 📨',
    #         'ask_location': 'Отправить локацию 📍',
    #         'export_users': 'Экспорт users.csv 👥',
    #     }
    # }
    #
    # bot_instance.delete_my_commands()
    # for language_code in langs_with_commands:
    #     bot_instance.set_my_commands(
    #         language_code=language_code,
    #         commands=[
    #             BotCommand(command, description) for command, description in langs_with_commands[language_code].items()
    #         ]
    #     )
    commands = [
        BotCommand("start", "Main menu"),
        BotCommand("help", "Help"),
        BotCommand("settings", "Settings"),
        BotCommand("about", "About us"),
        BotCommand("category", "Category"),
        BotCommand("cart", "Cart"),
        BotCommand("news", "News"),
        BotCommand("history", "Order history"),
    ]

    bot = Bot(settings.TELEGRAM_TOKEN)
    bot.set_my_commands(commands)


set_up_commands(bot)
