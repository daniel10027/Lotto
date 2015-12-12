from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from lottery.models import Lottery
from .forms import LotteryTicketForm


class AvailableLotteries(ListView):
    context_object_name = "lotteries"

    def get_queryset(self):
        return Lottery.open_lotteries.all()


def play_lottery(request, lottery_id):
    lottery = get_object_or_404(Lottery.open_lotteries.all(), id=lottery_id)

    if request.method == "GET":
        return render(
            request,
            template_name="lottery/play_lottery.html",
            context={"form": LotteryTicketForm()},
        )

    lform = LotteryTicketForm(request.POST)
    if not lform.is_valid():
        return render(
            request,
            template_name="lottery/play_lottery.html",
            context={"form": lform},
        )

    return render(
        request,
        template_name="lottery/play_lottery.html",
        context={},
    )

