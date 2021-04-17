from django.db import models


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "categories"


class food(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True, )
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "foods"


class newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "newsletters"


class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=300)

    def __str__(self):
        return '{}'.format(self.name)
    class Meta:
        verbose_name_plural = "contacts"


class order(models.Model):
    Food = models.ForeignKey(food, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.Food.name


