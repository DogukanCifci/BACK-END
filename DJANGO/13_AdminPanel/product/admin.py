from django.contrib import admin
from .models import *

admin.site.site_title = 'Clarusway Title' # <title>
admin.site.site_header = 'Clarusway Admin Portal' # <navbar>
admin.site.index_title = "Welcome to Clarusway Admin Portal" 
#Category Admin
admin.site.register(Category)

## ---------------- Tabular Inline ------------- ###
class ReviewInline(admin.TabularInline) : # or admin.StackedInline -> Sadece görüntü farki var
    model = Review
    extra =1
    classes = ('collapse',)
#-------------------------Product Admin-----------------------##

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter,DropdownFilter

class ProductAdmin(admin.ModelAdmin) :
    #Tablo Sütunlari :
    list_display = [ 'id', 'name', 'is_in_stock', 'slug', 'create_date', 'update_date'] 
    list_editable = ['is_in_stock'] # Panel üzerinde modelin icine girmeden düzenleme yapabilmek istedigim basliklari buraya ekleyebilirim.
    list_display_links = ['id', 'name'] #Normalde modelin icindeki ürün vb detayina gitmek icin bize default olarak sadece id'ye tiklama izni veriyor. Istersek bu sekilde baska baslik da atayabiliriz.
    #!!!!Ayni sütun basligi hem editable da hem de links de kullanilamaz.

    list_filter = [('name', DropdownFilter),'is_in_stock', 'create_date'] #Sag tarafta filtre yeri cikar. Sadece truelari ya da flaselari göster gibi. veya bugün kayit olmus, 7 gün önce olmus vb gibi....

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
        ('category'),
        #Bütün elementleri yazmak zorundayim. Yoksa hata ile karsilasiyorum.
    ) """

    #2 Method ayni anda kullanilmaz

    #2. Method (Daha Detayli)

    readonly_fields = ['view_image'] #Bunu yazmazsam hata verir. -->Admin Panel detail sayfasinda görünmesi icin yazdim. Ama resmi DB'ye göndermeyecegi icin read_only apmak zorundayim.
    fieldsets = (
        ('General:', {
            # 'classes': ('',), # class Eklemek zorunda degiliz.
            'fields': (
                ('name', 'is_in_stock'),
                ('category'),
            ),
            'description': 'Genel ayarları buradan yapabilirsiniz.'
        }),
        ('Details:', {
            'classes': ('collapse','dogukan',), #css'te yazdigimiz class'i verir. collapse'Da acilir gizlenir menü özelligi verir. Dogukan classina ait css olmadigi icin bir özellik katmaz. Sonda , olmali cünkü tupple olmak zorunda
            'fields': (
                ('slug'),
                ('image','view_image'), ###view_image'i admin panael detail'e girince image yükleme yerinin yaninda resim de gözüksün diye yazdik. view_image asagida kendim fonksiyon olustudum html kodlari ile.
                ('description'),
            ),
            'description': 'Diğer ayarları buradan yapabilirsiniz.',
            
        }),
    )
    filter_horizontal = ('category',) #bu yatay veya 
   # filter_vertical = ('category',) # bu da dikey

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
    ##-----------------#####


    ######### RELATED_name ile olusturdugum alt kayitlari TabularInline ile gösterme :
    inlines = [ReviewInline]


    ###-------- Extra Field Ekleme ---------###
    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days

    list_display += ['added_days_ago'] # Admin panelde gözüken diger sütunlar kaybolmadan ekleme yapilsin diye += yaptik. Ve en basta tupple degil liste yaptik. Cünkü tupple'a ekleme veya tupple'dan cikarma yapilmaz.
    added_days_ago.short_description = "DAYS"

    #viewsleri related name ile eklemek istiyorum. Yani yeni bir field daha ;
    def how_many_reviews(self,object) :
        return object.reviews.count()  #reviews modelste yazdigim related_name ile ayni olmak zorunda

    list_display += ['how_many_reviews']
    how_many_reviews.short_description = "reviewed"

    ### Extra Field Ekleme ------ Resim Icin -------#####
    def view_image_in_list(self,object) :
        from django.utils.safestring import mark_safe #HTML Codelarini yazabilmem icin bunu import etmeliyim
        if object.image :
            return mark_safe(f'<a href="{object.image.url}" target="_blank"><img src={object.image.url} style="height:30px ; width:30px;" /></a>')

    list_display = ['view_image_in_list'] + list_display #----->>> += yapsam list_display = list_display + ['view_image_in_list']  resimi en sona atardi. En basa alsin diye bu sekilde yazdim.
   
    view_image_in_list.short_description = "Image"  #Admin panelde görünen baslik fonksiyon adi ile ayni gözükür. Onu degistirmek icin her zaman bu method kullanilabilir

    ##Show Image in Admin Panel > Details Part----
    def view_image(self,object) :
        from django.utils.safestring import mark_safe #HTML Codelarini yazabilmem icin bunu import etmeliyim
        if object.image :
            return mark_safe(f'<a href="{object.image.url}" target="_blank"><img src={object.image.url} style="max-height:200px ; max-width:200px;" /></a>')
    ###view_image_in_list ile ayni fonksiyon. Tekrar yazmamin sebebi detail sayfasinda 30px 30px olmasin daha büyük olsun diye burda boyutlari degistirecegim. Yoksa tekrar yazmak zorunda degilim



   
    ### ------ TextField'i RichTextEditöre Dönüstürme ------ #####
'''
$ pip install django-ckeditor
$ pip freeze > requirements.txt
->settings.py ;
INSTALLED_APPS = (
    # ...
    'ckeditor',
    # ...
)
#----
CKEDITOR_CONFIGS = {
    'default' : {
        'toolbar' : 'full',
        'height' : 700,
        'width' : 1000
    }
}

#Daha sonra bu eklemeleri yapmaliyim. Daha sonra modelsede TextField ve models silip Direk RichTextField yazmam gerekiyor.
'''

#Call ;
admin.site.register(Product, ProductAdmin) #1.degisken farkli 2.degisken farkli. Product kisminin admin panelindeki görüntüsünü degistirdik.

class ReviewAdminPanel(admin.ModelAdmin) :
    list_display = ['__str__', 'created_date','is_released']
    list_per_page = 20
    raw_id_fields = ('product',) #Normalde isim gözüküyro ürünü secerken. Eger bunu yaparsam hem id'sini gösterecek hem de idsini
admin.site.register(Review,ReviewAdminPanel)


#Burada da FixAdmin diye kendim bir tanimlama yapip, eger birden fazla model icin ayni seyleri kullanacaksak onlari Fix'e yazabiliriz. Daha sonra FixAdmin inherit edilebilir.

