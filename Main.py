import customtkinter as ctk  # Importa a biblioteca CustomTkinter, que permite criar interfaces com tema escuro e estilos modernos

# Define o tema da interface
ctk.set_appearance_mode("dark")  # Define o modo escuro
ctk.set_default_color_theme("green")  # Define a cor padrão como verde

# Cria a janela principal do aplicativo
app = ctk.CTk()
app.title("Conversor Binário/Decimal")  # Define o título da janela
app.geometry("400x400")  # Define o tamanho da janela
app.resizable(False, False)  # Impede que a janela seja redimensionada

# Cria uma variável de controle para o modo de conversão
modo = ctk.StringVar(value="Binário -> Decimal")

# Função que quebra linhas de um texto muito longo para não sair da tela
def quebra_linha(texto, max_chars=15):
    return '\n'.join(texto[i:i+max_chars] for i in range(0, len(texto), max_chars))

# Função responsável pela conversão dos números
def converter():
    entrada = campo_entrada.get().strip()  # Obtém o valor digitado e remove espaços

    if not entrada:  # Verifica se está vazio
        resultado.configure(text="Digite um valor!", text_color="red")
        return

    if len(entrada) > 20:  # Limita a entrada a 20 caracteres
        resultado.configure(text="Máximo 20 caracteres!", text_color="red")
        return

    if modo.get() == "Binário -> Decimal":  # Se estiver no modo de binário para decimal
        try:
            decimal = int(entrada, 2)  # Converte de binário para decimal
            texto_resultado = str(decimal)
            resultado.configure(text=quebra_linha(texto_resultado), text_color="lime")
            adicionar_historico(f"Binário: {entrada} → Decimal: {texto_resultado}")
        except ValueError:
            resultado.configure(text="Entrada binária inválida", text_color="red")
    else:  # Se estiver no modo de decimal para binário
        try:
            decimal = int(entrada)  # Converte a string para inteiro
            binario = bin(decimal)[2:]  # Converte para binário e remove o prefixo '0b'
            texto_resultado = binario
            resultado.configure(text=quebra_linha(texto_resultado), text_color="cyan")
            adicionar_historico(f"Decimal: {entrada} → Binário: {texto_resultado}")
        except ValueError:
            resultado.configure(text="Entrada decimal inválida", text_color="red")

# Função para limpar os campos de entrada e resultado
def limpar():
    campo_entrada.delete(0, ctk.END)  # Limpa o campo de entrada
    resultado.configure(text="")  # Limpa o resultado

# Função que adiciona uma nova linha no histórico de conversões
def adicionar_historico(texto):
    historico.configure(state="normal")  # Ativa o campo para edição
    historico.insert(ctk.END, texto + "\n")  # Insere o texto no histórico
    historico.configure(state="disabled")  # Desativa para impedir edição manual
    historico.yview(ctk.END)  # Faz scroll automático para a última linha

# Elemento de texto (título)
texto_titulo = ctk.CTkLabel(app, text="Conversor Binário <-> Decimal", font=("Courier", 20, "bold"))
texto_titulo.pack(pady=15)

# Botão para selecionar o modo de conversão
seletor_modo = ctk.CTkSegmentedButton(app, values=["Binário -> Decimal", "Decimal -> Binário"], variable=modo)
seletor_modo.pack(pady=10)

# Campo onde o usuário digita o número a ser convertido
campo_entrada = ctk.CTkEntry(app, width=250, height=35, placeholder_text="Digite aqui...")
campo_entrada.pack(pady=10)

# Frame para organizar os botões lado a lado
frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10)

# Botão para executar a conversão
btn_converter = ctk.CTkButton(frame_botoes, text="Converter", command=converter, width=100)
btn_converter.grid(row=0, column=0, padx=10)

# Botão para limpar os campos
btn_limpar = ctk.CTkButton(frame_botoes, text="Limpar", command=limpar, width=80, fg_color="red")
btn_limpar.grid(row=0, column=1, padx=10)

# Label que exibe o resultado da conversão
resultado = ctk.CTkLabel(app, text="", font=("Courier", 18, "bold"))
resultado.pack(pady=15)

# Caixa de texto que mostra o histórico das conversões realizadas
historico = ctk.CTkTextbox(app, width=350, height=100, corner_radius=10, state="disabled", font=("Courier", 12))
historico.pack(pady=10)

# Mantém a janela aberta, executando o aplicativo
app.mainloop()
