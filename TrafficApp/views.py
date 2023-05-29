import datetime

from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from TrafficApp.models import *


# Create your views here.

def login_access(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        q = login.objects.filter(username=username, password=password)
        if q.exists():
            q = q[0]
            request.session['lid'] = q.id
            request.session['logout'] = 'true'
            if q.usertype == 'admin':
                return redirect('/admin_home')
            elif q.usertype == 'Traffic Police':
                return redirect('/traffic_police_home')
            elif q.usertype == 'Owner':
                return redirect('/owner_home')
            else:
                messages.info(request, "Request is Pending...")
                return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request, 'Login.html')


def log_out(request):
    request.session['logout'] = 'false'
    return redirect('/')


####### Admin section######


def admin_home(request):
    return render(request, 'Admin/Admin_index.html')


def traffic_police_register(request):
    if request.method == "POST":
        district = request.POST['textfield']
        control_room = request.POST['textfield2']
        username = request.POST['textfield4']
        password = request.POST['textfield3']
        obk = login()
        obk.username = username
        obk.password = password
        obk.usertype = 'Traffic Police'
        obk.save()
        obj = traffic_police()
        obj.district = district
        obj.control_room = control_room
        obj.login = obk
        obj.save()
        return redirect('/view_traffic_police')
    else:
        return render(request, 'Admin/Add_TrafficPolice.html')


def view_traffic_police(request):
    reg = traffic_police.objects.all()
    return render(request, 'Admin/View_TrafficPolice.html', {'TrafficPolice': reg})


def update_traffic_police(request, id):
    if request.method == "POST":
        district = request.POST['textfield']
        control_room = request.POST['textfield2']
        traffic_police.objects.filter(id=id).update(district=district, control_room=control_room)
        return redirect('/view_traffic_police')
    else:
        reg = traffic_police.objects.get(id=id)
        return render(request, 'Admin/Update_TrafficPolice.html', {'TrafficPolice': reg})


def delete_traffic_police(request, id):
    traffic_police.objects.filter(id=id).delete()
    return redirect('/view_traffic_police')


def driver_register(request):
    if request.method == "POST":
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        image = request.FILES['fileField']
        fs = FileSystemStorage()
        fs.save(r"D:\Bus Traffic Management\Traffic\TrafficApp\static\Driver_Image\\" + date + '.jpg', image)
        path = "/static/Driver_Image/" + date + '.jpg'
        name = request.POST['textfield']
        age = request.POST['textfield2']
        driver_license = request.FILES['fileField2']
        fs.save(r"D:\Bus Traffic Management\Traffic\TrafficApp\static\License_image\\" + date + '.jpg', driver_license)
        path_license = "/static/License_image/" + date + '.jpg'
        phone = request.POST['textfield3']
        email = request.POST['textfield4']
        password = request.POST['textfield6']
        obk = login()
        obk.username = email
        obk.password = password
        obk.usertype = 'Driver'
        obk.save()
        obj = drivers()
        obj.image = str(path)
        obj.name = name
        obj.age = age
        obj.licenses = str(path_license)
        obj.phone = phone
        obj.email = email
        obj.login = obk
        obj.save()
        return redirect('/view_driver')
    else:
        return render(request, 'Admin/Add_Driver.html')


def view_driver(request):
    reg = drivers.objects.all()
    return render(request, 'Admin/View_Driver.html', {'Driver': reg})


def delete_driver(request, id):
    drivers.objects.filter(id=id).delete()
    login.objects.filter(id=id).delete()
    return redirect('/view_driver')


def view_owner(request):
    reg = owners.objects.filter(login__usertype='Owner')
    return render(request, 'Admin/View_Owners.html', {'Owners': reg})


def view_owner_request(request):
    reg = owners.objects.filter(login__usertype='pending')
    return render(request, 'Admin/View_OwnersRequest.html', {'Owners': reg})


def accept_owner_request(request, id):
    login.objects.filter(id=id).update(usertype='Owner')
    return redirect('/view_owners')


