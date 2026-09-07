nome= input("Digite o nome do aparelho: ")
potencia= float(input(" potência do aparelho em watts (W): "))
tempo_medio= float(input("Digite o tempo médio de uso diário em horas: "))
consumoMensal = (potencia * tempo_medio * 30) / 1000

print(f"aparelho: {nome}")
print(f"potencia:{potencia:.2f} w")
print(f"consumo estimado:{consumoMensal:.2f} kwh/mes")
print(f"custo estimado:R$ {consumoMensal*0.90:.2f} reais/mensais")
