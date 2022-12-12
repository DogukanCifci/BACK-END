from django.db import models

# Create your models here.
class Student(models.Model) :
    first_name = models.CharField(max_length=50, default="")
    last_name=models.CharField(max_length=50, default="")
    number = models.IntegerField(default=0)

#Bir model eklendiginde/degistirildiginde asagidaki komutlari unutmamamiz gerekiyor.
#makemigrations
#migrate

#Sitede Object yazmak yerine altta verdigimiz format seklinde gözükecek(Student Object diye gözükür yoksa)
#Class'in icinde olmasi gerekiyor
    def __str__(self):
        return f'{self.number} - {self.first_name} {self.last_name}'

#Modelin varsayilan özelliklerini degisitirmek icin ;
#Class'in icinde olmasi gerekiyor
#Admin panelindeki gözümüze carpan seylerin degisikliklerini bu sekilde yapabiliriz.
    class Meta :
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#model-meta-options
        # db_table = 'ogrenci' # tablo_adı değiştir.
        ordering = ['-number'] #Objeleri siralama 
        verbose_name ="Ögrenci" #Modelin Ismi
        verbose_name_plural = "Ögrenciler" # Modelin cogul ismi



'''
    # Django - Shell - ORM
    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups
    $ python manage.py shell
    > objname = Student.objects.create(first_name='Abc', last_name='Def', number=5) # Yeni Kayıt
    > objname = Student.objects.all() # Tüm kayıtları getir (liste)
    > objname = Student.objects.get(number=5) # Number=5 olan kaydı getir (tek kayıt)
    > objname = Student.objects.filter(number=5) # Number=5 olan kayıtları getir (liste)
    > objname = Student.objects.filter(first_name__startswith='Q') # firstname 'Q' ile başlayan kayıtları getir (liste)
    > objname = Student.objects.filter(last_name__endswith='n') # lastname 'n' ile biten kayıtları getir (liste)
    > objname = Student.objects.filter(last_name__contains='a') # lastname 'a' içeren kayıtları getir (liste)
    > objname = Student.objects.exclude(number=5) # Number=5 olMAyan kayıtları getir (liste)
    > objname = Student.objects.exclude(last_name__contains='a') # lastname 'a' içerMEyen kayıtları getir (liste)
'''