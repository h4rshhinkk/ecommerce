from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        verbose_name = "Category"
        


    def __str__(self):
        return self.category_name
    
class SubCategory(models.Model):
    category = models.ForeignKey('products.Category',on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        verbose_name = "Sub Category"

    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    sub_category = models.ForeignKey('products.SubCategory',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField( max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to="product/",)
    description = models.TextField()


    class Meta:
        verbose_name = "Product"
        ordering = ['sub_category','product_name']


    def __str__(self):
        return self.product_name
    
