#comando(): quero permitir que  
#o usuário digite algo...
nome = input("Digite o seu nome:")

#pede a idade para o usuário"Qual sua idade?"
idade = int(input("Digite sua idade:"))

#comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba "Sua idade é..."
print(f"Sua idade é {idade}")

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2 
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
if (idade >= 18):
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("você é xóven ainda, xóven ainda")

  
#E se eu quisesse perguntar o gênero (M= Masculino e F= Feminino)
#Mostre (... e você também precisa/precisou prestar o serviço militar obrigatório)
sexo = input("Digite o seu sexo:M=Masculino, F=Feminino, O=Outros: ")
if (sexo == "M" and idade >= 18):
  print("... e você também precisou/precisa prestar serviço militar obrigatório")

#else:
 # print("... e você também não precisou/precisa prestar serviço militar obrigatório")

  
print("vai ser executada de qualquer jeito")