from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.json import JsonResponse
from django.template import loader


from .models import User


def index(request):
  users = User.objects.order_by('name')
  template = loader.get_template('demo/index.html')
  context = {
    'all_users': users
  }
  return HttpResponse(template.render(context, request))


def getUserCity(request):
  if request.method == 'GET':
    # extract the id from the parameters
    id = request.GET.get('id')
    # lookup the user
    user = User.objects.get(pk=id)

    print(user)
    print(user.city)

    # return the user's city
    return JsonResponse({ 'city': user.city })