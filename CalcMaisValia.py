def calcular_mais_valia(lucro, salario_mensal, funcionarios):
    if funcionarios <= 0:
        return "O número de funcionários deve ser maior que zero."

    salario_anual = salario_mensal * 12
    encargos = salario_anual * 0.35
    custo_total_funcionario = salario_anual + encargos

    folha_total = custo_total_funcionario * funcionarios
    total_distribuivel = folha_total + lucro

    valor_justo_por_funcionario = total_distribuivel / funcionarios
    valor_justo_sem_encargos = valor_justo_por_funcionario - (valor_justo_por_funcionario * 0.35)
    aumento_necessario = valor_justo_por_funcionario - custo_total_funcionario
    percentual_aumento = (aumento_necessario / custo_total_funcionario) * 100

    return f"""\nResultados:
Salário se o lucro fosse distribuído: R$ {valor_justo_sem_encargos/12:.2f}
MAIS-VALIA mensal: R$ {aumento_necessario/12:.2f}
Aumento necessário: {percentual_aumento:.1f}%\n
Se nós produzimos a riqueza, ela pertence a nós!"""
