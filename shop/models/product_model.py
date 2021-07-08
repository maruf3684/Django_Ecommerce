from django.db import models
from .ctagory_model import Catagory
from django.utils.safestring import mark_safe

class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    discription=models.TextField()
    brand=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to='Files/productimg')

    #this method will show photo in admin panel
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.product_image.url))
    admin_photo.short_description="Image"
    admin_photo.allow_tags=True

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_product():
        return Product.objects.order_by('?')

