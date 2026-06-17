# Sistema de Elevadores Inteligentes
# Faculdade - 2 elevadores, 7 andares

# posicao inicial dos elevadores
elevador_a = 0
elevador_b = 4

# andares que existem no predio
andares_validos = [-2, -1, 0, 1, 2, 3, 4]

print("=== Sistema de Elevadores ===")
print(f"Elevador A comeca no andar {elevador_a}")
print(f"Elevador B comeca no andar {elevador_b}")

# loop principal do sistema
while True:
    print("\n---- Menu ----")
    print("1 - Chamar elevador")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "0":
        print("Encerrando sistema...")
        break

    elif opcao == "1":

        # pegar o andar de origem
        andar_origem = int(input("De qual andar voce esta chamando? "))

        # verificar se o andar existe
        if andar_origem not in andares_validos:
            print("Andar invalido! Os andares validos sao:", andares_validos)

        else:
            # pegar o andar de destino
            andar_destino = int(input("Para qual andar voce quer ir? "))

            # verificar se o destino existe
            if andar_destino not in andares_validos:
                print("Andar invalido! Os andares validos sao:", andares_validos)

            else:
                # calcular qual elevador esta mais perto
                distancia_a = abs(elevador_a - andar_origem)
                distancia_b = abs(elevador_b - andar_origem)

                print(f"\nElevador A esta no andar {elevador_a}, distancia: {distancia_a}")
                print(f"Elevador B esta no andar {elevador_b}, distancia: {distancia_b}")

                # escolher o mais proximo
                if distancia_a <= distancia_b:
                    print("Elevador A foi escolhido!")

                    # mover ate o usuario
                    print(f"Elevador A indo do andar {elevador_a} ate o andar {andar_origem}...")
                    elevador_a = andar_origem

                    # pegar o usuario e ir pro destino
                    print(f"Usuario embarcou! Indo para o andar {andar_destino}...")
                    elevador_a = andar_destino
                    print(f"Chegou no andar {andar_destino}!")

                else:
                    print("Elevador B foi escolhido!")

                    # mover ate o usuario
                    print(f"Elevador B indo do andar {elevador_b} ate o andar {andar_origem}...")
                    elevador_b = andar_origem

                    # pegar o usuario e ir pro destino
                    print(f"Usuario embarcou! Indo para o andar {andar_destino}...")
                    elevador_b = andar_destino
                    print(f"Chegou no andar {andar_destino}!")

                print(f"\nPosicao atual: Elevador A = andar {elevador_a} | Elevador B = andar {elevador_b}")

    else:
        print("Opcao invalida!")