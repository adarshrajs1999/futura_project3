from django.shortcuts import render


def test1(request):
    return render(request,'template1.html')
def test2(request):
    return render(request,'template2.html')