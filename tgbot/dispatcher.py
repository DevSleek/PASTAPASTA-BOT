from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

from tgbot.handlers.onboarding.handlers import start, help, about, settings, category, \
    cart, news, menu, feedback, cafe_location, contacts, basket, \
    about_order, marking, menus

from tgbot.handlers.onboarding.keyboards import MENU, BASKET, CAFE_LOCATION, ABOUT_ORDER, \
    FEEDBACK, CONTACS, SETTINGS

from tgbot.handlers.onboarding.states import LOCATION_STATE, MENUS_STATE, FEEDBACK_STATE


def setup_dispatcher(dp):

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            CommandHandler("help", help),
            CommandHandler("settings", settings),
            CommandHandler("about", about),
            CommandHandler("category", category),
            CommandHandler("cart", cart),
            CommandHandler("news", news),

            MessageHandler(Filters.text(FEEDBACK), feedback),
            MessageHandler(Filters.text(CAFE_LOCATION), cafe_location),
            MessageHandler(Filters.text(CONTACS), contacts),
            MessageHandler(Filters.text(BASKET), basket),
            MessageHandler(Filters.text(SETTINGS), settings),
            MessageHandler(Filters.text(ABOUT_ORDER), about_order),
            MessageHandler(Filters.regex('^(🏠 Bosh menu)$'), start)
        ],
        states={
            # LOCATION_STATE: [MessageHandler(Filters.text(MENU), location)],
            LOCATION_STATE: [
                MessageHandler(Filters.text(MENU), menu),
                MessageHandler(Filters.location, menus),
            ],
            FEEDBACK_STATE: [
                MessageHandler(Filters.regex('^(😊Hammasi yoqdi ❤️|☺️Yaxshi ⭐️⭐️⭐️⭐️|😐 Yoqmadi ⭐️⭐️⭐️|☹️ Yomon ⭐️⭐️|😤 Juda yomon👎🏻)$'), marking),
            ],
            # SETTINGS_STATE: [
            #     MessageHandler(Filters.regex('^(🏠 Bosh menu)$'), start),
            # ],
        },
        fallbacks=[
            CommandHandler("start", start),
            CommandHandler("help", help),
        ],
    )
    dp.add_handler(conv_handler)

    return dp