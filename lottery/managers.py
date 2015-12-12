from django.db import models
from django.utils.timezone import now

class OpenLotteryManager(models.Manager):
    def get_queryset(self):
        now_ts = now()
        return super(OpenLotteryManager, self).get_queryset().filter(
            opening_datetime__lte=now_ts,
            closing_datetime__gte=now_ts,
        )
