from Address import Address
from Mailing import Mailing

mailing = Mailing(Address("111401", "Ленинград", "Строителей", "25", "13"),
                   Address("235642", "Москва", "Чекистов", "1А", "39"), 500,
                    "MKAM23MCE4")


print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")