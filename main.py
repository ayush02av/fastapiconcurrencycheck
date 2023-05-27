from fastapi import FastAPI
import asyncio  
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, reload=True)