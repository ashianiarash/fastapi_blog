from fastapi import FastAPI  ,Request ,  HTTPException , status 
from fastapi.responses import JSONResponse 
from fastapi.templating import Jinja2Templates 

app = FastAPI()

templates = Jinja2Templates(directory='../template')

posts : list[dict] = [
    {
        "id" :1 ,
        "author" : 'Corey Schafer',
        "title" : "Fastapi FrameWork",
        "content" : "Fastapi is Awesome",
        "date_posted" : "20 April 2026"
    } ,
    {
            "id" :2 ,
            "author" : 'Jane Doe',
            "title" : "JinJa2 is a good template redering lib",
            "content" : "JinJa2 is Awesome",
            "date_posted" : "20 October 2026"
        }
    
]

class NotFoundPost(Exception):
    status_code = 404
    def __init__(self, item_id: int ):
        self.item = item_id
    
    def message(self) -> str:
        return f" پیدا نکردم{self.item}متاسفم پسر آیتمی  با این آیدی "
    
    
@app.exception_handler(NotFoundPost)
async def not_found_handler(request : Request , exc : NotFoundPost):
    return JSONResponse(
        status_code= exc.status_code ,
        content={
            "message" : exc.message(),
        },
    )

@app.get('/')
def get_posts(request : Request ):
    return templates.TemplateResponse(request , 'home.html', {'posts' : posts})

@app.get('api/post/{item_id}')
def get_post(item_id: int):
    for post in posts :
        if post.get('id') == item_id:
            return post 
    raise NotFoundPost(item_id)
        