def reject_owner_request(request, id, lid):
    owners.objects.filter(id=id).delete()
    login.objects.filter(id=lid).delete()
    return redirect('/view_owner_request')


def view_bus_details(request):
    reg = bus.objects.all()
    return render(request, 'Admin/View_Bus.html', {'Bus_Details': reg})


def block_bus(request, id):
    bus.objects.filter(id=id).update(status='Blocked')
    return redirect('/bus_details')


def unblock_bus(request, id):
    bus.objects.filter(id=id).update(status='Running')
    return redirect('/bus_details')


def delete_bus_details(request, id):
    bus.objects.filter(id=id).delete()
    return redirect('/bus_details')


def add_bus_routes(request):
    if request.method == "POST":
        start = request.POST['textfield']
        end = request.POST['textfield2']
        obj = bus_routes()
        obj.start = start
        obj.end = end
        obj.save()
        return redirect('/view_routes')
    else:
        return render(request, 'Admin/Add_Routes.html')


def view_routes(request):
    reg = bus_routes.objects.all()
    return render(request, 'Admin/View_Routes.html', {'Routes': reg})


def delete_routes(request, id):
    bus_routes.objects.filter(id=id).delete()
    return redirect('/view_routes')


def add_bus_stops(request):
    if request.method == "POST":
        stops = request.POST['textfield']
        route = request.POST['select']
        obj = bus_stops()
        obj.stop = stops
        obj.route_id_id = route
        obj.save()
        return redirect('/view_stops')
    else:
        reg = bus_routes.objects.all()
        return render(request, 'Admin/Add_Stops.html', {'busRoutes': reg})


def view_stops(request):
    reg = bus_stops.objects.all()
    return render(request, 'Admin/View_Stops.html', {'Stops': reg})


def delete_stops(request, id):
    bus_stops.objects.filter(id=id).delete()
    return redirect('/view_stops')


def view_feedback(request):
    reg = feedback_ratings.objects.all()
    return render(request, 'Admin/View_Feedback.html', {'Feedback': reg})


#### Admin section end


####### Traffic Police Section #########

def traffic_police_home(request):
    lid = request.session['lid']
    reg = traffic_police.objects.get(login=lid)
    return render(request, 'Traffic_Police/TrafficPolice_index.html', {'traffic_police': reg})


def police_view_drivers_details(request):
    reg = drivers.objects.all()
    return render(request, 'Traffic_Police/View_Driver.html', {'viewDrivers': reg})


def police_view_bus_details(request):
    reg = bus.objects.all()
    return render(request, 'Traffic_Police/View_Bus.html', {'viewBusDetails': reg})


def view_complaints(request):
    reg = complaints.objects.all()
    return render(request, 'Traffic_Police/View_Complaint.html', {'complaints': reg})


def send_reply(request, id):
    if request.method == "POST":
        reply = request.POST['textarea']
        reply_date = datetime.datetime.now().strftime('%Y-%m-%d')
        complaints.objects.filter(id=id).update(reply=reply, reply_date=reply_date)
        return redirect('/View_complaint')
    else:
        reg = complaints.objects.get(id=id)
        return render(request, 'Traffic_Police/Send_Reply.html', {'reg_complaint': reg})


def add_traffic_blocks(request):
    if request.method == "POST":
        date = datetime.datetime.now().strftime('%d-%m-%y')
        route = request.POST['select']
        stop = request.POST['select2']
        obj = traffic_blocks()
        obj.date = date
        obj.route_id_id = route
        obj.stop_id_id = stop
        obj.save()
        return redirect('/view_blocks')
    else:
        bus_route = bus_routes.objects.all()
        bus_stop = bus_stops.objects.all()
        return render(request, 'Traffic_Police/Add_Blocks.html', {'blockRoute': bus_route, 'blockStop': bus_stop})


