from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from webui.deps import render

router = APIRouter()

@router.get("/settings/theme", response_class=HTMLResponse)
async def theme_page(request: Request):
    wallpaper_url = request.session.get("wallpaper_url", "")
    return render(request, "settings/theme.html", wallpaper_url=wallpaper_url)

@router.post("/settings/theme")
async def save_theme(request: Request, wallpaper_url: str = Form(...)):
    request.session["wallpaper_url"] = wallpaper_url
    return render(request, "settings/theme.html", wallpaper_url=wallpaper_url)

@router.post("/settings/theme/delete")
async def delete_theme(request: Request):
    request.session.pop("wallpaper_url", None)
    return render(request, "settings/theme.html", wallpaper_url="")
