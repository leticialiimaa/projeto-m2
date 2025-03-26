import webbrowser


def mostrar_introducao():
    mensagem = """
    *****************************************
    *  Bem-vindo à Calculadora Nutricional! *
    *                                       *
    *  Este programa fornecerá uma base     *
    *  sobre suas necessidades nutricionais.*
    *                                       *
    *  IMPORTANTE: Consulte sempre um       *
    *  médico ou nutricionista para         *
    *  orientações personalizadas.          *
    *****************************************

    Dica: Para acompanhar sua alimentação, visite:
    https://www.fatsecret.com.br/
    """
    print(mensagem)


def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)"""
    return peso / (altura ** 2)


def classificar_imc(imc):
    """Classifica o IMC em categorias de peso"""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


def calcular_tmb(sexo, peso, altura, idade):
    """Calcula a Taxa Metabólica Basal (TMB)"""
    altura_cm = altura * 100
    if sexo == 'm':
        return 88.36 + (13.4 * peso) + (4.8 * altura_cm) - (5.7 * idade)
    else:
        return 447.6 + (9.2 * peso) + (3.1 * altura_cm) - (4.3 * idade)


def ajustar_calorias_por_objetivo(tmb, objetivo):
    """Ajusta as calorias com base no objetivo"""
    if objetivo == 'perder':
        return tmb * 0.8  # redução de 20%
    elif objetivo == 'ganhar':
        return tmb * 1.2  # aumento de 20%
    else:
        return tmb  # manter o peso


def gerar_plano_treino(objetivo):
    """Gera um plano de treino básico"""
    planos = {
        'perder': [
            "\nDia 1: Cardio e corpo inteiro\n- 30 min caminhada/corrida\n- Agachamentos: 3x15\n- Flexões: 3x10",
            "\nDia 2: Descanso ativo\n- Alongamentos ou yoga",
            "\nDia 3: HIIT\n- 20 min treino intervalado",
            "\nDia 4: Treino de força\n- Exercícios com peso corporal",
            "\nDia 5: Descanso"
        ],
        'ganhar': [
            "\nDia 1: Treino de força (superior)\n- Supino: 4x8\n- Barra fixa: 4x5",
            "\nDia 2: Descanso",
            "\nDia 3: Treino de força (inferior)\n- Agachamento: 4x8\n- Afundos: 3x10",
            "\nDia 4: Descanso",
            "\nDia 5: Treino completo"
        ],
        'manter': [
            "\nDia 1: Cardio moderado\n- 30-45 min atividade aeróbica",
            "\nDia 2: Treino de força\n- Exercícios com peso corporal",
            "\nDia 3: Descanso ativo\n- Caminhada ou alongamentos",
            "\nDia 4: Treino intervalado\n- 20 min HIIT",
            "\nDia 5: Descanso"
        ]
    }
    return planos.get(objetivo, planos['manter'])


def obter_sexo():
    """Obtém e valida o sexo do usuário"""
    while True:
        sexo = input("\nSexo (M/F): ").strip().lower()
        if sexo in ['m', 'f']:
            return sexo
        print("Por favor, insira 'M' para masculino ou 'F' para feminino.")


def obter_peso():
    """Obtém e valida o peso do usuário"""
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if 0 < peso < 600:
                return peso
            print("Por favor, insira um peso válido entre 0 e 600kg.")
        except ValueError:
            print("Por favor, insira um número válido para o peso.")


def obter_altura():
    """Obtém e valida a altura do usuário"""
    while True:
        try:
            altura = float(input("Altura (m): "))
            if altura > 0.6:
                if altura > 2.51:
                    print("Altura impressionante!")
                return altura
            print("Por favor, insira uma altura válida acima de 0.6m.")
        except ValueError:
            print("Por favor, insira um número válido para a altura.")


def obter_idade():
    """Obtém e valida a idade do usuário"""
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                if idade > 127:
                    print("Idade impressionante!")
                return idade
            print("Por favor, insira uma idade válida maior que zero.")
        except ValueError:
            print("Por favor, insira um número inteiro válido para a idade.")


def obter_objetivo(imc):
    """Obtém o objetivo do usuário com sugestão baseada no IMC"""
    if imc < 18.5:
        print("\nSeu IMC sugere que você está abaixo do peso.")
        print("Sugestão: Objetivo 'ganhar' peso")
    elif imc >= 25:
        print("\nSeu IMC sugere que você está acima do peso.")
        print("Sugestão: Objetivo 'perder' peso")
    else:
        print("\nSeu IMC está na faixa considerada normal.")
        print("Sugestão: Objetivo 'manter' peso")

    while True:
        objetivo = input("\nQual seu objetivo? (perder/manter/ganhar): ").strip().lower()
        if objetivo in ['perder', 'manter', 'ganhar']:
            return objetivo
        print("Por favor, insira 'perder', 'manter' ou 'ganhar'.")


def mostrar_recomendacoes():
    """Mostra recomendações importantes"""
    print("\n" + "=" * 60)
    print("RECOMENDAÇÕES IMPORTANTES:")
    print("- Este programa fornece apenas uma estimativa básica")
    print("- Para uma avaliação precisa, consulte um nutricionista")
    print("- Para acompanhar sua dieta, visite: https://www.fatsecret.com.br/")
    print("- Mantenha hábitos saudáveis e pratique exercícios regularmente")
    print("=" * 60 + "\n")


def abrir_fatsecret():
    """Pergunta se o usuário deseja abrir o FatSecret"""
    while True:
        resposta = input("Deseja abrir o site do FatSecret agora? (sim/nao): ").lower().strip()
        if resposta == 'sim':
            webbrowser.open("https://www.fatsecret.com.br/")
            break
        elif resposta == 'nao':
            break
        else:
            print("Por favor, responda com 'sim' ou 'nao'.")


def executar_programa():
    """Função principal do programa"""
    mostrar_introducao()
    input("Pressione Enter para começar...")

    # Coletar dados do usuário
    sexo = obter_sexo()
    peso = obter_peso()
    altura = obter_altura()
    idade = obter_idade()

    # Calcular métricas
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    tmb = calcular_tmb(sexo, peso, altura, idade)

    # Obter objetivo e ajustar calorias
    objetivo = obter_objetivo(imc)
    calorias_ajustadas = ajustar_calorias_por_objetivo(tmb, objetivo)

    # Gerar plano de treino
    plano_treino = gerar_plano_treino(objetivo)

    # Exibir resultados
    print("\n" + "=" * 40)
    print("RESULTADOS:")
    print(f"IMC: {imc:.2f} ({classificacao})")
    print(f"Taxa Metabólica Basal: {round(tmb)} kcal/dia")
    print(f"Calorias recomendadas: {round(calorias_ajustadas)} kcal/dia")
    print("=" * 40 + "\n")

    print("\nSUGESTÃO DE TREINO:")
    for dia in plano_treino:
        print(dia)

    mostrar_recomendacoes()
    abrir_fatsecret()


def perguntar_continuar():
    """Pergunta se o usuário deseja continuar"""
    while True:
        resposta = input("\nDeseja fazer outra avaliação? (sim/nao): ").lower().strip()
        if resposta == 'sim':
            return True
        elif resposta == 'nao':
            print("\nObrigado por usar nossa calculadora nutricional!")
            print("Lembre-se: para orientações personalizadas, consulte sempre um profissional de saúde.")
            return False
        print("Por favor, responda com 'sim' ou 'nao'.")


# Ponto de entrada do programa
if __name__ == "__main__":
    executar_programa()
    while perguntar_continuar():
        executar_programa()