def view_traffic_blocks(request):
    reg = traffic_blocks.objects.all()
    return render(request, 'Traffic_Police/View_Block.html', {'viewBlocks': reg})


def delete_traffic_blocks(request, id):
    traffic_blocks.objects.filter(id=id).delete()
    return redirect('/view_blocks')


def police_view_rating(request):
    reg = feedback_ratings.objects.all()
    return render(request, 'Traffic_Police/View_Rating.html', {'busRatings': reg})


#### Traffic Police section ends

#### Owner section

def owner_home(request):
    lid = request.session['lid']
    reg = owners.objects.get(login=lid)
    return render(request, 'Bus_Owner/Owner_index.html', {'owner': reg})


def owner_registration(request):
    if request.method == "POST":
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        image = request.FILES['fileField']
        fs.save(r'D:\Bus Traffic Management\Traffic\TrafficApp\static\Owner_Image\\' + date + '.jpg', image)
        path = "/static/Owner_Image/" + date + '.jpg'
        name = request.POST['textfield']
        age = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        address = request.POST['textarea']
        place = request.POST['textfield5']
        post = request.POST['textfield6']
        pin = request.POST['textfield7']
        phone = request.POST['textfield8']
        associationID = request.POST['textfield3']
        email = request.POST['textfield4']
        password = request.POST['textfield9']
        qry = login.objects.filter(username=email)
        if qry.exists():
            messages.warning(request, "Current Email is Exists")
            return redirect('/registration')
        else:
            obk = login()
            obk.username = email
            obk.password = password
            obk.usertype = 'pending'
            obk.save()
            obj = owners()
            obj.image = str(path)
            obj.name = name
            obj.age = age
            obj.gender = gender
            obj.address = address
            obj.place = place
            obj.post = post
            obj.pin = pin
            obj.phone = phone
            obj.association_ID = associationID
            obj.email = email
            obj.login = obk
            obj.save()
            return redirect('/')
    else:
        return render(request, 'Bus_Owner/Owner_Registration.html')


def ajax_owner_reg(request):
    if request.method == "POST":
        pname = request.POST['type']
        qry = login.objects.filter(username=pname)
        if qry.exists():

            return JsonResponse({'status': 'no'})
        else:
            return JsonResponse({'status': 'ok'})


def owner_profile(request):
    lid = request.session['lid']
    reg = owners.objects.get(login=lid)
    return render(request, 'Bus_Owner/Owner_Profile.html', {'Profile': reg})


def edit_owner_profile(request, id):
    if request.method == "POST":
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        image = request.FILES['fileField']
        fs.save(r'D:\Bus Traffic Management\Traffic\TrafficApp\static\Owner_Image\\' + date + '.jpg', image)
        path = "/static/Owner_Image/" + date + '.jpg'
        name = request.POST['textfield']
        address = request.POST['textarea']
        age = request.POST['textfield2']
        gender = request.POST['RadioGroup1']
        place = request.POST['textfield3']
        post = request.POST['textfield4']
        pin = request.POST['textfield5']
        phone = request.POST['textfield7']
        assID = request.POST['textfield6']
        owners.objects.filter(id=id).update(image=str(path), name=name, address=address, age=age, gender=gender,
                                            place=place, post=post, pin=pin, phone=phone, association_ID=assID)
        return redirect('/view_profile')
    else:
        lid = request.session['lid']
        reg = owners.objects.get(login=lid)
        return render(request, 'Bus_Owner/OwnerEdit_Profile.html', {'Profile': reg})


def add_bus(request):
    if request.method == "POST":
        bus_name = request.POST['textfield']
        registration = request.POST['textfield2']
        route = request.POST['select']
        driver = request.POST['select2']
        obj = bus()
        obj.bus_name = bus_name
        obj.registration_number = registration
        obj.route_id_id = route
        obj.driver_id_id = driver
        obj.save()
        return redirect('/view_bus')
    else:
        driver = drivers.objects.all()
        reg = bus_routes.objects.all()
        return render(request, 'Bus_Owner/Add_Bus.html', {'busRoutes': reg, 'driver': driver})


