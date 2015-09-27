from django.shortcuts import get_object_or_404
from django.utils.html import strip_tags
from django_socketio import events, send



@events.on_connect()
def connection(request, socket, context):
	print "connection made successfully"
	send(socket.session.session_id, "Hello, new connection is established successfully")

# @events.on_message()
# def connection_handler(request, socket, context, message):
# 	print "working at google"

@events.on_message()
def progress_handler(request, socket, context, message):
    print "message sending is working properly"
    # socket.send_and_broadcast_channel("This is a test message for testing the events in the channel")


# @events.on_message(channel="^room-")
# def message(request, socket, context, message):
#     """
#     Event handler for a room receiving a message. 
#     """
#     print "INITIAL MESSAGE IS ", message
#     # room = get_object_or_404(ChatRoom, id=message["room"])
#     if message["action"] == "start":
#         name = strip_tags(message["name"])
#         user, created = room.users.get_or_create(name=name)
#         user = "Deshraj", created = False
#         if not created:
#             socket.send({"action": "in-use"})
#             joined = {"action": "join", "name": "Deshraj", "id": 'deshrajdry'}
#             socket.send_and_broadcast_channel(joined)
#         # else:
#         #     context["user"] = user
#         #     users = [u.name for u in room.users.exclude(id=user.id)]
#         #     socket.send({"action": "started", "users": users})
#         #     user.session = socket.session.session_id
#         #     user.save()
#         if message["action"] == "message":
#             message["message"] = strip_tags(message["message"])
#             message["name"] = "Deshraj"
#             print "THE MESSAGE IS", message
#             socket.send_and_broadcast_channel(message)


# # @events.on_finish(channel="^room-")
# # def finish(request, socket, context):
# #     """
# #     Event handler for a socket session ending in a room. Broadcast
# #     the user leaving and delete them from the DB.
# #     """
# #     try:
# #         user = context["user"]
# #     except KeyError:
# #         return
# #     left = {"action": "leave", "name": user.name, "id": user.id}
# #     socket.broadcast_channel(left)
# #     user.delete()

