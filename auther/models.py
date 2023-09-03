from django.db import models

# Auther moduls
class AutherModel(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_brth = models.DateField(default='')
    place_of_birth = models.CharField(max_length=50,default='')
    Date_of_death = models.DateField(default='')
    Place_of_death = models.CharField(max_length=50, default='')
    images = models.ImageField(upload_to='images/')
    bio = models.TextField()
    GENRE_CHOICES = (
    ('Adventure', 'Adventure'),
    ('Science Fiction', 'Science Fiction'),
    ('Romance', 'Romance'),
    # Boshqa variantlar...
    )
    genre =models.CharField(max_length=50, choices=GENRE_CHOICES)
    
    def __str__(self) -> str:
        return self.first_name    
    class Meta:
        db_table = 'auther'
        
        
# Auther Book
class AutherBookModel(models.Model):
    name = models.CharField(max_length=25)
    pages = models.IntegerField()
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='images/',default='')
    bio = models.TextField()
    GENRE_CHOICES = (
    ('Adventure', 'Adventure'),
    ('Science Fiction', 'Science Fiction'),
    ('Romance', 'Romance'),
    # Boshqa variantlar...
    )
    genre =models.CharField(max_length=50, choices=GENRE_CHOICES)
        
    def __str__(self) -> str:
        return self.name
        
    class Meta:
        db_table = 'autherbook'