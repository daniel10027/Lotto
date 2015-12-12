from django.contrib import admin

from .models import Lottery
from .models import LotteryTicket

admin.site.register(Lottery)
admin.site.register(LotteryTicket)
