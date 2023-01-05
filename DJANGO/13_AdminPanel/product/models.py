from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category name")
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True) #RichTextfield olunca basindaki models'i kaldiriyoruz.
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, default='clarusway.png', upload_to='product/')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name

    def view_image(self) : #admindeki ayni fonksiyonu aldim ama object admin.py'a has bir özellik oldugu icin, objecti sildim. Bunu yazmasam da olurdu. Sadece burda da yazilabilecegini göstermke icin yazdim. Tek fark Object yazmiyoruz burda. self kullaniyoruz.
        from django.utils.safestring import mark_safe #HTML Codelarini yazabilmem icin bunu import etmeliyim
        if self.image :
            return mark_safe(f'<a href="{self.image.url}" target="_blank"><img src={self.image.url} style="height:30px ; width:30px;" /></a>')
        else :
            return mark_safe(f'<h2>There is no Image</h2>')

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}"