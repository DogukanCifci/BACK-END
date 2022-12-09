from django.urls import path, include
from fscohort.views import fscohort,fscohort2

# must be in views.py:
urlpatterns = [
    path('', fscohort), # fs linjk --> .../fscohort iken fscohort fonksiyonuna gider.
    path('example/', fscohort2), # ..../fscohort/example iken fscohort2 fonksiyonuna gider
    #yani direk link ..../ iken fscohorta gitmez o zaman maindeki url kismindaki cagirdigimiz fonksiyon neresiyse oraya gider
]