from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()
class HelloWorld():
    def read_hello(self):
        return {"message": "Hello World"}
    
hello_world = HelloWorld()
route = APIRouter()
route.add_api_route('/api/v2/hello-world', 
endpoint = hello_world.read_hello, methods=["GET"])
app.include_router(route)

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


