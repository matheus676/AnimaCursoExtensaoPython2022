#Pede o nome do aluno  e sua nota (de 0 a 10) e, se ele tirou nota 10,mostra  "Você é bichão, mesmo ..."
nome = input("Digite o seu nome:")
nota = float(input("Digite a sua nota de 0 a 10:"))
#while nota > 10 or nota < 0: 
# print("Nota invalida")
# nota = float(input("Digite a sua nota de 0 a 10:"))
if (nota==10):
  print(f"{nome}, você é o bichão mesmo")
elif(nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho")
else:
  print("Burro, não tirou dez")