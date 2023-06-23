from django.db import models


class Client(models.Model):
    telegram_id = models.IntegerField(unique=True)
    nik_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="UserName"
    )

    def __str__(self):
        return f"{self.nik_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Speaker(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name='speakers')
    name = models.CharField(
        max_length=256,
        null=True,
        blank=False,
        verbose_name="Name"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры"


class Topic(models.Model):
    speaker = models.ManyToManyField(Speaker)
    title = models.CharField(
        max_length=256,
        null=True,
        blank=False,
        verbose_name="Name"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class EventQuerySet(models.QuerySet):

    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except Event.DoesNotExist:
            return None


class Event(models.Model):
    title = models.CharField(
        max_length=256,
        null=True,
        blank=False,
        verbose_name="Title"
    )
    text = models.TextField()
    speaker = models.ManyToManyField(Speaker)
    topic = models.ManyToManyField(Topic)

    objects = EventQuerySet.as_manager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Flag(models.Model):
    speaker = models.ForeignKey(Speaker,
                                on_delete=models.CASCADE,
                                related_name='speakers_flag')
    flag = models.BooleanField(
        default=False,
        null=True,
        blank=False,
    )

    def __str__(self):
        return f"{self.speaker} | {self.flag}"

    class Meta:
        verbose_name = "Флаг"
        verbose_name_plural = "Флаги"
