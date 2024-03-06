from random import choice

jogador_vitorias = 0
maquina_vitorias = 0

def opçao_jagador():
    esc_jagador = input('Escolha pedra, papel ou tesoura: ')
    esc_jagador.lower()
    if esc_jagador == 'pedra':
        return esc_jagador
    elif esc_jagador == 'papel':
        return esc_jagador
    elif esc_jagador == 'tesoura':
        return esc_jagador
    else:
        print('Opção invalida. Tente novamente')
        opçao_jagador()

def opçao_maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina

while True:

    print('-' * 30)
    esc_jagador = opçao_jagador()
    esc_maquina = opçao_maquina()
    print('-' * 30)

    if (esc_jagador == 'pedra ') and (esc_maquina == 'tesoura ') \
        or (esc_jagador == 'papel ') and (esc_maquina == 'pedra ') \
            or (esc_jagador == 'tesoura ') and (esc_maquina == 'papel '):
        
        print(f'Jogador escolheu {esc_jagador} e a Máquina escolheu {esc_maquina}'
              'Resultado: Você ganhou!')
        jogador_vitorias += 1

    elif esc_jagador == esc_maquina:
        print(f'Jogador escolheu {esc_jagador} e a Máquina escolheu {esc_maquina}'
              'Resultado: Empate!')
    else:
        print(f'Jogador escolheu {esc_jagador} e a Máquina escolheu {esc_maquina}'
              'Resultado: Você perdeu!')
        maquina_vitorias += 1

    print('-' * 30)
    print(f'Vitórias do Jogador: {jogador_vitorias}')
    print(f'Vitórias do Máquina: {maquina_vitorias}')
    print('-' * 30)

    esc_jagador = input('Você quer jogar novamente? ')
    if esc_jagador in ['SIM', 'sim', 'Sim', 's', 'S']:
        pass
    elif esc_jagador in ['NAO', 'nao', 'Nao', 'n', 'N']:
        break
    else:
        break