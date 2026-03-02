# main/models.py
from django.db import models


class Case(models.Model):
    title = models.CharField("Название", max_length=200)
    subtitle = models.CharField("Подзаголовок", max_length=255, blank=True)
    description = models.TextField("Описание (под заголовком)", blank=True)

    # NEW: картинки как в techimpuls.html
    cover_image = models.ImageField("Обложка для списка (avatar)", upload_to="cases/cover/", blank=True, null=True)
    hero_image = models.ImageField("Главная картинка (фон сверху)", upload_to="cases/hero/", blank=True, null=True)
    mockup_image = models.ImageField("Mockup (большая картинка под кнопкой)", upload_to="cases/mockup/", blank=True, null=True)

    # NEW: тексты блоков “Задача / Исполнение / Результат”
    task_text = models.TextField("Задача", blank=True)
    execution_text = models.TextField("Исполнение", blank=True)
    result_text = models.TextField("Достигнутый результат", blank=True)

    # NEW: блоки Desktop/Mobile как в techimpuls.html
    desktop_text = models.TextField("Текст блока Desktop", blank=True)
    desktop_image = models.ImageField("Картинка Desktop (macbook)", upload_to="cases/desktop/", blank=True, null=True)

    mobile_text = models.TextField("Текст блока Mobile", blank=True)
    mobile_image = models.ImageField("Картинка Mobile (iphone)", upload_to="cases/mobile/", blank=True, null=True)

    is_published = models.BooleanField("Опубликовано", default=True)
    sort = models.PositiveIntegerField("Порядок", default=0)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    slug = models.SlugField("Ссылка (slug)", max_length=200, unique=True)

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"
        ordering = ["created_at"]  # чтобы новые шли вниз

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
    image = models.ImageField("Фото", upload_to="cases/gallery/")
    scale = models.PositiveSmallIntegerField("Масштаб", choices=SCALE_CHOICES, default=SCALE_100)
    title = models.CharField("Заголовок под фото", max_length=200, blank=True)
    subtitle = models.TextField("Текст под фото", blank=True)
    sort = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Фото кейса"
        verbose_name_plural = "Фото кейса"
        ordering = ["sort", "id"]

    def str(self):
        return f"{self.case.title} — {self.get_scale_display()}"