# Yazlab2 1. Proje

# Araç Takip Sistemi

# ÖZET

Yazılım Laboratuvarı 2 dersi 1.projesi kapsamında çok katmanlı bir web uygulaması 
geliştirilecektir. Bu proje ile birlikte gerçek dünya ihtiyaçlarını karşılayacak bazı yetenekler 
kazandırılacaktır.Bunlardan başlıcaları Model, Manzara/Arayüz ve Yönetim 
(Model,View,Controller) kalıbının kullanılması (Arayüz, İşlem Mantığı ve Verinin 
ayrıştırılması) Dağıtık bir sistem mimari kullanarak çözüm oluşturma Güncel bir web 
kütüphane, alt yapısının kullanımının öğrenilmesi ve uygulanması ,veri tabanlarını kullanma 
ve veri tabanı tasarımı konularıdır.

# GİRİŞ

Projede bizden istenilen kullanıcılar için onların araç bilgilerinin gösterildiği bir sistem
tasarlamamızdır.Bunun için öncelikle kullanıcıların isim ve şifre bilgileri alınarak hangi
kullanıcının sisteme girdiği alınır.Bundan sonraki adımda ise kullanıcının sahip olduğu tüm
araçların son yarım saatlik konum bilgileri harita üzerinde gösterilir.Bu ekranda kullanıcının
seçebileceği iki adet buton vardır. Bunlardan ilki seçim menüsüne yönlendirir.Diğeri ise giriş
ekranına gönderir.Bu ekranın en altında kullanıcının araçlarının konum bilgileri dakika dakika
gösterilir ve yol güzergahı gösterilir.Eğer kullanıcı seçim ekranını seçtiyse sahip olduğu
araçlar,seçilmek üzere saat bilgileri bulunur. Burada ayrıca üç adet buton vardır.Bunlar
submit,geri ve çıkış butonlarıdır.Geri butonu bir önceki sayfaya geçiş yaparak son 30 dakikalık
veriyi gösterir.Çıkış tuşuna basarsak giriş ekranına dönüş yapılır.Kullanıcı seçim ekranında
göstermek istediği aracı ve saat aralıklarını seçtikten sonra submit tuşuna basarsak haritamız
açılır.Bu harita ekranımızda ise kullanıcının seçtiği aracın kullanıcının seçtiği saat
aralıklarındaki bilgileri harita üzerinde gösterilir ve yol güzergahı gösterilir.Bu harita
ekranında iki adet buton bulunmaktadır.Bu butonlardan ilki geri dön butonudur.Bu buton
seçilerek seçim ekranınna geri dönülür.Diğer buton ise çıkış butonudur.Bu buton ile çıkış
yapılarak kullanıcı giriş ekranına yönlendirilir.

# I. YÖNTEM

Program Python programlama dilinde geliştirdik.Bizden istenen MVC yapısı olarak
Flask frameworkünü tercih ettik. Geliştirme ortamı olarak ise “Visual Studio Code”
kullandık. Veri tabanı yönetim sistemi için SQLite’ı kullandık.NoSql database 
olarak Firebase Firestore’u kullandık. Projemize başlarken öncelikle yol haritamızı 
çıkardık. Projenin isterlerini analiz edip bu isterler üzerine araştırmalar yaptık.Bu 
araştırmalarımıza öncelikle kullanacağımız dile karar vermek oldu.Bunun için 
pythonda karar kıldık.Sonra bizden istenen mvc yapısı için hangi framework’ü 
kullancağımız hakkında kararsız kaldık.Ya önceden kullandığımız Django veya 
Flask’ı tercih edicektik.Flask’ın MVC yapısına daha uygun olduğunu öğrenince 
Flask’ta karar kıldık.Bundan sonraki adım olarak ise database seçim ve bu 
database’de verileri tutmamız oldu.Bunun için SQLite’ı tercih ettik.Database 
kullandığımız tablolar şu şekildedir :

## Users :
Bu tabloda bireyin kişisel bilgileri(name,password,loginTime,logoutTime)bulunur.
vehicles:Bu tabloda hangi bireyin hangi araca sahip olduğu bilgileri tutulur.NoSql 
olarak kullandığımız database’imizde ise kullanıcının araçlarının hangi zamanda 
nerde olduğu tutulmuştur.Bu sayede kullanıcı ilk başta giriş yaptığında SQLite’dan 
kullanıcı bilgilerinin doğruluğu kontrol edilir.Ondan sonra hangi kullanıcı girdiyse 
onun bilgileri firestore’dan çekilerek haritada gösterilir.Tüm bunları yapmak için 
flask framework’ün bize sağladığı MVC yapısı kullanılır.MVC yapısının içinde 
bulunan Models,Views ve Contrallers şu şekilde kullanılmıştır.

## Contrallers:

### session_interface.py:
Kullanıcın bilgilerinin tutulmasını sağlar

### users.py:
Kullanıcınının girişini çıkışını ve isminin kontrolü yapılır.

## Models:

### models.py:
SQLite’dan bilgilerin çekilmesini sağlar

## Views:

### home.py:
Kullanıcının mapleri ve seçim ekranıyla ilgili her türlü yönlendirmenin
yapıldığı ve firestore’dan çekilen bilgilerin tutulduğu yerdir.

### users.py:
Kullanıcının bilgilerinin alınarak login yapılması sağlanır.

# DENEYSEL SONUÇLAR
## Giriş ekranı :

![image](https://user-images.githubusercontent.com/58952369/180182094-9648a5ca-fba3-482d-8a9d-c8300bfa3f04.png)

###Son 30 dakikalık Verinin Gösterildiği Ekran :

![image](https://user-images.githubusercontent.com/58952369/180182171-770cb02f-d325-4d29-bb44-7b6ac9653ab9.png)

![image](https://user-images.githubusercontent.com/58952369/180182203-1ea908db-825a-4965-b431-57fd22926c07.png)


###Seçim Ekranı :

![image](https://user-images.githubusercontent.com/58952369/180182355-28c6da0f-e9b7-4520-be3f-1e728cf9933b.png)


###Seçilen bilgilerin sonuçlarının gösterildiği ekran:

![image](https://user-images.githubusercontent.com/58952369/180182395-17799190-c7b4-4a84-a026-2984574f194e.png)

![image](https://user-images.githubusercontent.com/58952369/180182445-92703550-0c50-45e3-95fc-b8f6a5b8a154.png)



# V. AKIS DIAGRAMI

![image](https://user-images.githubusercontent.com/58952369/180182476-78118605-5522-4efe-bf22-4e247a8db3e4.png)


# VI. KAYNAKÇA

https://flask.palletsprojects.com/en/2.0.x/

https://www.youtube.com

https://tutorial.djangogirls.org/

https://stackoverflow.com/

https://www.geeksforgeeks.org

https://developers.google.com/maps/documentation/javascript/

www.w3schools.com/

https://www.sqlite.org

https://firebase.google.com/doc
