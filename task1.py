import asyncio
import time
import aiohttp

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("URL:",url)
            print("Status:",response.status)
            print("Content-type:",response.headers['content-type'])
            html = await response.text()
            print("Body:",html[:15],'...')
            print("------------------------------------------")

#synchronous programming
async def main_sync():
    url_base = "https://reqres.in/api/users?page{el}" #the base URL (to be formatted to give the required URLs)
    arr = [1,2,3] #to be used for formatting the base URL

    obj1 = download(url_base.format(el = arr[0]))
    obj2 = download(url_base.format(el = arr[1]))
    obj3 = download(url_base.format(el = arr[2]))

    start = time.time()

    await obj1
    await obj2
    await obj3

    time_taken = time.time() - start

    print('Time taken (by synchronous programming method): {0}s'.format(time_taken))
    print("****************************")

#asynchronous programming
async def main_async():
    url_base = "https://reqres.in/api/users?page{el}" #the base URL (to be formatted to give the required URLs)
    arr = [1,2,3] #to be used for formatting the base URL

    obj1 = download(url_base.format(el = arr[0]))
    obj2 = download(url_base.format(el = arr[1]))
    obj3 = download(url_base.format(el = arr[2]))

    start = time.time()

    await asyncio.gather(obj1,obj2,obj3)

    time_taken = time.time() - start

    print('Time taken (by asynchronous programming method): {0}s'.format(time_taken))
    print("****************************")

if __name__=="__main__":
    asyncio.run(main_sync())
    asyncio.run(main_async())
