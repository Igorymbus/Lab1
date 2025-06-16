from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    registered_date = models.DateField()

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='genre_images/', null=True, blank=True)

    class Meta:
        db_table = 'genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'labels'
        verbose_name = 'Лейбл'
        verbose_name_plural = 'Лейблы'

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist_images/', null=True, blank=True)

    class Meta:
        db_table = 'artists'
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist, through='AlbumArtist')
    cover_image = models.ImageField(upload_to='album_covers/', null=True, blank=True)

    class Meta:
        db_table = 'albums'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.title

class AlbumArtist(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'album_artists'
        unique_together = ('album', 'artist')

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    duration = models.TimeField()

    class Meta:
        db_table = 'tracks'
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return f"{self.title} - {self.album.title}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ #{self.id} - {self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=100)

    class Meta:
        db_table = 'employees'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Sale(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sale_date = models.DateField()

    class Meta:
        db_table = 'sales'
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)

    class Meta:
        db_table = 'payments'
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'suppliers'
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name

class Shipment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shipment_date = models.DateField()

    class Meta:
        db_table = 'shipments'
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

class Inventory(models.Model):
    album = models.OneToOneField(Album, on_delete=models.CASCADE, primary_key=True)
    stock_quantity = models.IntegerField()
    last_updated = models.DateField()

    class Meta:
        db_table = 'inventory'
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'
