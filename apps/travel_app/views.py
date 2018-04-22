from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users
from .models import Trips
import bcrypt

def index ( request ):
	# if 'user' in request.session:
	# 	me = request.session['user']['id']
	# 	context = {
	# 		'your_trips': Travel.objects.filter(planned_trip=me),
	# 		'all_trips': Travel.objects.exclude(planned_trip=me).exclude(joined_trip=currentUser),
	# 		'joined_trips': Users.objects.get(id=me).joined.all()
	# 	}
	# 	return render(request,'login_app/travel.html',context)
	
	print "index route is working"
	return render( request, "travel_app/index.html")

def login(request):
	
	errors = Users.objects.login_validator(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		print 'we hit this due to invalid email'
		return redirect( '/')
	# session logic goes here
	request.session.modified = True
	request.session['email'] = request.POST['email']
	print '############# we hit success'
	return render(request,'travel_app/travels.html')
	

def register(request):
	if request.method == 'POST':
		print "we hit register Post"
	errors = Users.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect("/")
		

	else:
		users = Users()
		users.first_name = request.POST['first_name']
		users.last_name = request.POST['last_name']
		users.email = request.POST['email']
		users.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		users.save()
		request.session.modified = True
		request.session['email'] = request.POST['email']
		print '############# we hit success'
		return render(request,'travel_app/travels.html')

# def travel(request):
# 	print "travel funcition"
# 	return render(request,'travel_app/travel.html')

def add(request):
	print "hit add route booyaah!"
	return render(request, 'travel_app/add.html')

def create_trip(request):
	# if request.method == 'POST':
	# 	print "############## we hit register Post ###########"
	# errors = Trips.objects.travel_validator(request.POST)
	# if len(errors):
	# 	for tag, error in errors.iteritems():
	# 		messages.error(request, error, extra_tags=tag)
	# 	return redirect("/")

	# else:
	trips = Trips.objects.create(
	# trips = Trips()
		destination = request.POST['destination'],
		description = request.POST['description'],
		start_date = request.POST['start_date'],
		end_date = request.POST['end_date'],
	# trips.trip_tripsned = request.session['email']
	# trips.adventures = request.session['email']
	# trips.save()
	)
	print "#############we hit this shit homie################ #blessed"
	return render(request,'travel_app/travels.html')







