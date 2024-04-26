from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

from tgbot.handlers.onboarding.handlers import start, help, about, settings, category, \
    cart, news, menu, feedback, cafe_location, contacts, basket, about_order, marking, \
    menus, select_lenguage, sub_menus_by_category, product, order_finished

from tgbot.handlers.onboarding.keyboards import MENU, BASKET, CAFE_LOCATION, ABOUT_ORDER, \
    FEEDBACK, CONTACS, SETTINGS, BACK_TO, MAIN_MENU_KEYBOARD

from tgbot.handlers.onboarding.states import LOCATION_STATE, FEEDBACK_STATE, \
    SETTINGS_STATE, SUB_MENUS_STATE, PRODUCT_STATE, ORDER_FINISHED


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

            MessageHandler(Filters.text(MENU), menu),
            MessageHandler(Filters.text(FEEDBACK), feedback),
            MessageHandler(Filters.text(CAFE_LOCATION), cafe_location),
            MessageHandler(Filters.text(CONTACS), contacts),
            MessageHandler(Filters.text(BASKET), basket),
            MessageHandler(Filters.text(SETTINGS), settings),
            MessageHandler(Filters.text(ABOUT_ORDER), about_order),
            MessageHandler(Filters.text(MAIN_MENU_KEYBOARD), start)
        ],
        states={
            LOCATION_STATE: [
                MessageHandler(Filters.location, menus),
            ],
            SUB_MENUS_STATE: [
                MessageHandler(Filters.text & (~Filters.regex('^(⬅️ Ortga|📥 Savat)$')), sub_menus_by_category),
                MessageHandler(Filters.text(BASKET), basket),
                MessageHandler(Filters.text(BACK_TO), menus)
            ],
            PRODUCT_STATE: [
                MessageHandler(Filters.text & (~Filters.text(BACK_TO)), product),
                MessageHandler(Filters.text(BACK_TO), sub_menus_by_category)
            ],
            ORDER_FINISHED: [
                MessageHandler(Filters.text & (~Filters.text(BACK_TO)), order_finished),
                MessageHandler(Filters.text(BACK_TO), product)
            ],
            FEEDBACK_STATE: [
                MessageHandler(Filters.regex('^(😊Hammasi yoqdi ❤️|☺️Yaxshi ⭐️⭐️⭐️⭐️|😐 Yoqmadi ⭐️⭐️⭐️|☹️ Yomon ⭐️⭐️|😤 Juda yomon👎🏻)$'), marking),
            ],
            SETTINGS_STATE: [
                MessageHandler(Filters.regex('^(🌐 Tilni tanlash)$'), select_lenguage)
            ],
        },
        fallbacks=[
            CommandHandler("start", start),
            CommandHandler("help", help),
            MessageHandler(Filters.text(MENU), menu),
            MessageHandler(Filters.text(MAIN_MENU_KEYBOARD), start),
            MessageHandler(Filters.text(BASKET), basket),
        ],
    )
    dp.add_handler(conv_handler)

    return dp