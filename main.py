from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from controller.users import Users
from lib.checker import check_user

app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/", response_class=HTMLResponse)
def root(req:Request):
    return template.TemplateResponse("index.html",{"request":req}) 

@app.post("/", response_class=HTMLResponse)
def root(req:Request):
    return template.TemplateResponse("index.html",{"request":req}) 

@app.get("/signup", response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request":req})
'''
@app.get("/user", response_class=HTMLResponse)
def user(req: Request):
    #return template.TemplateResponse("users.html", {"request":req})
    return RedirectResponse("/") 
'''
@app.post("/user", response_class=HTMLResponse)
def user(req: Request, username: str = Form(), password_user: str = Form()):
    print ("Usuario    ", username)
    print ("Contraseña ", password_user) 
    verifica_user = check_user(username, password_user)
    if verifica_user:
        return template.TemplateResponse("users.html", { "request":req, "data_user":verifica_user })
    return RedirectResponse("/") 

@app.post("/data-processing")
def data_processing(firstname: str = Form(), lastname: str = Form(), username: str = Form(), country: str = Form(), password_user:str = Form()):
    data_user = {
            "firstname":firstname, 
            "lastname":lastname, 
            "username":username,
            "country":country,
            "password_user":password_user 
            }
    db = Users(data_user)
    db.create_user()
    return RedirectResponse("/") 
