from django.db import models
from lottery.managers import OpenLotteryManager


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

    open_lotteries = OpenLotteryManager()


class LotteryTicket(models.Model):
    lottery = models.ForeignKey("lottery.Lottery")
    player = models.ForeignKey("auth.User")
    ticket = models.CharField(
        max_length=200,
        help_text="Serialization of the ticket/selection of numbers made by the player",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("lottery", "player"),)
