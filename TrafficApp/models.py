from django.db import models



class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class traffic_police(models.Model):
    district = models.CharField(max_length=100)
    control_room = models.CharField(max_length=100)
    login = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class owners(models.Model):
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    association_ID = models.CharField(max_length=100)
    login = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class passengers(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    login = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class drivers(models.Model):
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    licenses = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    login = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class bus_routes(models.Model):
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)

class bus(models.Model):
    bus_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    owner_id = models.ForeignKey(owners, default=1, on_delete=models.CASCADE)
    route_id = models.ForeignKey(bus_routes, default=1, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(drivers, default=1, on_delete=models.CASCADE)

class bus_stops(models.Model):
    stop = models.CharField(max_length=100)
    route_id = models.ForeignKey(bus_routes, default=1, on_delete=models.CASCADE)

class traffic_blocks(models.Model):
    date = models.CharField(max_length=100)
    stop_id = models.ForeignKey(bus_stops, default=1, on_delete=models.CASCADE)
    route_id = models.ForeignKey(bus_routes, default=1, on_delete=models.CASCADE)

class time_allocation(models.Model):
    bus_id = models.ForeignKey(bus, default=1, on_delete=models.CASCADE)
    stop_id = models.ForeignKey(bus_stops, default=1, on_delete=models.CASCADE)
    arrival_time = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)

class complaints(models.Model):
    complaint = models.CharField(max_length=500)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=500)
    reply_date = models.CharField(max_length=100)
    bus_id = models.ForeignKey(bus, default=1, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(passengers, default=1, on_delete=models.CASCADE)

class feedback_ratings(models.Model):
    feedback = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    bus_id = models.ForeignKey(bus, default=1, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(passengers, default=1, on_delete=models.CASCADE)
