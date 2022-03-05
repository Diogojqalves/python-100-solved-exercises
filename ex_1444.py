name = "Computer"
ageMin = 200
nameMin = name
while name != "STOP":
   name = input("Digite o nome: ")
   age = int(input("Digite a sua idade: "))
   if age < ageMin:
       ageMin = age
       nameMin = name

print("mais jovem:", nameMin, "com", ageMin)