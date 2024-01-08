#Code to generate fake data
import random

first_names=['Akshay','Salman','Amitabh','Kiara','Ananya','Sara','Tiger','Disha','Vicky','Katrina','Kapil']

last_names=['Kumar','Khan','Bachchan','Advani','Pandey','Khan','Sroff','Patani','Kaushal','Keff','Sharma']

street_names=['Mudit-palace','Ghodod-road','VIP-road','Sindubhanav','Rajauri-park','Canot-palce','Worli-west','Satelite']

fake_city=['Surat','Mumbai','Ahemdabad','Delhi','Gurugram','Bangalore','Chennai','Luckhnow','Patiala']

states=['Gujrat','Delhi','Punjab','Karnataka','J&K','Rajasthan','Toronto']

for num in range(15):
    first=random.choice(first_names)
    last=random.choice(last_names)

    phone=f'{random.randint(62,99)}-999-{random.randint(10000,99999)}'

    street=random.choice(street_names)
    city=random.choice(fake_city)
    state=random.choice(states)
    zip_code=random.randint(1234,9999)
    address=f'{street} St.,{city} ,{state}, {zip_code}'
    email= first.lower()+last.lower()+'@Gmail.commm'
    print(f'{first} {last} \n{phone}\n{address}\n{email}\n')
