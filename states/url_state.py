from aiogram.dispatcher.filters.state import StatesGroup, State


class UrlState(StatesGroup):
    content_data = State()
