# from turtle import home
from fastapi import FastAPI , Request 
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles



app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
def home():
     return RedirectResponse(url="/login")

@app.get("/vaccination_center")
def userLogin(request: Request):
    return templates.TemplateResponse(
        "admin.html" , {"request" : request}
    )

@app.get("/adminLogin")
def adminLogin(request: Request):
    return templates.TemplateResponse(
        "adminLogin.html" , {"request" : request}
    )

@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse(
        "login1.html" , {"request" : request}
    )


@app.get("/adminSignup")
def adminLogin(request: Request):
    return templates.TemplateResponse(
        "adminSignup.html" , {"request" : request}
    )
