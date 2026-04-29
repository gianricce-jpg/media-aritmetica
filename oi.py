def quantidade_materia():
    qtd = int(input("Digite quantas matérias você tem (ex:10) "))
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
    print(f"\n Media Final: {media_final:.1f}")
    if media_final >= 8.0:
        print("Parabéns, você passou e ganhou o CERTIFICADO.")
        
    elif media_final >= 6.0:
        print("Parabéns, você passou.")
        
    else:
        print("Você não passou, melhore.")
        
        
qtd = quantidade_materia()
media = calcular_media(qtd)
dar_resultado(media)