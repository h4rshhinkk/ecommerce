from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=50,blank=True,null=True)
    image = models.ImageField(upload_to="Category/",)


    class Meta:
        verbose_name = "Category"
        
    

    def __str__(self):
        return self.category_name
    
class SubCategory(models.Model):
    category = models.ForeignKey('products.Category',on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=50,blank=True,null=True)
    image = models.ImageField(upload_to="Sub Category/",)


    class Meta:
        verbose_name = "Sub Category"

    def __str__(self):
        return self.sub_category_name



class Product(models.Model):
    sub_category = models.ForeignKey('products.SubCategory',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    price = models.DecimalField( max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to="product/",)
    description = models.TextField()


    class Meta:
        verbose_name = "Product"
        ordering = ['sub_category','product_name']

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.product_name
    