def view_bus(request):
    reg = bus.objects.all()
    return render(request, 'Bus_Owner/View_Bus.html', {'Bus': reg})


def update_bus_details(request, id):
    if request.method == "POST":
        bus_name = request.POST['textfield']
        registration = request.POST['textfield2']
        route = request.POST['select']
        driver = request.POST['select2']
        bus.objects.filter(id=id).update(bus_name=bus_name, registration_number=registration, route_id=route,
                                         driver_id=driver)
        return redirect('/view_bus')
    else:
        bus_details = bus.objects.get(id=id)
        route = bus_routes.objects.all()
        driver = drivers.objects.all()
        return render(request, 'Bus_Owner/Update_Bus_info.html',
                      {'updateBus': bus_details, 'route': route, 'driver': driver})


def delete_bus(request, id):
    bus.objects.filter(id=id).delete()
    return redirect('/view_bus')


def owner_view_routes(request):
    reg = bus.objects.all()
    return render(request, 'Bus_Owner/View_Routes.html', {'viewRoutes': reg})


def owner_view_stops(request):
    reg = bus_stops.objects.all()
    return render(request, 'Bus_Owner/View_Stops.html', {'viewStops': reg})


def bus_time_allocation(request):
    if request.method == "POST":
        bus_name = request.POST['select']
        stop = request.POST['select2']
        arrival_time = request.POST['textfield']
        departure_time = request.POST['textfield2']
        obj = time_allocation()
        obj.bus_id_id = bus_name
        obj.stop_id_id = stop
        obj.arrival_time = arrival_time
        obj.departure_time = departure_time
        obj.save()
        return redirect('/view_time_allocation')
    else:
        reg = bus.objects.all()
        stop_name = bus_stops.objects.all()
        return render(request, 'Bus_Owner/Arrival_Time.html', {'busName': reg, 'stopName': stop_name})


def dynamic_select_stops(request, id):
    reg = bus_stops.objects.filter(route_id=id)
    return render(request, 'Bus_Owner/ajaxviewstops.html', {'eid': reg})


def view_bus_time_allocation(request):
    reg = time_allocation.objects.all()
    return render(request, 'Bus_Owner/View_TimeAllocation.html', {'timeAllocation': reg})


def delete_time_allocation(request, id):
    time_allocation.objects.filter(id=id).delete()
    return redirect('/view_time_allocation')


def view_bus_locations(request):
    reg = bus.objects.all()
    return render(request, 'Bus_Owner/Track_BusLocation.html', {'location': reg})


#### Owner section end

########### Android Module ###########

def android_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        q = login.objects.filter(username=username, password=password)
        if q.exists():
            q = q[0]
            if q.usertype == 'Driver':
                driver = drivers.objects.get(login=str(q.id))
                return JsonResponse(
                    {'status': 'ok', 'type': q.usertype, 'lid': q.id, 'name': driver.name, 'phone': driver.phone,
                     'email': driver.email, 'image': driver.image})
            else:
                return JsonResponse(
                    {'status': 'ok', 'type': q.usertype, 'lid': q.id})
        else:
            return JsonResponse({'status': "Not found"})


#### Driver Section

def android_view_blocks(request):
    if request.method == "POST":
        lid = request.POST['id']
        driver = drivers.objects.get(login=lid)
        routes = bus.objects.get(driver_id=driver)
        route_id = bus_routes.objects.get(id=routes.route_id.id)  # passing the primary key value to get data from table
        obj = traffic_blocks.objects.filter(route_id=route_id)
        ar = []
        for i in obj:
            ar.append({'id': i.id, 'date': i.date, 'route_id_id': i.route_id.start, 'route_id': i.route_id.end,
                       'stop_id_id': i.stop_id.stop})
        return JsonResponse({'status': 'ok', 'data': ar})


