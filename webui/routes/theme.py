from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

@router.get("/settings/theme", response_class=HTMLResponse)
async def theme_page(request: Request):
    wallpaper_url = request.session.get("wallpaper_url", "")
    return templates.TemplateResponse("settings/theme.html", {
        "request": request,
        "wallpaper_url": wallpaper_url
    })

@router.post("/settings/theme")
async def save_theme(request: Request, wallpaper_url: str = Form(...)):
    request.session["wallpaper_url"] = wallpaper_url
    return templates.TemplateResponse("settings/theme.html", {
        "request": request,
        "wallpaper_url": wallpaper_url
    })

@router.post("/settings/theme/delete")
async def delete_theme(request: Request):
    request.session.pop("wallpaper_url", None)
    return templates.TemplateResponse("settings/theme.html", {
        "request": request,
        "wallpaper_url": ""
    })
