from django.db import models
from common.models import Common


class ChattingRoom(Common):

    """Chatting Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
        related_name="chattingrooms",
    )

    def __str__(self) -> str:
        return "Chatting Room"


class Message(Common):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    chatting_room = models.ForeignKey(
        "chattings.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} 메세지 : {self.text}"
