from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import FormView

from lottery.models import Lottery
from lottery.models import LotteryTicket
from .forms import LotteryTicketForm
from .utils import serialize_ticket


def main_page(request):
    context = {"player_tickets": [], "lotteries": Lottery.open_lotteries.all()}
    if request.user.is_authenticated():
        player_tickets = request.user.lotteryticket_set.select_related().all()
        context["player_tickets"] = player_tickets
        context["lotteries"] = Lottery.open_lotteries.exclude(
            id__in=[ticket.lottery.id for ticket in player_tickets],
        )
    return render(request, template_name="lottery/lottery_list.html", context=context)


class PlayLottery(FormView):
    template_name="lottery/play_lottery.html"
    form_class = LotteryTicketForm
    success_url = reverse_lazy("main_page")

    def form_valid(self, form):
        ticket = LotteryTicket(
            lottery=self.lottery,
            player=self.request.user,
            ticket=serialize_ticket(form.cleaned_data["numbers"]),
        )
        ticket.save()
        return super(PlayLottery, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, lottery_id, *args, **kwargs):
        self.lottery = get_object_or_404(Lottery.open_lotteries.all(), id=lottery_id)
        if request.user.lotteryticket_set.filter(lottery=self.lottery).exists():
            return redirect(self.success_url)
        return super(PlayLottery, self).dispatch(request, *args, **kwargs)
