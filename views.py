from django.shortcuts import render
from requests import request as r1
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

fields=["name","phone","general_info","about","attire","bio","location","parking","hours","emails","website","description","company_overview","personal_info"]
# page_access_token="EAASq1zRIalQBABHWwfxeZCxKU45dPE4LLsO11Peldoazfntm0fyF4VdVA2TtfxskAsAXmdLLbT9OICTjzkLYEZCu9Kax2nNgmDq6eVEM8xrBvQShB7KEL5DB2ycZAFWMhsZCPD6wzAq7QdM1ONztBLK6rcIZCiZBli9mLkhJrip9Xaci8eqoQIZCJFZATlvSdN0rjT0pYZBUM4AZDZD"
# header="OAuth "+page_access_token
# pageid="168706986987778"
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
			print(fieldProperty,fieldPropertyValue)
			data={}
			data[fieldProperty]=fieldPropertyValue
			# print(data)
			response1=r1('POST',"https://graph.facebook.com/"+pageID,data=data,headers={"Authorization": header})
			response=json.dumps(response1.json())
			return HttpResponse(response)
		except:
			return HttpResponse("failure")
	return HttpResponse("invalid")

@csrf_exempt
def get_data(request):
	if request.method=="POST":
		# try:
		response1=r1('GET',"https://graph.facebook.com/"+pageid+"?fields="+fieldstring,headers={"Authorization": header})
		response=json.dumps(response1.json())
		# print(response)
		return HttpResponse(response)
		# except:
		# 	return HttpResponse('failure')
	return HttpResponse("invalid")
