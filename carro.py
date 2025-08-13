nome_carro = input("Digite o nome do carro: ")
valor_carro = float(input("Digite o valor do carro: "))
consumo_por_litro = float(input("Digite o consumo do carro (km/l): "))

print("---------------------------------------------")
print(f"Nome do carro     | {nome_carro}")
print(f"Valor do carro    | R${valor_carro:.2f}")  
print(f"Consumo do carro  | {consumo_por_litro} km/l")
print("---------------------------------------------") 