from django.views import View
from django.http  import JsonResponse
from .models	  import *
import json

class MenuView(View):
	def get(self, request):
		menus = Menu.objects.all()
		result = []

		for menu in menus:
			result.append(menu.name)

		return JsonResponse({"result": result}, status = 200)

	def post(self, request):
		data = json.loads(request.body)
		Menu.objects.create(name=data["name"])

		return JsonResponse({"result" : "Created"}, status = 201)
