from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponseBadRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.http import require_POST

from .models import Composition
from .music_generator import generate_music_file

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def index(request):
    only = request.GET.get("only")
    compositions = Composition.objects.filter(user=request.user).order_by("-created_at")
    if only == "favorites":
        compositions = compositions.filter(favorite=True)
    return render(request, "composer/index.html", {"compositions": compositions, "only": only})

@login_required
def generate_music(request):
    if request.method != "POST":
        return redirect("home")

    style = request.POST.get("style", "Classical")
    prompt = (request.POST.get("prompt") or "").strip()
    try:
        duration_s = int(request.POST.get("duration", "12"))
    except ValueError:
        duration_s = 12

    rel_media_path = generate_music_file(style=style, prompt=prompt, duration_s=duration_s)

    # Save relative path to FileField (Django will serve via MEDIA_URL)
    comp = Composition.objects.create(
        user=request.user,
        title=f"{style}_AI_Song",
        style=style,
        file=rel_media_path,
    )
    return redirect("home")

@login_required
def download_music(request, comp_id):
    comp = Composition.objects.get(id=comp_id, user=request.user)
    return FileResponse(open(comp.file.path, "rb"), as_attachment=True)

@login_required
@require_POST
def toggle_favorite(request, comp_id):
    try:
        comp = Composition.objects.get(id=comp_id, user=request.user)
    except Composition.DoesNotExist:
        return HttpResponseBadRequest("Invalid composition")

    comp.favorite = not comp.favorite
    comp.save(update_fields=["favorite"])
    return redirect(request.META.get("HTTP_REFERER") or "home")
