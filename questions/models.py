from tabnanny import verbose
from django.db import models
from pkg_resources import require
from .calculation import _get_result


class MyQuesyion(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    age = models.ForeignKey("Age", on_delete=models.CASCADE, verbose_name="Возраст")
    work = models.ForeignKey(
        "Work", on_delete=models.CASCADE, verbose_name="Социальный статус(работа)"
    )
    position = models.ForeignKey(
        "Position",
        on_delete=models.CASCADE,
        verbose_name="Позиция",
        null=True,
        blank=True,
    )
    level_of_awareness = models.ForeignKey(
        "LevelOfAwareness",
        on_delete=models.CASCADE,
        verbose_name="Уровень осведомленности",
    )
    activity_in_social_networks = models.ForeignKey(
        "ActivityInSocialNetworks",
        on_delete=models.CASCADE,
        verbose_name="Активность в соц. сетях",
    )
    message_board_activity = models.ForeignKey(
        "MessageBoardActivity",
        on_delete=models.CASCADE,
        verbose_name="Активность доски объявлений",
    )
    activity_on_online_trading_platforms = models.ForeignKey(
        "ActivityOnJnlineTradingPlatforms",
        on_delete=models.CASCADE,
        verbose_name="Активность на торговых интернет-платформах",
    )
    anonymity_on_the_internet = models.ForeignKey(
        "AnonymityOnTheInternet",
        on_delete=models.CASCADE,
        verbose_name="Анонимности в Интернете",
    )
    use_of_reaction_enhancers = models.ForeignKey(
        "UseOfReactionEnhancers",
        on_delete=models.CASCADE,
        verbose_name="Применение усилителей реакции",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["-created"]
        verbose_name = "Опросник пользователя"
        verbose_name_plural = "Опросники"

    def __str__(self):
        return self.name

    result = property(_get_result)


class Age(models.Model):
    user_age = models.CharField(max_length=50, verbose_name="Возраст")

    class Meta:
        verbose_name = "Возраст"
        verbose_name_plural = "Возраст"

    def __str__(self):
        return self.user_age


class Work(models.Model):
    user_work = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Социальный статус(работа)"
        verbose_name_plural = "Социальный статус(работа)"

    def __str__(self):
        return self.user_work


class Position(models.Model):
    user_position = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиция"

    def __str__(self):
        return self.user_position


class LevelOfAwareness(models.Model):
    user_level_of_awareness = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Уровень осведомленности"
        verbose_name_plural = "Уровень осведомленности"

    def __str__(self):
        return self.user_level_of_awareness


class ActivityInSocialNetworks(models.Model):
    user_activity_in_social_networks = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Активность в соц. сетях"
        verbose_name_plural = "Активность в соц. сетях"

    def __str__(self):
        return self.user_activity_in_social_networks


class MessageBoardActivity(models.Model):
    user_message_board_activity = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Активность доски объявлений"
        verbose_name_plural = "Активность доски объявлений"

    def __str__(self):
        return self.user_message_board_activity


class ActivityOnJnlineTradingPlatforms(models.Model):
    user_activity_on_online_trading_platforms = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Активность на торговых интернет-платформах"
        verbose_name_plural = "Активность на торговых интернет-платформах"

    def __str__(self):
        return self.user_activity_on_online_trading_platforms


class AnonymityOnTheInternet(models.Model):
    user_anonymity_on_the_internet = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Анонимности в Интернете"
        verbose_name_plural = "Анонимности в Интернете"

    def __str__(self):
        return self.user_anonymity_on_the_internet


class UseOfReactionEnhancers(models.Model):
    user_use_of_reaction_enhancers = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Применение усилителей реакции"
        verbose_name_plural = "Применение усилителей реакции"

    def __str__(self):
        return self.user_use_of_reaction_enhancers
