
class Carro:
    def __init__(self, modelo, marca, ano, preco):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__preco = preco

    def calcular_valor_diaria(self):
        return self.__preco * 0.01

    def __str__(self):
        return f"Modelo: {self.__modelo}, Marca: {self.__marca}, Ano: {self.__ano}, Preço: R${self.__preco:.2f}"


def adicionar_carros_predefinidos():
    return [
        Carro("Civic", "Honda", 2021, 90000.0),
        Carro("Corolla", "Toyota", 2022, 95000.0),
        Carro("Onix", "Chevrolet", 2023, 80000.0),
        Carro("Polo", "Volkswagen", 2020, 70000.0),
        Carro("Sentra", "Nissan", 2019, 85000.0),
    ]


def listar_carros(carros):
    print("\nCarros Cadastrados:")
    for carro in carros:
        print(carro)


def escolher_modelo_carro(carros):
    print("\nEscolha um modelo de carro para calcular o valor da diária:")
    modelos_disponiveis = {i: carro for i, carro in enumerate(carros)}
    for i, carro in modelos_disponiveis.items():
        print(f"[{i}] Modelo: {carro._Carro__modelo}")

    try:
        escolha = int(input("Digite o número do modelo desejado: "))
        if escolha in modelos_disponiveis:
            carro_escolhido = modelos_disponiveis[escolha]
            print(f"\nVocê escolheu: {carro_escolhido}")
            diaria = carro_escolhido.calcular_valor_diaria()
            print(f"Valor da diária: R${diaria:.2f}")

            dias = int(input("Quantos dias deseja ficar com o carro? "))
            if dias > 0:
                valor_total = dias * diaria
                print(f"\nValor total para {dias} dias: R${valor_total:.2f}")
            else:
                print("\nQuantidade de dias inválida! Tente novamente.")
        else:
            print("\nÍndice inválido! Tente novamente.")
    except ValueError:
        print("\nEntrada inválida! Certifique-se de digitar um número.")


if __name__ == "__main__":
    carros = adicionar_carros_predefinidos()

    print("Sistema de Gerenciamento de Carros")

    listar_carros(carros)
    escolher_modelo_carro(carros)

    print("Saindo do sistema. Até logo!")
