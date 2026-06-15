from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from webui.deps import render

router = APIRouter()

@router.get("/settings/theme")
def theme_page(request: Request):
    wallpaper_url = request.session.get("wallpaper_url", "")
    return render(request, "settings/theme.html", wallpaper_url=wallpaper_url)

@router.post("/settings/theme")
def save_theme(request: Request, wallpaper_url: str = Form(...)):
    request.session["wallpaper_url"] = wallpaper_url
    return render(request, "settings/theme.html", wallpaper_url=wallpaper_url)

@router.post("/settings/theme/delete")
def delete_theme(request: Request):
    request.session.pop("wallpaper_url", None)
    return render(request, "settings/theme.html", wallpaper_url="")
