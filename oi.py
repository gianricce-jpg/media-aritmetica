print("-" * 50)
print("             CALCULADORA ARITMÉTICA      ")
print("-" * 50)
    
def quantidade_materia():
    qtd = int(input("Digite quantas matérias você tem (ex: 10) "))
    return qtd

def calcular_media(quantidade):
    soma_notas = 0
    for i in range(quantidade):
        while True:
                nota = float(input(f"Digite a nota da {i + 1}ª matéria (ex: 0.0 10.0): "))
                if 0.0 <= nota <= 10.0:
                    soma_notas += nota
                    break 
                else:
                    print("Nota inválida! Digite um valor entre 0.0 e 10.0.")

    media = soma_notas / quantidade 
    return media

def dar_resultado(media_final):
    print(f"\nMédia Final: {media_final:.1f}")
    if media_final >= 8.0:
        print("Parebéns você foi: APROVADO E GANHOU CERTIFICADO! 🏆")
    elif media_final >= 6.0:
        print(" Parebéns você foi: APROVADO ✅")
    elif 5.0 <= media_final < 6.0:
        print("EM RECUPERAÇÃO, Estude mais para a prova final ⚠️")
    else:
        print("REPROVADO❌, Te vejo ano que vem!!")
        

                    
qtd = quantidade_materia()
media = calcular_media(qtd)
dar_resultado(media)

print("-" * 50)
print("      CALCULADORA ARITMÉTICA      ")
print("-" * 50)