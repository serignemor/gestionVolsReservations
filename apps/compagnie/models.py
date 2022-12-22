from PIL import Image
from django.db import models


class Compagnie(models.Model):
    nom = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='compagnie/')

    def __str__(self):
        return self.nom

    # def save(self, *args, **kwargs):
    #     super(Compagnie, self).save(*args, **kwargs)
    #     print(self.logo)
    #     if not self.logo == '':
    #         imag = Image.open(self.logo.path)
    #         width = imag.width
    #         height = imag.height
    #         if imag.width > 640:
    #             perc = (width - 640) / width
    #             width = 640
    #             height = height - (height * perc)
    #         if imag.height > 480:
    #             perc = (height - 480) / height
    #             height = 480
    #             width = width - (width * perc)
    #         output_size = (width, height)
    #         imag.thumbnail(output_size)
    #         imag.save(self.logo.path)
