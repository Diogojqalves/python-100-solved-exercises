name = "Computer"
notaMax = 0
nameMin = name
while name != "STOP":
   name = input("Digite o nome: ")
   nota = int(input("Digite a sua nota de português: "))
   if nota > notaMax:
       notaMax = nota
       nameMin = name
# number=int(input('Enter number of students: '))
# average=float(sum(nota)/number)
# print('Average is: %.2f '%(average))
print("melhor classificado:", nameMin, "com nota", notaMax)
