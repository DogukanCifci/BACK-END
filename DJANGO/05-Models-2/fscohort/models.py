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
        #db_table = 'ogrenci'
        ordering = ['-number'] #Objeleri siralama 
        verbose_name ="Ögrenci" #Modelin Ismi
        verbose_name_plural = "Ögrenciler" # Modelin cogul ismi