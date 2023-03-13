from django.shortcuts import render

# Create your views here.
def jinja_first(request):
    d={'Name':'SONU','age':20}
    return render(request,'jinja_first.html',context=d)