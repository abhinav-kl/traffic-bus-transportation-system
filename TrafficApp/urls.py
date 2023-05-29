"""Traffic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from TrafficApp import views

urlpatterns = [
    #### Web Module urls
    path('', views.login_access),
    path('logout', views.log_out),

    # admin section
    path('admin_home', views.admin_home),
    path('traffic_police', views.traffic_police_register),
    path('view_traffic_police', views.view_traffic_police),
    path('update_traffic_police/<id>', views.update_traffic_police),
    path('delete_traffic_police/<id>', views.delete_traffic_police),
    path('add_driver', views.driver_register),
    path('view_driver', views.view_driver),
    path('delete_driver/<id>', views.delete_driver),
    path('view_owners', views.view_owner),
    path('view_owner_request', views.view_owner_request),
    path('accept/<id>', views.accept_owner_request),
    path('reject/<id>/<lid>', views.reject_owner_request),
    path('bus_details', views.view_bus_details),
    path('block/<id>', views.block_bus),
    path('unblock/<id>', views.unblock_bus),
    path('delete_bus/<id>', views.delete_bus_details),
    path('add_routes', views.add_bus_routes),
    path('view_routes', views.view_routes),
    path('delete_routes/<id>', views.delete_routes),
    path('add_stops', views.add_bus_stops),
    path('view_stops', views.view_stops),
    path('delete_stops/<id>', views.delete_stops),
    path('view_feedback', views.view_feedback),

    #### Traffic Police Section
    path('traffic_police_home', views.traffic_police_home),
    path('traffic_view_drivers', views.police_view_drivers_details),
    path('add_blocks', views.add_traffic_blocks),
    path('view_blocks', views.view_traffic_blocks),
    path('delete_blocks/<id>', views.delete_traffic_blocks),
    path('traffic_view_bus', views.police_view_bus_details),
    path('View_complaint', views.view_complaints),
    path('send_reply/<id>', views.send_reply),
    path('traffic_view_rating', views.police_view_rating),

    #### Owner section
    path('owner_home', views.owner_home),
    path('registration', views.owner_registration),
    path('ajax_form_check', views.ajax_owner_reg),
    path('view_profile', views.owner_profile),
    path('edit_profile/<id>', views.edit_owner_profile),
    path('add_bus', views.add_bus),
    path('view_bus', views.view_bus),
    path('update_bus/<id>', views.update_bus_details),
    path('delete_bus_entry/<id>', views.delete_bus),
    path('Owner_view_routes', views.owner_view_routes),
    path('Owner_view_stops', views.owner_view_stops),
    path('time_allocation', views.bus_time_allocation),
    path('ajaxviewstops/<id>', views.dynamic_select_stops),
    path('view_time_allocation', views.view_bus_time_allocation),
    path('delete_time_allocation/<id>', views.delete_time_allocation),
    path('view_location', views.view_bus_locations),


    ##### Android Module urls
    path('login', views.android_login),

    ##### Driver Module
    path('view_traffic_block', views.android_view_blocks),
    path('driver_card', views.android_driver_card),
    path('location_service', views.location_service),

    ##### Passenger Module
    path('passenger_reg', views.android_passenger_registration),
    path('view_bus_stops', views.android_view_stop),
    path('routes', views.android_search_route),
    path('search_results', views.android_view_search_results),
    path('reg_complaint', views.android_register_complaint),
    path('view_reply', views.android_view_reply),
    path('feedback_rating', views.android_feedback_rating),
]
