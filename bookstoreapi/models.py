from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Author's name")
    bio = models.TextField(blank=True, verbose_name="Biography")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name="Author")
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    stock = models.PositiveIntegerField(default=0, verbose_name="Quantity in stock")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
