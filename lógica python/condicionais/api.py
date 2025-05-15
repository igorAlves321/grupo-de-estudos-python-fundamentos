import google.generativeai as genai

# Configuração da chave de API
genai.configure(api_key="AIzaSyA6euSkx8XJS0XR8S1UOWjDc45NxTn_UiU")

# Usando modelo funcional
modelo = genai.GenerativeModel(model_name="gemini-1.5-flash-001")

print("Bem-vindo ao ChatBot!")
print("Qual sua pergunta.")

pergunta = input("Qual sua pergunta: ")

if pergunta == '':
    print("Por favor, digite algo.")

elif pergunta == 'sair':
    print("Tchau!")

else:
    resposta = modelo.generate_content(pergunta)
    print("\nResposta:", resposta.text)

    print("Qual sua pergunta.")
    pergunta = input("Qual sua pergunta: ")

    if pergunta == '':
        print("Por favor, digite algo.")

    elif pergunta == 'sair':
        print("Tchau!")

    else:
        resposta = modelo.generate_content(pergunta)
        print("\nResposta:", resposta.text)
