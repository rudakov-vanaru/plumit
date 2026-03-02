from django.db import models


class Case(models.Model):
    title = models.CharField("Название", max_length=200)
    subtitle = models.CharField("Подзаголовок", max_length=255, blank=True)
    description = models.TextField("Описание", blank=True)
    is_published = models.BooleanField("Опубликовано", default=True)
    sort = models.PositiveIntegerField("Порядок", default=0)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    slug = models.SlugField("Ссылка (slug)", max_length=200, unique=True)

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"
        ordering = ["sort", "-created_at"]

    def str(self):
        return self.title


class CaseImage(models.Model):
    SCALE_40 = 40
    SCALE_60 = 60
    SCALE_100 = 100
    SCALE_CHOICES = (
        (SCALE_40, "40%"),
        (SCALE_60, "60%"),
        (SCALE_100, "100%"),
    )

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="images", verbose_name="Кейс")
    image = models.ImageField("Фото", upload_to="cases/")
    scale = models.PositiveSmallIntegerField("Масштаб", choices=SCALE_CHOICES, default=SCALE_100)
    caption = models.CharField("Подпись", max_length=255, blank=True)
    sort = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Фото кейса"
        verbose_name_plural = "Фото кейса"
        ordering = ["sort", "id"]

    def str(self):
        return f"{self.case.title} — {self.get_scale_display()}"
