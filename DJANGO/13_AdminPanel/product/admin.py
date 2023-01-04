from django.contrib import admin
from .models import *


# ------------------ Product Admin ---------------------#

class ProductAdmin(admin.ModelAdmin) :
    #Tablo Sütunlari :
    list_display = [ 'id', 'name', 'is_in_stock', 'slug', 'create_date', 'update_date'] 
    list_editable = ['is_in_stock'] # Panel üzerinde modelin icine girmeden düzenleme yapabilmek istedigim basliklari buraya ekleyebilirim.
    list_display_links = ['id', 'name'] #Normalde modelin icindeki ürün vb detayina gitmek icin bize default olarak sadece id'ye tiklama izni veriyor. Istersek bu sekilde baska baslik da atayabiliriz.
    #!!!!Ayni sütun basligi hem editable da hem de links de kullanilamaz.

    list_filter = ['is_in_stock', 'create_date'] #Sag tarafta filtre yeri cikar. Sadece truelari ya da flaselari göster gibi. veya bugün kayit olmus, 7 gün önce olmus vb gibi....

    search_fields = ['id','name'] #id ve name'e göre arama butonu cikartir. iceren bir harf veya sayi girersek direk algilar
    search_help_text = "Arama islemlerini buradan yapabilirsiniz" #Butonun altinda helper text olusturur.

    ordering = ['id'] # Ilk acildiginda otomatik olarak buna göre sirala demek. Basina - koyarsam tersten yapar

    list_per_page = 20 #default = 100

    date_hierarchy = 'create_date' #Yukarida filtremsi bi sey cikar. Bugün olusturulanlari, Ocak 2023'te olusturulanlari, 2023 'te olusutulanlari vb gibi..

    list_max_show_all = 999

    #admin_class tanimladik. register'a gidersem görürüm. 


    #BaseModel'e kadar indik;
    prepopulated_fields = {'slug': ['name']} #Models'te olusturdugum slug'in name'i base alarak otomatik olusmasini istiyorum. Birden fazla sey ekleyebiliirm name'in yanina. Max_length 50 dir. Degistirilebilir. Slug otomatik olarak SEO'ya uygun bir url olusturur. O iteme tiklandiginda slugdaki isim neyse urlde o gözükür. 


#Call ;
admin.site.register(Product, ProductAdmin) #1.degisken farkli 2.degisken farkli. Product kisminin admin panelindeki görüntüsünü degistirdik.

