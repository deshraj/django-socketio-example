from django.shortcuts import render_to_response, render
from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import broadcast, broadcast_channel, NoSocket, send
from django.http import HttpResponse
from sampleapp.events import *
from time import sleep
import json
def home(request):
	'''
	Home page view for socket connections 
	'''
	# r.publish('chat', json.dumps({'message': 'Hello Deshraj', 'socketid': 'qwertyuiop'}))	
	# a = r.publish('chat', json.dumps({'message': 'Hello Deshraj', 'socketid': 'qwertyuiop'}))
	# print "value of redis is ", a
	# broadcast_channel({'message': 'Hello World'}, channel = 'progress')
	# send({'message': 'Hello World'})
	return render_to_response('index.html')


def message(request, template="message.html"):
	# while True:
	try:
		pass
		# send(session.session_id, "{'hello':'world'}")
		# send(socket.session.session_id, "deshraj is great")
	except NoSocket, e:
		print e
		# sleep(1)
	context = {"rooms": ""}
	# if request.method == "POST":s
	# 	room = request.POST["room"]
	# 	print "room is ", room
	# 	data = {"action": "system", "message": request.POST["message"]}
	# 	# try:
	# 	if room:
	# 		print "!!!!!!!!!!!   inside if condition !!!!!!!!!!!"
	# 		broadcast_channel(data, channel="room-" + room)
	# 	else:
	# 		print "!!!!!!!!!!!   inside else condition !!!!!!!!!!!"
	# 		broadcast(data)
	# 	# except NoSocket, e:
	# 	# 	print "no sockets found. Throwing an exception"
	# 	# 	context["message"] = e
	# else:
	# 	context["message"] = "Message sent"
	return render(request, template, context)