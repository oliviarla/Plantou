from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Plant.models import Plant, User


#index 페이지를 보여줌
def index(request):
    return render(request, 'Plant/index.html')

# index 페이지에서 받아온 데이터를 바탕으로 User 객체를 생성
def save_user(request):
    if request.method == 'POST':
        User.objects.create(
            h_sunlight=request.POST.get('h_sunlight', ''),
            h_temp=request.POST.get('h_temp', ''),
            desired_size=request.POST.get('desired_size', '')
        )
        return redirect('recommend')
    return render(request, 'Plant/index.html')


# user의 정보를 바탕으로 적절한 plant 데이터를 불러옴
def recommend(request):
    user = User.objects.order_by('-user_id').first()
    result = Plant.objects.filter(size=user.desired_size).get()
    '''
    plants = Plant.objects.all()
    for plant in plants:
        if str(plant.size) == str(user.desired_size):
            # and plant.g_temp-5 <= user.h_temp <= plant.g_temp+5 and
            # plant.g_sunlight-5 <= user.h_sunlight <= plant.g_sunlight+5:
            result = plant
            break
        else:
            return HttpResponse("not matching")
    '''
    return render(request, 'Plant/recommend.html', {'result': result})


# plantCreate page를 불러옴
def plantCreate(request):
    return render(request, 'Plant/plantCreate.html')


# plantCreate 페이지에서 받아온 데이터를 기반으로 plant 객체 생성
def Create_Plant(request):
    if request.method == 'POST':
        Plant.objects.create(
            name=request.POST.get('name', ''),
            g_sunlight=request.POST.get('g_sunlight', ''),
            water=request.POST.get('water', ''),
            g_temp=request.POST.get('g_temp', ''),
            size=request.POST.get('size', '')
        )
        return redirect('index')
    return render(request, 'Plant/plantCreate.html')
