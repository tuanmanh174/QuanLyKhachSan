from django.http import Http404, HttpResponse
from Home.models import SanPham
from django.shortcuts import render
# Create your views here.

def Index(request):
    response = HttpResponse()
    response.write('<h1>Hello World</h1>')
    return response


def ShowProduct(request):
    try:
        products = SanPham.objects.all()
    except SanPham.DoesNotExist:
        raise Http404("Sản phẩm không tồn tại")
    return render(request, 'showproduct.html', {'products': products})


def ProductDetail(request, id):
    try:
        products = SanPham.objects.get(pk=id)
    except SanPham.DoesNotExist:
        raise Http404("Sản phẩm không tồn tại")
    return render(request, 'productdetail.html', {'products': products})

def ListTheGioi(request):
    try:
        listthegioi = SanPham.objects.all()
    except SanPham.DoesNotExist:
        raise Http404("Sản phẩm không tồn tại")
    return render(request, 'showlistthegioi.html', {'listthegioi': listthegioi})