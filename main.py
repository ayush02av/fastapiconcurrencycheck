from fastapi import FastAPI
import asyncio  

async def wait():  
    print ("Waiting 5 seconds. ")  
    for _ in range(1):  
        await asyncio.sleep(1)  
        print ("Hello")  
    print ("Finished waiting.")

app = FastAPI()

@app.get("/")
async def root():
    await wait()
    return {"message": "Hello World"}