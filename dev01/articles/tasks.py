from celery import shared_task
from core.celery import app
import redis
import json
from django.conf import settings
from actions.models import Tracking

redis_pub = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


@app.task(bind=True)
def notification_about_new_post(self, post, id, author):

    ul = Tracking.objects.filter(to_user=author).values_list("from_user", flat=True)
    for rec in ul:
        redis_pub.hset(rec, id, post)
