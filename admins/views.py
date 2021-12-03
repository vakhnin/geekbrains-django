# Create your views here.
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import ShopUser


# Create your views here.
from products.models import ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': ShopUser.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, pk):
    user_select = ShopUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = ShopUser.objects.get(pk=pk)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, pk):
    pass
