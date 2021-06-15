import time

def carro():
    print('')
    print('=-=' * 10, 'Calcular custo por KM rodado', '=-=' * 10)
    print('')
    placa_carro = input('Informe a placa do veiculo: ')
    return placa_carro


def km_rodado():
    distancia_em_km = float(input('Informe a distância em km percorrida: '))
    return distancia_em_km


def calcular_custo(placa_do_carro, km_rodado):
    calculo = float(km_rodado * 5.30)
    print('Aguarde o cálculo !!!')
    time.sleep(5)
    print('')
    print(f'O Veiculo identificado pela placa [{placa_do_carro}] percorreu {km_rodado}Km/h'
          f' gerando um custo em combustível R${calculo:.2f}')
    return calculo


if __name__ == '__main__':
    info_placa = carro()
    km_rodado_pelo_carro = km_rodado()
    resultado = calcular_custo(info_placa, km_rodado_pelo_carro)
