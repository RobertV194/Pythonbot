from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from pythonbot.keyboards.for_navigate import game
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.formatting import as_marked_section, Underline, Bold, as_key_value

GAMES = []

game_router = Router()

@game_router.message(Command('games'))
async def games_cmd(message: Message):
    await message.answer('Choose your action:', reply_markup=game)


@game_router.message((F.text == 'View all'))
async def add_game_cmd(message: Message):
    if not GAMES:
        await message.answer('There aren`t any games to view')
    for i in range(len(GAMES)):
        text = as_marked_section(
            Underline(Bold(f'Game {i+1}')),
            as_key_value('Topic', GAMES[i]['topic']),
            as_key_value('Genre', GAMES[i]['genre']),
            as_key_value('Studio', GAMES[i]['studio']),
            as_key_value('Country', GAMES[i]['country']),
            as_key_value('Release_date', GAMES[i]['release_date']),
            as_key_value('Memory', GAMES[i]['memory']),
            as_key_value('Multyplayer', GAMES[i]['multyplayer']),
            marker='🎮 '
        )
        await message.answer(text.as_html())


@game_router.message((F.text == 'Delete all'))
async def delete_game(message: Message):
    if not GAMES:
        await message.answer('There aren`t any games to delete')
    else:
        await message.answer('All games have been deleted successfully')
        return GAMES.clear()
class AddGame(StatesGroup):
    topic = State()
    genre = State()
    studio = State()
    country = State()
    release_date = State()
    memory = State()
    multyplayer = State()

@game_router.message(StateFilter(None), (F.text == 'Add game'))
async def add_game_cmd(message: Message, state: FSMContext):
    await message.answer('Enter the name:',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(AddGame.topic)

@game_router.message(AddGame.topic, F.text)
async def add_genre_cmd(message: Message, state: FSMContext):
    await state.update_data(topic=message.text)
    await message.answer('Enter a genre of the game: ')
    await state.set_state(AddGame.genre)


@game_router.message(AddGame.genre, F.text)
async def add_studio_cmd(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer('Enter a studio of the game:')
    await state.set_state(AddGame.studio)


@game_router.message(AddGame.studio, F.text)
async def add_country_cmd(message: Message, state: FSMContext):
    await state.update_data(studio=message.text)
    await message.answer('Enter a developer`s country:')
    await state.set_state(AddGame.country)


@game_router.message(AddGame.country, F.text)
async def add_release_date_cmd(message: Message, state: FSMContext):
    await state.update_data(country=message.text)
    await message.answer('Enter release date of the game(only numbers):')
    await state.set_state(AddGame.release_date)


@game_router.message(AddGame.release_date, F.text)
async def add_memory_cmd(message: Message, state: FSMContext):
    await state.update_data(release_date=message.text)
    await message.answer('Enter a memory of the game(in gigabytes, only numbers):')
    await state.set_state(AddGame.memory)


@game_router.message(AddGame.memory, F.text)
async def add_multyplayer_cmd(message: Message, state: FSMContext):
    await state.update_data(memory=message.text)
    await message.answer('Does this game have a multyplayer?(yes/no)')
    await state.set_state(AddGame.multyplayer)

@game_router.message(AddGame.multyplayer, F.text)
async def add_content_cmd(message: Message, state: FSMContext):
    await state.update_data(multyplayer=message.text)
    await message.answer('The game have been added successfully', reply_markup=game)
    data = await state.get_data()
    await message.answer(str(data))
    GAMES.append(data)
    await state.clear()