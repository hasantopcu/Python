#Add codes to check primary key constraint

import pyodbc
import random

mydb = pyodbc.connect('Driver={SQL Server};'
                      'Server=your_server_name;'
                      'Database=your_database_name;'
                      'Trusted_Connection=yes;')

size = 2445
lr = 1
ur = 501

names = []
f = open('isimler.txt','r' , encoding="utf8")
for line in f:
  names.append(line.strip())

Surnames = []
f = open('soyisimler.txt','r' , encoding="utf8")
for line in f:
  Surnames.append(line.strip())
  
cities = {
    "1": "ADANA",
    "2": "ADIYAMAN",
    "3": "AFYONKARAHİSAR",
    "4": "AĞRI",
    "5": "AMASYA",
    "6": "ANKARA",
    "7": "ANTALYA",
    "8": "ARTVİN",
    "9": "AYDIN",
    "10": "BALIKESİR",
    "11": "BİLECİKK",
    "12": "BİNGÖL",
    "13": "BİTLİS",
    "14": "BOLU",
    "15": "BURDUR",
    "16": "BURSA",
    "17": "ÇANAKKALE",
    "18": "ÇANKIRI",
    "19": "ÇORUM",
    "20": "DENİZLİ",
    "21": "DİYARBAKIR",
    "22": "EDİRNE",
    "23": "ELAZIĞ",
    "24": "ERZİNCAN",
    "25": "ERZURUM",
    "26": "ESKİŞEHİR",
    "27": "GAZİANTEP",
    "28": "GİRESUN",
    "29": "GÜMÜŞHANE",
    "30": "HAKKARİ",
    "31": "HATAY",
    "32": "ISPARTA",
    "33": "MERSİN",
    "34": "İSTANBUL",
    "35": "İZMİR",
    "36": "KARS",
    "37": "KASTAMONU",
    "38": "KAYSERİ",
    "39": "KIRKLARELİ",
    "40": "KIRŞEHİR",
    "41": "KOCAELİ",
    "42": "KONYA",
    "43": "KÜTAHYA",
    "44": "MALATYA",
    "45": "MANİSA",
    "46": "KAHRAMANMARAŞ",
    "47": "MARDİN",
    "48": "MUĞLA",
    "49": "MUŞ",
    "50": "NEVŞEHİR",
    "51": "NİĞDE",
    "52": "ORDU",
    "53": "RİZE",
    "54": "SAKARYA",
    "55": "SAMSUN",
    "56": "SİİRT",
    "57": "SİNOP",
    "58": "SİVAS",
    "59": "TEKİRDAĞ",
    "60": "TOKAT",
    "61": "TRABZON",
    "62": "TUNCELİ",
    "63": "ŞANLIURFA",
    "64": "UŞAK",
    "65": "VAN",
    "66": "YOZGAT",
    "67": "ZONGULDAK",
    "68": "AKSARAY",
    "69": "BAYBURT",
    "70": "KARAMAN",
    "71": "KIRIKKALE",
    "72": "BATMAN",
    "73": "ŞIRNAK",
    "74": "BARTIN",
    "75": "ARDAHAN",
    "76": "IĞDIR",
    "77": "YALOVA",
    "78": "KARABüK",
    "79": "KİLİS",
    "80": "OSMANİYE",
    "81": "DÜZCE"
    }


def addCustomer():
  mycursor = mydb.cursor()
  for i in range(lr,ur):
    name = names[random.randint(0,size)]
    surname = Surnames[random.randint(0,size)]
    email = name.lower() + surname.lower() + "@gmail.com"
    email = email.replace(" ","_")
    geoId = random.choice(list(iller))
    query = "insert into dbo.CustomerInfo (CustomerID , CustomerName ,CustomerSurname , CustomerEmail , CustomerPhone , CustomerGeographyID ) values(? , ? , ? , ? , ? , ?)"
    values = (random.randint(0,10000) , name , surname , email , random.randint(0,1000000) , geoId)
    mycursor.execute(query , values)
    mydb.commit()


def getCity():
   
    mycursor6 = mydb.cursor()
    
    for i in cities:
      query = "insert into dbo.cities (id,name) values(? , ?)"
      values = (i , cities[i])
      mycursor6.execute(query , values)
      mydb.commit()


if __name__ == "__main__":
    getCity()
    #addCustomer()






