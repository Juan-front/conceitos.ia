# conceitos_ia.py

def obter_descricao(categoria, termo):
    mapas = {
        "conceitos_gerativos": {
            "Modelos de Linguagem": "IA treinada em textos para prever e gerar linguagem natural.",
            "Treinamento Supervisionado": "Aprendizado com dados rotulados para ensinar a IA a prever.",
            "Prompt Engineering": "Técnica para guiar modelos via comandos (prompts) escritos.",
            "Modelos Diffusion": "Modelo que gera imagens por refinamentos iterativos do ruído.",
        },
        "ferramentas_aws": {
            "Amazon Bedrock": "Serviço de acesso via API a múltiplos modelos fundacionais.",
            "Amazon Titan": "Modelos base da AWS para gerar e resumir texto.",
            "Amazon Q": "Assistente de IA para devs e TI integrado aos serviços AWS.",
            "AWS Trainium": "Chip da AWS para treinar modelos de ML em larga escala.",
        },
        "termos_tecnicos": {
            "Token": "Unidade de texto que modelos de linguagem processam.",
            "Fine-tuning": "Adapta um modelo treinado com dados novos e específicos.",
            "Inference": "Uso do modelo treinado para gerar saída da entrada.",
            "Dataset": "Conjunto de dados para treinar ou ajustar um modelo de IA.",
        },
    }

    categoria_map = mapas.get(categoria)
    if not categoria_map:
        return "Categoria inválida. Use: conceitos_gerativos, ferramentas_aws ou termos_tecnicos."

    return categoria_map.get(termo, "Termo não encontrado nessa categoria.")

def listar_termos(categoria):
    listas = {
        "conceitos_gerativos": [
            "Modelos de Linguagem",
            "Treinamento Supervisionado",
            "Prompt Engineering",
            "Modelos Diffusion",
        ],
        "ferramentas_aws": [
            "Amazon Bedrock",
            "Amazon Titan",
            "Amazon Q",
            "AWS Trainium",
        ],
        "termos_tecnicos": [
            "Token",
            "Fine-tuning",
            "Inference",
            "Dataset",
        ],
    }
    return listas.get(categoria, [])

def menu():
    print("\n=== Dicionário de IA Generativa ===")
    print("Categorias disponíveis:")
    print("1) conceitos_gerativos")
    print("2) ferramentas_aws")
    print("3) termos_tecnicos")
    print("4) sair")

def main():
    while True:
        menu()
        escolha = input("\nDigite a categoria (ou 'sair'): ").strip().lower()

        if escolha == "sair" or escolha == "4":
            print("Encerrando. Até mais!")
            break

        # Normaliza entradas numéricas para nomes
        mapa_num = {
            "1": "conceitos_gerativos",
            "2": "ferramentas_aws",
            "3": "termos_tecnicos",
        }
        categoria = mapa_num.get(escolha, escolha)

        termos = listar_termos(categoria)
        if not termos:
            print("Categoria inválida. Tente novamente.")
            continue

        print("\nTermos disponíveis nessa categoria:")
        for t in termos:
            print(f"- {t}")

        termo = input("\nDigite exatamente um termo da lista: ").strip()
        descricao = obter_descricao(categoria, termo)
        print(f"\nDescrição: {descricao}")

if __name__ == "__main__":
    main()