ccc=raw_input("Introduzca CCC: ").split("-")
bancos=open("banco.txt","r")
for linea in bancos:
	if ccc[0] == linea.split(",")[0]:
		print "La entidad bancaria es:", linea.split(",")[1]
		break

