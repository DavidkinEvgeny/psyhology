from django.contrib import admin
from .models import *


@admin.register(MyQuesyion)
class MyQuesyionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created",
        "result",
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


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    list_display = ["user_age"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["user_position"]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ["user_work", "id"]


@admin.register(LevelOfAwareness)
class LevelOfAwarenessAdmin(admin.ModelAdmin):
    list_display = ["user_level_of_awareness"]


@admin.register(ActivityInSocialNetworks)
class ActivityInSocialNetworksAdmin(admin.ModelAdmin):
    list_display = ["user_activity_in_social_networks"]


@admin.register(MessageBoardActivity)
class MessageBoardActivityAdmin(admin.ModelAdmin):
    list_display = ["user_message_board_activity"]


@admin.register(ActivityOnJnlineTradingPlatforms)
class ActivityOnJnlineTradingPlatformsAdmin(admin.ModelAdmin):
    list_display = ["user_activity_on_online_trading_platforms"]


@admin.register(AnonymityOnTheInternet)
class AnonymityOnTheInternetAdmin(admin.ModelAdmin):
    list_display = ["user_anonymity_on_the_internet"]


@admin.register(UseOfReactionEnhancers)
class UseOfReactionEnhancersAdmin(admin.ModelAdmin):
    list_display = ["user_use_of_reaction_enhancers"]
