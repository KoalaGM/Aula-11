def main():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        
    except ValueError:
        print("Erro: Por favor, insira um número válido para as notas.")
    
    else:
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
            media = (nota1 + nota2) / 2
            print(f"A média do aluno é: {media:.2f}")
            
            if media >= 6:
                print("Aluno aprovado!")
            else:
                print("Aluno reprovado!")
        else:
            print("Erro: As notas devem estar entre 0 e 10.")
    
    finally:
        print("Programa encerrado.")


main()