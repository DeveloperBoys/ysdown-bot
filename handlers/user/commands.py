import requests
import json

from keyboards.inlines.url_data import url_data
from loader import dp, bot
from aiogram import types
from decouple import config

BASE_URL = config('BASE_URL')
AUTH_TOKEN = config('TOKEN')


@dp.message_handler(state=None)
async def post_url(message: types.Message):
    url = message.text
    print('1')
    head = {'Authorization': 'token {}'.format(AUTH_TOKEN)}
    print('2')
    try:
        print('3')
        response = requests.post(url=f'{BASE_URL}/api/v1/url/', headers=head, data={
            'original_url': url
        })
        print('4')
        if response.status_code == 500:
            await message.answer("Uzur serverda internet bilan muammo bo'lib qoldi.")
        elif response.status_code != 404:
            # await message.delete()
            await message.answer('Tekshirilmoqda...')
            data = json.loads(response.content)
            reply_markup = await url_data(data)
            text = f"ℹ {data['video_title']}\n👤 {data['video_author']}\n🕒: <a>{data['video_time']} daqiqa</a>"
            await message.answer(text=text, reply_markup=reply_markup)
        else:
            await message.reply(f"Uzr nimadur xato - {response.status_code}")
    except requests.HTTPError or requests.ConnectionError as er:
        print(er)
