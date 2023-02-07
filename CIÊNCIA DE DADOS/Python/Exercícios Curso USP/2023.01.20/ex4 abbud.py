SegInput=int(input("Entre com número de segundos que desejar: "))

dia=SegInput//(24*60*60)

horas=(SegInput-dia*24*60*60)//3600

minutos=(SegInput-dia*24*60*60-horas*3600)//60

segundos=SegInput-dia*24*60*60-horas*3600-minutos*60

print(dia,"dias,", horas,"horas,",minutos,"minutos e",segundos,"segundos.")
