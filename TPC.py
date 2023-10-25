
#Para ler o número de capitulos

def contar_capitulos(nome_arquivo): 
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            # Suponha que cada capítulo comece com a palavra "Capítulo" seguida de um número
            capitulos = texto.count('# ')
            return capitulos
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = 'camilo\obra\Camilo-A_Brasileira_de_Prazins.md'  # Substitua com o nome do arquivo do seu livro
    numero_de_capitulos = contar_capitulos(nome_arquivo)
    
    if isinstance(numero_de_capitulos, int):
        print(f"O livro tem {numero_de_capitulos} capítulos.")
    else:
        print(numero_de_capitulos)


    
#Para ler a quantidade de frases

#import nltk
#nltk.download('punkt')  # Certifique-se de baixar o tokenizer do NLTK se ainda não o fez

from nltk.tokenize import sent_tokenize

def contar_frases(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            frases = sent_tokenize(texto)
            return len(frases)
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = 'camilo\obra\Camilo-A_Brasileira_de_Prazins.md'  # Substitua com o nome do arquivo do seu livro
    numero_de_frases = contar_frases(nome_arquivo)
    
    if isinstance(numero_de_frases, int):
        print(f"O livro tem {numero_de_frases} frases.")
    else:
        print(numero_de_frases)





#Para verificar o comprimento médio das frases

from nltk.tokenize import sent_tokenize

def calcular_comprimento_medio_das_frases(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            frases = sent_tokenize(texto)
            
            total_caracteres = sum(len(frase) for frase in frases)
            numero_de_frases = len(frases)
            
            if numero_de_frases > 0:
                comprimento_medio = total_caracteres / numero_de_frases
                return comprimento_medio
            else:
                return 0
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = 'camilo\obra\Camilo-A_Brasileira_de_Prazins.md'  # Substitua com o nome do arquivo do seu livro
    comprimento_medio_das_frases = calcular_comprimento_medio_das_frases(nome_arquivo)
    
    if isinstance(comprimento_medio_das_frases, float):
        print(f"O comprimento médio das frases é aproximadamente {comprimento_medio_das_frases:.2f} caracteres.")
    else:
        print(comprimento_medio_das_frases)





