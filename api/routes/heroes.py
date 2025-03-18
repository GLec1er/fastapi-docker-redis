from fastapi import APIRouter

router = APIRouter()

fake_heroes = [
    {'name': 'Spider-man', 'title': 'spider'},
    {'name': 'Iron-man', 'title': 'iron'},
    {'name': 'Thor', 'title': 'thor'},
    {'name': 'Hulk', 'title': 'hulk'},
    {'name': 'Captain America', 'title': 'captain'},
    {'name': 'Black Widow', 'title': 'black widow'},
    {'name': 'Hawkeye', 'title': 'hawkeye'},
    {'name': 'Winter Soldier', 'title': 'winter soldier'},
    {'name': 'Ant-Man', 'title': 'ant man'},
]


@router.get("")
async def get_heroes():
    return fake_heroes

