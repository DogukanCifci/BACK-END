from django.contrib import admin
from .models import *


# ------------------ Product Admin ---------------------#

class ProductAdmin(admin.ModelAdmin) :
    #Tablo Sütunlari :
    list_display = [ 'id', 'name', 'is_in_stock', 'create_date', 'update_date'] 
    list_editable = ['is_in_stock'] # Panel üzerinde modelin icine girmeden düzenleme yapabilmek istedigim basliklari buraya ekleyebilirim.
    list_display_links = ['id', 'name'] #Normalde modelin icindeki ürün vb detayina gitmek icin bize default olarak sadece id'ye tiklama izni veriyor. Istersek bu sekilde baska baslik da atayabiliriz.

    #!!!!Ayni sütun basligi hem editable da hem de links de kullanilamaz.
    
    #admin_class tanimladik. register'a gidersem görürüm. 
    
#Call ;
admin.site.register(Product, ProductAdmin) #1.degisken farkli 2.degisken farkli. Product kisminin admin panelindeki görüntüsünü degistirdik.

