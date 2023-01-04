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


    #Inputlarin KONUMLANDIRILMASI :
    #1. Method (Daha Sade)
    """ fields = (
        ('name', 'is_in_stock'), #Name ile is_in_stock kismi yan yana gelsin demek
        ('slug'), #Slug yukardaki ikilinin altinda olsun
        ('description'), #Description en altta olsun. 

        #Bütün elementleri yazmak zorundayim. Yoksa hata ile karsilasiyorum.
    ) """

    #2 Method ayni anda kullanilmaz

    #2. Method (Daha Detayli)


    fieldsets = (
        ('General:', {
            # 'classes': ('',), # class Eklemek zorunda degiliz.
            'fields': (
                ('name', 'is_in_stock'),
            ),
            'description': 'Genel ayarları buradan yapabilirsiniz.'
        }),
        ('Details:', {
            'classes': ('collapse','dogukan',), #css'te yazdigimiz class'i verir. collapse'Da acilir gizlenir menü özelligi verir. Dogukan classina ait css olmadigi icin bir özellik katmaz. Sonda , olmali cünkü tupple olmak zorunda
            'fields': (
                ('slug'),
                ('description'),
            ),
            'description': 'Diğer ayarları buradan yapabilirsiniz.'
        }),
    )


    # ------ Toplu islemlere Islem ekleme --------#
    #action kisminda normalde sadece delete vardi. Buraya kendim de eklemlerde bulunabiliyorum..
    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True) # Kendi olusturdugum is_in_stock degerini queryset.update methodu ile güncelledim.
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.') # islem gerceklestikten sonra yukarda olusacak mesaj icerigi
    

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False) 
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    actions = ('set_stock_in', 'set_stock_out')
    set_stock_in.short_description = 'İşaretli ürünleri "Stokta Var" olarak Isaretler' #Action kisminda yazicak olan mesaj icerigi
    set_stock_out.short_description = 'İşaretli ürünleri "Stokta Yok" olarak isaretle'

#Call ;
admin.site.register(Product, ProductAdmin) #1.degisken farkli 2.degisken farkli. Product kisminin admin panelindeki görüntüsünü degistirdik.

