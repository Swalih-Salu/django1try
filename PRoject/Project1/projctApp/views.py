from django.shortcuts import render

# Create your views here.
def projct(r):
    return render(r,'index.html')
def contact(e):
    return render(e,'contact.html')
def destinations(q):
    return render(q,'destinations.html')
def elements(u):
    return render(u,'elements.html')
def news(s):
    return render(s,'news.html')