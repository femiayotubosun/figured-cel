from django.http.response import HttpResponse
from channels.layers import get_channel_layer
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/index.html",
    {"room_name": "broadcast"})

from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications_broadcast", {
            'type': 'send_notification',
            'message': 'Notification',
        }
    )
    return HttpResponse("done")