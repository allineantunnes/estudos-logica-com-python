#Bibliotecas
import datetime

dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hoje = datetime.date.today()
dia_semana = dias[hoje.weekday()]
print("A data de hoje é: ", hoje, dia_semana)
