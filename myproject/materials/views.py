# materials/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Material, File
from .forms import MaterialForm, FileForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url="/users/login/")
def material_new(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save()
            for category in ['lectures', 'classes', 'labs', 'projects']:
                for file in request.FILES.getlist(f'{category}_files'):
                    File.objects.create(material=material, category=category, file=file)
            return redirect('materials:list')
    else:
        form = MaterialForm()
    return render(request, 'materials/material_new.html', {'form': form})

@user_passes_test(is_admin, login_url="/users/login/")
def material_update(request, slug):
    material = get_object_or_404(Material, slug=slug)
    if request.method == 'POST':
        for category in ['lectures', 'classes', 'labs', 'projects']:
            for file in request.FILES.getlist(f'{category}_files'):
                File.objects.create(material=material, category=category, file=file)
        return redirect('materials:page', slug=material.slug)
    return render(request, 'materials/material_update.html', {'material': material})

@login_required(login_url="/users/login/")
def materials_list(request):
    materials = Material.objects.all().order_by('-date')
    return render(request, 'materials/materials_list.html', {'materials': materials})

@login_required(login_url="/users/login/")
def material_page(request, slug):
    material = get_object_or_404(Material, slug=slug)
    files = material.files.all()
    return render(request, 'materials/material_page.html', {'material': material, 'files': files})

@user_passes_test(is_admin, login_url="/users/login/")
def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    material_slug = file.material.slug
    file.delete()
    return redirect('materials:page', slug=material_slug)

@user_passes_test(is_admin, login_url="/users/login/")
def delete_material(request, slug):
    material = get_object_or_404(Material, slug=slug)
    material.delete()
    return redirect('materials:list')
