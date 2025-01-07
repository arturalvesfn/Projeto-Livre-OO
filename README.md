Este é um sistema simples de gerenciamento de carros para aluguel. O usuário pode visualizar uma lista de carros disponíveis, escolher um modelo específico, e calcular o custo total de acordo com o número de dias que deseja ficar com o carro. 
Estrutura do Código:
-->Classes

->Carro

Atributos privados:
__modelo
__marca
__ano
__preco

Métodos:
calcular_valor_diaria: Calcula a diária como 1% do preço do carro.
__str__: Formata as informações do carro como uma string.

-->Funções
1-adicionar_carros_predefinidos:
Adiciona uma lista de carros predefinidos ao sistema.

2-listar_carros:
Exibe todos os carros cadastrados no sistema.

3-escolher_modelo_carro:
Permite ao usuário escolher um modelo pelo número, exibe o valor da diária, solicita o número de dias e calcula o valor total do aluguel.

Requisitos
Python 3.7 ou superior.
