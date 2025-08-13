# 🚗 Cadastro e Exibição de Dados do Carro em Python

Este repositório contém um script simples em Python que permite ao usuário inserir informações sobre um carro, como nome, valor e consumo de combustível, e exibe essas informações formatadas no terminal.

## 📋 Descrição

O programa solicita ao usuário que digite:

- O nome do carro
- O valor do carro (em reais)
- O consumo do carro em km por litro

Após a entrada, o programa imprime um resumo dos dados informados, formatando o valor monetário com duas casas decimais.

## 💻 Código

```python
nome_carro = input("Digite o nome do carro: ")
valor_carro = float(input("Digite o valor do carro: "))
consumo_por_litro = float(input("Digite o consumo do carro (km/l): "))

print("---------------------------------------------")
print(f"Nome do carro     | {nome_carro}")
print(f"Valor do carro    | R${valor_carro:.2f}")  
print(f"Consumo do carro  | {consumo_por_litro} km/l")
print("---------------------------------------------")
