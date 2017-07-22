from django.shortcuts import render
from requests import request as r1
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

fields=["category","name","phone","general_info","about","attire","bio","location","parking","hours","emails","website","description","company_overview","personal_info"]
fieldstring=','.join(fields)

@csrf_exempt
def home(request):
	return render(request, 'index.html',{'fields':fields})

@csrf_exempt
def post_data(request):
	if request.method=="POST":
		try:
			pageAccesstoken=request.POST.get("pageAccessToken",'')
			pageID=request.POST.get("pageID",'')
			header="OAuth "+pageAccesstoken
			fieldProperty=request.POST.get("fieldProperty",'')
			fieldPropertyValue=request.POST.get("fieldPropertyValue",'')
			data={}
			data[fieldProperty]=fieldPropertyValue
			response1=r1('POST',"https://graph.facebook.com/"+pageID,data=data,headers={"Authorization": header})
			response=json.dumps(response1.json())
			return HttpResponse(response)
		except:
			return HttpResponse("failure")
	return HttpResponse("invalid call")

@csrf_exempt
def get_data(request):
	if request.method=="POST":
		try:
			pageAccesstoken=request.POST.get("pageAccessToken",'')
			pageID=request.POST.get("pageID",'')
			header="OAuth "+pageAccesstoken
			response1=r1('GET',"https://graph.facebook.com/"+pageID+"?fields="+fieldstring,headers={"Authorization": header})
			response=json.dumps(response1.json())
			return HttpResponse(response)
		except:
			return HttpResponse('Some Error Occured')
	return HttpResponse("invalid call")
