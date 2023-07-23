import aiohttp
import requests

from app.loggers.loggers import get_custom_logger


def get_data_from_request(url) -> str:
    logger = get_custom_logger(__name__)
    logger.info(f"Gathering data from {url}")
    data = requests.get(url).json()
    names = [person["name"] for person in data["people"]]
    output_str = "\n".join(names)
    print(f"Who now in cosmos:\n{output_str}")


async def get_data_from_async_request(url) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                r = await resp.json()
                names = [person["name"] for person in r["people"]]
                print(f"Total in cosmos: {len(names)}")
            else:
                print(f"Error: {resp.status}")
