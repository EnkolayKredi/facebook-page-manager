from flask import *
from requests import request as r1
app=Flask(__name__)

fields=["category","name","phone","general_info","about","attire","bio","location","parking","hours","emails","website","description","company_overview","personal_info"]
fieldstring=','.join(fields)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/purana')
def purana():
	return render_template("home.html")

@app.route('/post_data',methods=["POST"])
def post_data():
	if request.method=="POST":
		try:
			pageAccesstoken=request.form.get("pageAccessToken",'')
			pageID=request.form.get("pageID",'')
			header="OAuth "+pageAccesstoken
			fieldProperty=request.form.get("fieldProperty",'')
			fieldPropertyValue=request.form.get("fieldPropertyValue",'')
			data={}
			if fieldProperty=="emails":
				x=[fieldPropertyValue]
				data[fieldProperty]=str(x)
				# data=json.dump(data)
			else:
				data[fieldProperty]=fieldPropertyValue
			print(data)
			response1=r1('POST',"https://graph.facebook.com/"+pageID,data=data,headers={"Authorization": header})
			response=json.dumps(response1.json())
			return (response)
		except:
			return ("failure")
	return ("invalid call")

@app.route('/get_data',methods=["POST"])
def get_data():
	if request.method=="POST":
		try:
			pageAccesstoken=request.form.get("pageAccessToken",'')
			pageID=request.form.get("pageID",'')
			header="OAuth "+pageAccesstoken
			response1=r1('GET',"https://graph.facebook.com/"+pageID+"?fields="+fieldstring,headers={"Authorization": header})
			response=json.dumps(response1.json())
			return (response)
		except:
			return ('Some Error Occured')
	return ("invalid call")


if __name__=="__main__":
    app.run(debug=True)