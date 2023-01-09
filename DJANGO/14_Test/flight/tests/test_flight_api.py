from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from flight.views import *
from flight.models import *
from django.contrib.auth.models import User


#Nonauthenticated User giris yapabildiginde erisim saglayabiliyor mu onun kontrolünü yapacagiz. Cunku biz permission_class olarak isStaffOrReadOnly atamisiz.

class FlightViewTestCase(APITestCase) :

    
    def create_flight(self) :
        flight = Flight.objects.create({
        "flight_number": "TK8438",
        "operation_airlines": "THY",
        "departure_city": "Köln",
        "arrival_city": "Samsun",
        "date_of_departure": "2023-01-11",
        "estimated_time_departure": "12:00:00"
        })
        return flight

    def setUp(self) :
        self.factory = APIRequestFactory()
        self.create_flight()
        self.user = User.objects.create_user(
            username='dogukan',
            password="dogukan",
            email="dogukan@gmail.com"
        )
        self.token = Token.objects.create(user=self.user) #Olusturdugum user icin token olusturma komutu

    def test_flight_lisst_as_non_azthenticate_user(self) : #--->fonksiyon basina test yazmak zorundayim. Gerisi bana kalmis.
        #factory = APIRequestFactory() #-->Eger setup fonksiyonunda tanimlamasam burda tanimlamam gerekir. ve self yazmadan yazabilirdim
        request = self.factory.get('/flight/flights/')
        response = FlightView.as_view({'get' : 'list'})(request)
        self.assertEquals(response.status_code, 200)  # Gelen response'un status_code'unun 200'e esit olup olmadigini kontrol et demek. 201 yapsam terminal'De 200!=201 diye sonuc verirdi. cunkü gelen response_code 200. 200 yazdim ve sonuc gectigi icin OK diye cevap aldim.
        self.assertNotContains(response, 'reservation') ## Hep true döndürmeliyim kontrol de Burada reservation key'inin dönen data icinde olmamasi gerekiyor.


    
    def test_flight_list_as_staff_user(self) :
        request = self.factory.get('/flight/flights/', HTTP_AUTHORIZATION = 'Token {}'.format(self.token)) #OLUSTURDUGUM TOKENÄI POSTMANDE NASIL HEADER'A KOYUYORSAM BURDA DA KOYMAM LAZIM. CÜNKÜ STAFF USER ILE GIRIS YAPMAYI TEST EDIYORUM
        self.user.is_staff=True #user staff ikenki sonucu görmek icin test ediyorum Bundan dolayi burda staff özelligini True yapiyorum
        self.user.save()
        request.user=self.user
        response = FlightView.as_view({'get' : 'list'})(request)
        self.assertContains(response, 'reservation')