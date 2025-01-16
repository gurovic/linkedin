import io
from PIL import Image

from django.db import models
from django.utils import timezone
from django.core.files.base import ContentFile

class Event(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    picture = models.ImageField(upload_to = "events/", blank = True)

    date = models.DateTimeField()
    participants = models.ManyToManyField("auth.User", blank = True, related_name = "events")
    location = models.CharField(max_length = 200)
    allowed = models.BooleanField(default = False)

    def already_passed(self):
        now = timezone.now()
        return now > self.date + timezone.timedelta(days = 1)

    def format_image_to_height(self, target_height):
        if self.picture:
            img = Image.open(self.picture)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            aspect_ratio = img.width / img.height
            target_width = int(target_height * aspect_ratio)
            img = img.resize((target_width, target_height), Image.LANCZOS)
            image_io = io.BytesIO()
            img.save(image_io, format = "JPEG")
            picture_filename = self.picture.name.split('/')[-1]
            self.picture.save(picture_filename, ContentFile(image_io.getvalue()), save = False)
        else:
            raise ValueError("Событие не имеет изображения для форматирования.")

    def __str__(self):
        return self.name