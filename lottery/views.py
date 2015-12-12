from django.views.generic import ListView

from lottery.models import Lottery


class AvailableLotteries(ListView):
    context_object_name = "lotteries"

    def get_queryset(self):
        return Lottery.open_lotteries.all()
