from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from lottery.models import Lottery
from lottery.models import LotteryTicket
from .forms import LotteryTicketForm
from .utils import serialize_ticket


class AvailableLotteries(ListView):
    context_object_name = "lotteries"

    def get_queryset(self):
        return Lottery.open_lotteries.all()


class PlayLottery(LoginRequiredMixin, FormView):
    template_name="lottery/play_lottery.html"
    form_class = LotteryTicketForm
    success_url = reverse_lazy("main_page")

    def form_valid(self, form):
        ticket = LotteryTicket(
            lottery=self.lottery,
            player=self.request.user,
            ticket=serialize_ticket(form.cleaned_data["numbers"]),
        )
        return super(PlayLottery, self).form_valid(form)

    def dispatch(self, request, lottery_id, *args, **kwargs):
        self.lottery = get_object_or_404(Lottery.open_lotteries.all(), id=lottery_id)
        if request.user.lotteryticket_set.filter(lottery=self.lottery).exists():
            return redirect(self.success_url)
        return super(PlayLottery, self).dispatch(request, *args, **kwargs)
