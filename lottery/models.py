from django.db import models
from lottery.managers import OpenLotteryManager
from django.conf import settings
from random import sample
from .utils import serialize_ticket


class Lottery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    opening_datetime = models.DateTimeField(
        help_text="time after which getting a ticket for this lottery is allowed",
    )
    closing_datetime = models.DateTimeField(
        help_text="time after which getting a ticket for this lottery is no longer allowed",
    )
    winner_ticket = models.CharField(
        max_length=200,
        help_text="Serialization of the winner ticket/selection of numbers",
        blank=True,
    )

    def winner_chosen(self):
        return self.winner_ticket

    def select_winner(self):
        winner_ticket = sample(
            settings.LOTTERY_NUMBER_RANGE,
            settings.LOTTERY_TICKET_NUMBERS,
        )
        self.winner_ticket = serialize_ticket(winner_ticket)
        self.save()

    objects = models.Manager()
    open_lotteries = OpenLotteryManager()


class LotteryTicket(models.Model):
    lottery = models.ForeignKey("lottery.Lottery")
    player = models.ForeignKey("auth.User")
    ticket = models.CharField(
        max_length=200,
        help_text="Serialization of the ticket/selection of numbers made by the player",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def is_winner(self):
        return self.lottery.winner_ticket and self.ticket == self.lottery.winner_ticket

    class Meta:
        unique_together = (("lottery", "player"),)
