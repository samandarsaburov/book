from django.db import models
# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=25)
    pages = models.IntegerField()
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='images/',default='')
    auther = models.CharField(max_length=25)
    bio = models.TextField()
    GENRE_CHOICES = (
    ('Adventure', 'Adventure'),
    ('Science Fiction', 'Science Fiction'),
    ('Romance', 'Romance'),
    # Boshqa variantlar...
    )
    genre =models.CharField(max_length=50, choices=GENRE_CHOICES)
    # user = models.ForeignKey(CustomUser,default='',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = 'book'