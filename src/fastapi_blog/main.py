from fastapi import FastAPI  ,Request
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




@app.get('/')
def get_posts(request : Request ):
    return templates.TemplateResponse(request , 'home.html', {'posts' : posts})

