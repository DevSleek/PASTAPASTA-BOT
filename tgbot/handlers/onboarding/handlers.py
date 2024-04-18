import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from telegram import KeyboardButton, ReplyKeyboardMarkup,  InlineKeyboardMarkup, Update, InlineKeyboardButton
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)

from users.models import User
from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from tgbot.handlers.onboarding.keyboards import MAIN_MENU_KEYBOARD, MAIN_KEYBOARD, MARKS, SETTINGS_KEYBOARD, BASKET
from tgbot.handlers.onboarding.states import FEEDBACK_STATE, MENUS_STATE, LOCATION_STATE, SETTINGS_STATE, SUB_MENUS_STATE
from products.models import Menu, Product


def start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if not created:
        text = static_text.start_not_created.format(first_name=u.first_name)
        update.message.reply_text(text)

    update.message.reply_text(
        "«CIAO!» {}! Kichik Italiyaga xush kelibsiz 🇮🇹 \n\n Nima buyurtma qilamiz?".format(u.first_name),
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            resize_keyboard=True,
        ),
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Buyurtma va boshqa savollar bo'yicha javob olish uchun @pastarobot'ga murojaat qiling, barchasiga javob beramiz :)"""
    )


def about(update: Update, context: CallbackContext):
    update.message.reply_text(
        "«CIAO!»  Sukhrob! Kichik Italiyaga xush kelibsiz🇮🇹 \n\n Nima buyurtma qilamiz?"
    )


def settings(update: Update, context: CallbackContext):
    update.message.reply_text(
        "⚙️ Sozlamalar",
        reply_markup=ReplyKeyboardMarkup(
            SETTINGS_KEYBOARD + MAIN_MENU_KEYBOARD,
            one_time_keyboard=False,
            resize_keyboard=True,
        )
    )
    return SETTINGS_STATE


def select_lenguage(update: Update, context: CallbackContext):

    buttons = [
        [InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="uzb")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="rus")],
    ]
    markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(
        """Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️""",
        reply_markup=markup
    )


def category(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Kategoriyalar"
    )


def cart(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Savat"
    )


def news(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Yangiliklar"
    )


def history(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Buyurtmalar tarixi"
    )


def menu(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🇮🇹 Italiyani yetkazib berish!
🍝 Italiyancha pasta korobochkalarda!
⏰ С 11:00 до 01:00 
🛵 Hoziroq buyurtma bering!

*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin""",
    )
    keyboard = [[KeyboardButton("📍 Manzilini yuborish", request_location=True)]]
    update.message.reply_text(
        """Qaysi manzilga yetkazilsin?
Manzilni kiriting yoki "📍 Manzilini yuborish" tugmachasini bosing 👇🏻""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            one_time_keyboard=True,
            resize_keyboard=True,
        ),
    )
    return LOCATION_STATE


def menus(update: Update, context: CallbackContext):
    menus = Menu.objects.all()
    menu_keyboard = []
    for i in range(0, len(menus), 2):
        if i+1 != len(menus):
            menu_keyboard.append([menus[i].title, menus[i+1].title])
        else:
            menu_keyboard.append([menus[i].title])
    menu_keyboard.insert(0, BASKET)
    menu_keyboard.append([MAIN_MENU_KEYBOARD])
    reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
    update.message.reply_text(
        "Quyidagilardan birini tanlang 👇🏻",
        reply_markup=reply_markup,
    )
    return SUB_MENUS_STATE


def sub_menus_by_category(update: Update, context: CallbackContext):
    text = update.message.text
    product = Menu.product.get(title=text)
    menu_keyboard = []
    for i in range(0, len(product), 2):
        if i + 1 != len(product):
            menu_keyboard.append([product[i].title, product[i + 1].title])
        else:
            menu_keyboard.append([product[i].title])
    menu_keyboard.insert(0, BASKET)
    menu_keyboard.append([MAIN_MENU_KEYBOARD])
    reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
    update.message.reply_text(
        "Mahsulotni tanlang 👇🏻",
        reply_markup=reply_markup,
    )
    return PRODUCT_STATE


def product(update: Update, context: CallbackContext):
    title = update.message.text
    product = Product.objects.get(title=title)
    update.message.reply_text(
        product.price
    )


def basket(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sizning savatingiz bo'sh"
    )


def cafe_location(update: Update, context: CallbackContext):
    update.message.reply_location(latitude=41.27422, longitude=69.19017)
    update.message.reply_text(
        """🤩 Pastani kafeimizga kelib to'g'ridan-to'g'ri skovorodkadan ta'tib ko'ring - aynan shu uchun ham shaharning markazida joy ochdik, manzil Ц-1'da Ecopark va 64 maktab yonida

📌 Ish tartibi: du - pa 11:00 - 23:00 / ju 14:00 - 23:00 / sha - yak 11:00 - 23:00

Operator bilan aloqa 👉 @pastarobot"""
    )


def about_order(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🇮🇹 Italiyani yetkazib berish!
🍝 Italiyancha pasta korobochkalarda!
⏰ С 11:00 до 01:00 
🛵 Hoziroq buyurtma bering!

*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin""",
    )


def feedback(update: Update, context: CallbackContext):
    update.message.reply_text(
        """✅ PASTA-PASTA ni tanlaganingiz uchun rahmat.
Agar Siz bizning xizmatlarimiz sifatini yaxhshilashga yordam bersangiz benihoyat hursand bo’lamiz.
Buning uchun 5 ballik tizim asosida bizni baholang""",
        reply_markup=ReplyKeyboardMarkup(
            MARKS + MAIN_MENU_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
            resize_keyboard=True,
        ),
    )
    return FEEDBACK_STATE


def marking(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Rahmat! Bizning xizmatlarimizni baholaganiz uchun rahmat! 🙏🏻",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            resize_keyboard=True,
        ),
    )

    return ConversationHandler.END


def contacts(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Buyurtma va boshqa savollar bo'yicha javob olish uchun @pastarobot'ga murojaat qiling, barchasiga javob beramiz :)"
    )


def secret_level(update: Update, context: CallbackContext) -> None:
    # callback_data: SECRET_LEVEL_BUTTON variable from manage_data.py
    """ Pressed 'secret_level_button_text' after /start command"""
    user_id = extract_user_data_from_update(update)['user_id']
    text = static_text.unlock_secret_room.format(
        user_count=User.objects.count(),
        active_24=User.objects.filter(updated_at__gte=timezone.now() - datetime.timedelta(hours=24)).count()
    )

    context.bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=update.callback_query.message.message_id,
        parse_mode=ParseMode.HTML
    )
