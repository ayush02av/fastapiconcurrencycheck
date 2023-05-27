import requests
import aiohttp
import asyncio
import time

start = time.time()
print('started')

urls = ['http://localhost'] * 100

async def get_url_data(url, session):
    r = await session.request('GET', url=f'{url}')
    data = await r.json()
    return data
    
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(get_url_data(url=url, session=session))
        results = await asyncio.gather(*tasks, return_exceptions=True)

    return results

data = asyncio.run(main(urls))
for item in data:
    print(item)

end = time.time()

print(end - start)