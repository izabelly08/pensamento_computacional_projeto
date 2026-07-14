# ===========================================
# SISTEMA DE VENDAS - PADARIA
# ===========================================

produtos = [
    {"nome": "Pão Francês", "preco": 0.80, "estoque": 100},
    {"nome": "Pão de Queijo", "preco": 3.50, "estoque": 50},
    {"nome": "Coxinha", "preco": 6.00, "estoque": 30},
    {"nome": "Bolo de Chocolate", "preco": 8.00, "estoque": 20},
    {"nome": "Café", "preco": 3.00, "estoque": 40}
]

vendas = []

while True:

    print("\n" + "=" * 50)
    print("         SISTEMA DE VENDAS - PADARIA")
    print("=" * 50)
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Realizar Venda")
    print("4 - Suporte")
    print("5 - Relatório de Vendas")
    print("6 - Gerenciar Estoque")
    print("7 - Cardápio")
    print("8 - Promoções")
    print("9 - Feedback")
    print("0 - Sair")
    print("=" * 50)

    opcao = input("Escolha uma opção: ")

    # CADASTRAR PRODUTO
    
    if opcao == "1":

        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        estoque = int(input("Quantidade em estoque: "))

        produtos.append({
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        })

        print("Produto cadastrado com sucesso!")
        
        

  
    # LISTAR PRODUTOS
  
    elif opcao == "2":

        print("\nLISTA DE PRODUTOS\n")

        for i, produto in enumerate(produtos):
            print(f"{i+1} - {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Estoque: {produto['estoque']}")
            print("-" * 30)

   
    # REALIZAR VENDA
    
    elif opcao == "3":

        print("\nCARDÁPIO")

        for i, produto in enumerate(produtos):
            print(f"{i+1} - {produto['nome']} - R$ {produto['preco']:.2f}")

        codigo = int(input("Código do produto: ")) - 1

        if codigo < 0 or codigo >= len(produtos):
            print("Produto inválido.")
            continue

        quantidade = int(input("Quantidade: "))

        if quantidade > produtos[codigo]["estoque"]:
            print("Estoque insuficiente.")
            continue

        total = quantidade * produtos[codigo]["preco"]

        produtos[codigo]["estoque"] -= quantidade

        vendas.append({
            "produto": produtos[codigo]["nome"],
            "quantidade": quantidade,
            "total": total
        })

        print("\n========== CUPOM ==========")
        print("Produto:", produtos[codigo]["nome"])
        print("Quantidade:", quantidade)
        print(f"Total: R$ {total:.2f}")
        print("===========================")

    # SUPORTE

    elif opcao == "4":

        print("\nSUPORTE")
        print("Telefone: (11) 99999-9999")
        print("E-mail: suporte@padaria.com")

    
    # RELATÓRIO
   
    elif opcao == "5":

        print("\nRELATÓRIO DE VENDAS")

        if len(vendas) == 0:
            print("Nenhuma venda realizada.")
        else:

            total_geral = 0

            for venda in vendas:
                print(f"{venda['produto']} - {venda['quantidade']} unidade(s)")
                print(f"Valor: R$ {venda['total']:.2f}")
                total_geral += venda["total"]
                print("-" * 30)

            print(f"TOTAL GERAL: R$ {total_geral:.2f}")

   
    # ESTOQUE
   
    elif opcao == "6":

        print("\nESTOQUE")

        for produto in produtos:
            print(f"{produto['nome']} - {produto['estoque']} unidades")

   
    # CARDÁPIO
  
    elif opcao == "7":

        print("\n" + "=" * 55)
        print("              CARDÁPIO DA PADARIA")
        print("=" * 55)

        print(f'{"CÓD":<5}{"PRODUTO":<25}{"PREÇO":<10}{"ESTOQUE"}')
        print("-" * 55)

        for i, produto in enumerate(produtos):
            print(f'{i+1:<5}{produto["nome"]:<25}R$ {produto["preco"]:<7.2f}{produto["estoque"]}')

        print("=" * 55)

    
    # PROMOÇÕES
  
    elif opcao == "8":

        print("\nPROMOÇÕES")
        print("🥖 Pão Francês: Leve 10 e pague 9")
        print("☕ Café + Pão de Queijo: R$ 5,99")
        print("🍰 Café + Bolo: R$ 9,90")

    
    # FEEDBACK
    
    elif opcao == "9":

        feedback = input("Digite seu feedback: ")
        print("Obrigado pela sua opinião!")

    
    # SAIR
    elif opcao == "0":

        print("\nObrigado por utilizar nosso sistema!")
        print("Volte sempre!")
        break

   
    # OPÇÃO INVÁLIDA
    
    else:
        print("Opção inválida! Tente novamente.")