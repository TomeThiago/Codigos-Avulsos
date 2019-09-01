import datetime

#datetime() recebe como paramametros:
#ano, mes, dia, hora, minuto, segundo
#e retorna um objeto do tipo datetime
dt = datetime.datetime(2020, 12, 31, 23, 59, 59)

#Objetos data e time podem ser criados
#a partir de um objeto datetime
data = dt.date()
hora = dt.time()

#Quanto tempo falta para 31/12/2020

dd = dt - dt.today()

print('Data:', data)
print('Hora:', hora)
print('Quanto tempo falta para 31/12/2020:', str(dd).replace('days','dias'))