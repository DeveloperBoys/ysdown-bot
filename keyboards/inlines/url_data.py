from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

call_data = CallbackData("show_menu", "itag")


def make_callback_data(itag=None):
    return call_data.new(itag=itag)


async def url_data(data):
    markup = InlineKeyboardMarkup(row_width=2)

    results = data['filtered_video']
    for result in results:
        itag = result['itag']
        resolution = result['resolution']
        filesize = result['filesize']

        callback_data = make_callback_data(
            itag=itag
        )

        markup.insert(
            InlineKeyboardButton(text=f"{filesize}MB, {resolution}", callback_data=callback_data)
        )

    return markup
