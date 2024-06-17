def gerenciar_equipamentos():
    # Inicializa uma lista vazia para armazenar os equipamentos
    equipamentos = []

    # Loop para solicitar ao usuário inserir até três equipamentos
    for i in range(3):
        equipamento = input("Insira o nome do equipamento (ou deixe em branco para terminar): ")
        if equipamento.strip():  # Verifica se o input não está em branco
            equipamentos.append(equipamento)
        else:
            break  # Se o input estiver em branco, encerra o loop

    # Exibindo a lista de equipamentos
    print("\nLista de Equipamentos:")
    for equipamento in equipamentos:
        print(f"- {equipamento}")

# Executa a função para gerenciar os equipamentos
gerenciar_equipamentos()