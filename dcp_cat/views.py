from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def quiz_cat_1(request):
    return render(request, 'quiz_cat_1.html')

def quiz_cat_2(request):
    return render(request, 'quiz_cat_2.html')

def quiz_cat_3(request):
    return render(request, 'quiz_cat_3.html')

def quiz_cat_4(request):
    return render(request, 'quiz_cat_4.html')

def quiz_cat_5(request):
    return render(request, 'quiz_cat_5.html')

def test_result_cat(request):
    return render(request, 'test_result_cat.html')