def location_service(request):
    if request.method == "POST":
        lid = request.POST['id']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        driver = drivers.objects.get(login=lid)
        bus_id = bus.objects.get(driver_id=driver)
        bus.objects.filter(id=bus_id.id).update(latitude=latitude, longitude=longitude)
        return JsonResponse({'status': 'ok'})


def android_driver_card(request):
    if request.method == "POST":
        lid = request.POST['lid']
        obj = drivers.objects.get(login=lid)
        return JsonResponse({'status': 'ok', 'id': obj.id, 'name': obj.name, 'phone': obj.phone, 'email': obj.email,
                             'image': obj.image})


##### Driver section end
##### Passenger section

def android_passenger_registration(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        obk = login()
        obk.username = email
        obk.password = password
        obk.usertype = 'Passenger'
        obk.save()
        obj = passengers()
        obj.name = name
        obj.email = email
        obj.phone = phone
        obj.login = obk
        obj.save()
        return JsonResponse({'status': 'ok'})


def android_search_route(request):
    s = request.POST['start']
    e = request.POST['end']
    obj = bus.objects.filter(route_id__start__contains=s, route_id__end__contains=e)
    arr = []
    for i in obj:
        arr.append({'id': i.id, 'bus': i.bus_name, 'route_start': i.route_id.start, 'route_end': i.route_id.end,
                    "rid": i.route_id_id})
    return JsonResponse({'status': 'ok', 'data': arr})


def android_view_search_results(request):
    if request.method == "POST":
        obj = bus.objects.all()
        arr = []
        for i in obj:
            arr.append({'id': i.id, 'bus': i.bus_name, 'route_start': i.route_id.start, 'route_end': i.route_id.end,
                        'rid': i.route_id_id})
        return JsonResponse({'status': 'ok', 'data': arr})


def android_view_stop(request):
    if request.method == "POST":
        route_id = request.POST['rid']
        obj = time_allocation.objects.filter(stop_id__route_id=route_id)
        ar = []
        for i in obj:
            ar.append({'id': i.id, 'stop': i.stop_id.stop, 'route_start': i.bus_id.route_id.start,
                       'route_end': i.bus_id.route_id.end, 'arrival': i.arrival_time, 'departure': i.departure_time,
                       'lati': i.bus_id.latitude, 'longi': i.bus_id.longitude})
        return JsonResponse({'status': 'ok', 'data': ar})


def android_register_complaint(request):
    if request.method == "POST":
        lid = request.POST['id']
        bid = request.POST['b_id']
        date = datetime.datetime.now().strftime('%d-%m-%Y')
        complaint = request.POST['complaints']
        obj = complaints()
        obj.complaint = complaint
        obj.complaint_date = date
        obj.passenger_id_id = lid
        obj.bus_id_id = bid
        obj.reply = 'Pending...'
        obj.save()
        return JsonResponse({'status': 'ok'})


def android_view_reply(request):
    if request.method == "POST":
        lid = request.POST['id']
        obj = complaints.objects.filter(passenger_id_id=lid)
        ar = []
        for i in obj:
            ar.append(
                {'id': i.id, 'b_id': i.bus_id.bus_name, 'complaints': i.complaint, 'complaint_date': i.complaint_date,
                 'reply': i.reply,
                 'reply_date': i.reply_date})
        return JsonResponse({'status': 'ok', 'data': ar})


def android_feedback_rating(request):
    if request.method == "POST":
        lid = request.POST['id']
        bus_id = request.POST['bus_id']
        feedback = request.POST['feedback']
        rating = request.POST['rating']
        date = datetime.datetime.now().strftime('%d-%m-%Y')
        passenger_id = passengers.objects.get(login=lid)
        obj = feedback_ratings()
        obj.feedback = feedback
        obj.rating = rating
        obj.date = date
        obj.passenger_id = passenger_id
        obj.bus_id_id = bus_id
        obj.save()
        return JsonResponse({'status': 'ok'})

        ##### Passenger section end
