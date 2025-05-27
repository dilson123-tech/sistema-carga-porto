from controllers.carga_controller import (
    carregar_dados,
    mostrar_estatisticas,
    gerar_grafico,
    cadastrar_carga,
    gerar_cargas_mock
)

def main():
    while True:
        print("\n=== SISTEMA DE CARGAS DO PORTO - Última Geração ===")
        print("1 - Ver Estatísticas")
        print("2 - Gerar Gráfico de Destinos")
        print("3 - Cadastrar Nova Carga")
        print("4 - Sair")
        print("5 - Gerar cargas de teste")
        opcao = input("Escolha uma opção: ").strip()

        cargas = carregar_dados()

        if opcao == "1":
            mostrar_estatisticas(cargas)
        elif opcao == "2":
            gerar_grafico(cargas)
        elif opcao == "3":
            cadastrar_carga(cargas)
        elif opcao == "4":
            print("Saindo... Até a próxima!")
            break
        elif opcao == "5":
            quantidade = input("Quantas cargas mock quer gerar? ").strip()
            if quantidade.isdigit() and int(quantidade) > 0:
                gerar_cargas_mock(int(quantidade))
            else:
                print("Digite um número válido para quantidade.")
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
