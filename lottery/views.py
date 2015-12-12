from django.views.generic import ListView
from django.utils.timezone import now

from lottery.models import Lottery


class AvailableLotteries(ListView):
    context_object_name = "lotteries"

    def get_queryset(self):
        now_ts = now()
        return Lottery.objects.filter(
            opening_datetime__lte=now_ts,
            closing_datetime__gte=now_ts,
        ).order_by("opening_datetime")
