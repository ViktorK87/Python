from smartphone import Smartphone
catalog = [
    Smartphone("Iphone", "15", "+79563453456"), 
    Smartphone("Samsung", "Galaxy s20", "+79162349808"),
    Smartphone("Huawey", "SuperPhone", "+79031423678"),
    Smartphone("Mi", "MiPhone", "+79320987654"),
    Smartphone("Siemens", "A35", "+79001832387")
    ]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")