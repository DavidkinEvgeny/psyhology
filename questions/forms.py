from dataclasses import fields
from django import forms
from .models import MyQuesyion


class QuestionForm(forms.ModelForm):
    class Meta:
        model = MyQuesyion
        fields = [
            "name",
            "age",
            "work",
            "position",
            "level_of_awareness",
            "activity_in_social_networks",
            "message_board_activity",
            "activity_on_online_trading_platforms",
            "anonymity_on_the_internet",
            "use_of_reaction_enhancers",
        ]
