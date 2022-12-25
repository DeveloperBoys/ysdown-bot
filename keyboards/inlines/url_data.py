from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

call_data = CallbackData("show_menu", "itag")


def make_callback_data(itag=None):
    return call_data.new(itag=itag)


async def url_data(data):
    item = 0
    markup = InlineKeyboardMarkup(row_width=2)

    results = data['filtered_video']
    for result in results:
        res = results[result]
        print("11111111111111111111111111111111111111111")
        print(result)
        print("11111111111111111111111111111111111111111")
        itag = res['itag']
        resolution = res['resolution']
        filesize = res['filesize']

        callback_data = make_callback_data(
            itag=itag
        )

        markup.insert(
            InlineKeyboardButton(text=f"{filesize}MB, {resolution}", callback_data=callback_data)
        )

    return markup
