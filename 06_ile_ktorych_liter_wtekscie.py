import pprint
message = 'Administratorem bazy w której znajduje się Twój adres jest Serverstyle sp. z o.o. ul. Teofila Wiśniowskiego 1A, 37-700 Przemyśl. Wiadomość wysłana na zlecenie Toyota Motor Poland Company Limited sp. z o.o., 02-673 Warszawa, ul. Konstruktorska 5, Sąd Rejonowy dla m. st. Warszawy, XIII Wydział Krajowego Rejestru Sądowego, nr 0000025715 NIP: 521-012-31-77, Kapitał zakładowy: 475.000,- PLN . Jeżeli chcesz zrezygnować z możliwości otrzymywania wiadomości kliknij tutaj. W razie dodatkowych pytań zapraszamy do kontaktu pod adresem kontakt@servernews.pl..'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)