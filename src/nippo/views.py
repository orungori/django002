from django.shortcuts import render,get_object_or_404,redirect
from random import randint
from .models import NippoModel
from .forms import  NippoFormClass

# Create your views here.
from django.views.generic import ListView #インポート

class NippoListView(ListView): #クラス作成
    template_name = "nippo/nippo-list.html" #変数
    model = NippoModel #変数
def nippoDetailView(request,number):
    template_name = "nippo/nippo-detail.html"
    random_int=randint(1,10)
    ctx = {
        "random_number":random_int,
        "number":number,
    }
    return render(request,template_name,ctx)
def nippoUpdateFormView(request, pk):
    template_name = "nippo/nippo-form.html"
    obj = NippoModel.objects.get(pk=pk)
    initial_values = {"title": obj.title, "content":obj.content}
    form = NippoFormClass(request.POST or initial_values)
    ctx = {"form": form}
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj.title = title
        obj.content = content
        obj.save()
    return render(request, template_name, ctx)
def nippoDeleteView(request, pk):
    template_name = "nippo/nippo-delete.html"
    obj = get_object_or_404(NippoModel, pk=pk)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("nippo/nippo-list")
    return render(request, template_name, ctx)