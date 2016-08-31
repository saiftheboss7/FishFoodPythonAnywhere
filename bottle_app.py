from bottle import default_app, route, request, template, run, post, get, debug
@route('/')
def index():
    return template ('index')

@post('/result', method='POST')
def result():

	sumFish= float(request.forms.get("TotalFish"))
	fishRange= float(request.forms.get("FishRange"))
	select=request.forms.get("dropdownform")

	if select=="1":
		if 5000<=sumFish<=999999999:
			constant=0.00020
		if 4000<=sumFish<=4999:
			constant=0.00019
		if 3000<=sumFish<=3999:
			constant=0.00017
		if 2000<=sumFish<=2999:
			constant=0.00020
		if 1000<=sumFish<=1999:
			constant=0.00035
		if 800<=sumFish<=899:
			constant=0.00038
		if 500<=sumFish<=599:
			constant=0.00050
		if 400<=sumFish<=499:
			constant=0.00050
		if 300<=sumFish<=399:
			constant=0.00050
		if 100<=sumFish<=299:
			constant=0.00120
		if 75<=sumFish<=99:
			constant=0.00133
		if 50<=sumFish<=74:
			constant=0.00160
		if 40<=sumFish<=49:
			constant=0.00175
		if 25<=sumFish<=39:
			constant=0.00200
		if 15<=sumFish<=24:
			constant=0.00200
		if 0<=sumFish<=14:
			constant=0.00250

	if select=="2":
		if 5000<=sumFish<=8000:
			constant=.00020
		if 4000<=sumFish<=4999:
			constant=.00019
		if 3000<=sumFish<=3999:
			constant=.00017
		if 2000<=sumFish<=2999:
			constant=.00020
		if 1000<=sumFish<=1999:
			constant=0.00035
		if 800<=sumFish<=899:
			constant=.00038
		if 500<=sumFish<=599:
			constant=.00050
		if 400<=sumFish<=499:
			constant=.00050
		if 300<=sumFish<=399:
			constant=.00050
		if 100<=sumFish<=299:
			constant=.00120
		if 75<=sumFish<=99:
			constant=.00133
		if 50<=sumFish<=74:
			constant=.00160
		if 40<=sumFish<=49:
			constant=.00175
		if 25<=sumFish<=39:
			constant=.00200
		if 15<=sumFish<=24:
			constant=.00200
		if 10<=sumFish<=14:
			constant=.00250
		if 0<=sumFish<=9:
			constant=.00300

	if select=="3":
		if 1000<=sumFish<=150000:
			constant=.00011
		if 200<=sumFish<=999:
			constant=.00050
		if 100<=sumFish<=199:
			constant=.00050
		if 20<=sumFish<=99:
			constant=.00200
		if 2<=sumFish<=19:
			constant=0.01500

	if select=="4":
		if 20000<=sumFish<=150000:
			constant=.00001
		if 1000<=sumFish<=19999:
			constant=.00008
		if 500<=sumFish<=999:
			constant=.00014
		if 0<=sumFish<=499:
			constant=.00417

	if select=="5":
		if 20000<=sumFish<=150000:
			constant=.00002
		if 1000<=sumFish<=19999:
			constant=.00025
		if 500<=sumFish<=999:
			constant=.00030
		if 0<=sumFish<=499:
			constant=.01667

	if select=="6":
		if 11<=sumFish<=20 or sumFish>20:
			constant=.003
		if 9<=sumFish<=10:
			constant=.004
		if 7<=sumFish<=8:
			constant=.006
		if 5<=sumFish<=6:
			constant=.008
		if sumFish==4:
			constant=.01
		if sumFish==3:
			constant=.012
		if sumFish==2:
			constant=.015
		if sumFish==1:
			constant=.016

	if select=="7":
		if 0<=sumFish<=50000:
			constant=.0125

	if select=="8":
		if 5000<=sumFish<=7000:
			constant=.00004
		if 1000<=sumFish<=4999:
			constant=.00015
		if 300<=sumFish<=999:
			constant=.00033
		if 70<=sumFish<=299:
			constant=.00071
		if 50<=sumFish<=69:
			constant=.00060



	a=constant*fishRange
	newvar=format(a, '.2f')

	return template('output', name=newvar)




debug(True)
application = default_app()