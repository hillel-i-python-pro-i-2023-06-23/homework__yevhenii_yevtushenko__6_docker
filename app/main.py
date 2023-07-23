import asyncio

from app.services.get_requests import get_data_from_request, get_data_from_async_request
from app.services.read_csv import read_csv_file
from app.services.read_from_file import read_file
from app.services.show_user import show_users


def main():
    read_csv_file("https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt")
    read_file()
    show_users()

    url = "http://api.open-notify.org/astros.json"
    get_data_from_request(url)
    asyncio.run(get_data_from_async_request(url))
