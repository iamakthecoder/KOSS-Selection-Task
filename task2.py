import asyncio
import time
import aiohttp
import json
import os

async def download_json(url,filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data_json = json.loads(await response.read())
            with open(filename,"w") as f:
                json.dump(data_json,f)

async def synchronised_main(base_url):
    #'sync' folder to store the JSON files downloaded through synchronous programming method
    if not os.path.exists("sync"):
        os.mkdir("sync")

    start = time.time()

    for i in range(1,201):
        await download_json(base_url.format(comic_id = i),"sync/file{num}_sync.json".format(num = i))

    time_duration = time.time()-start

    print("Time taken by synchronous programming method (in s):",time_duration)

async def asynchronised_main(base_url):
    #'async' folder to store the JSON files downloaded through asynchronous programming method
    if not os.path.exists("async"):
        os.mkdir("async")

    tasks=[]
    for i in range(1,201):
        tasks.append(download_json(base_url.format(comic_id=i),"async/file{num}_async.json".format(num=i)))

    start = time.time()

    await asyncio.gather(*tasks)

    time_duration = time.time()-start

    print("Time taken by asynchronous programming method (in s):",time_duration)
    
if __name__=="__main__":
    url_base = "https://xkcd.com/{comic_id}/info.0.json"
    asyncio.run(synchronised_main(url_base))
    asyncio.run(asynchronised_main(url_base))