from celery import shared_task
from channels.layers import get_channel_layer

@shared_task(bind=True)
def test_func(self):
    channel_layer = get_channel_layer()
    channel_layer.group_send(
        "notifications_broadcast", {
            'type': 'send_notification',
            'message': 'Notification',
        }
    )
    return "Done"