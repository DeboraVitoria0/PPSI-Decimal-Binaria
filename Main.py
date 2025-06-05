import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Conversor Binário/Decimal")
app.geometry("400x400")
app.resizable(False, False)

modo = ctk.StringVar(value="Binário -> Decimal")

def quebra_linha(texto, max_chars=15):
    return '\n'.join(texto[i:i+max_chars] for i in range(0, len(texto), max_chars))

def converter():
    entrada = campo_entrada.get().strip()

    if not entrada:
        resultado.configure(text="Digite um valor!", text_color="red")
        return

    if len(entrada) > 20:
        resultado.configure(text="Máximo 20 caracteres!", text_color="red")
        return

    if modo.get() == "Binário -> Decimal":
        try:
            decimal = int(entrada, 2)
            texto_resultado = str(decimal)
            resultado.configure(text=quebra_linha(texto_resultado), text_color="lime")
            adicionar_historico(f"Binário: {entrada} → Decimal: {texto_resultado}")
        except ValueError:
            resultado.configure(text="Entrada binária inválida", text_color="red")
    else:
        try:
            decimal = int(entrada)
            binario = bin(decimal)[2:]
            texto_resultado = binario
            resultado.configure(text=quebra_linha(texto_resultado), text_color="cyan")
            adicionar_historico(f"Decimal: {entrada} → Binário: {texto_resultado}")
        except ValueError:
            resultado.configure(text="Entrada decimal inválida", text_color="red")

def limpar():
    campo_entrada.delete(0, ctk.END)
    resultado.configure(text="")

def adicionar_historico(texto):
    historico.configure(state="normal")
    historico.insert(ctk.END, texto + "\n")
    historico.configure(state="disabled")
    historico.yview(ctk.END)

texto_titulo = ctk.CTkLabel(app, text="Conversor Binário <-> Decimal", font=("Courier", 20, "bold"))
texto_titulo.pack(pady=15)

seletor_modo = ctk.CTkSegmentedButton(app, values=["Binário -> Decimal", "Decimal -> Binário"], variable=modo)
seletor_modo.pack(pady=10)

campo_entrada = ctk.CTkEntry(app, width=250, height=35, placeholder_text="Digite aqui...")
campo_entrada.pack(pady=10)

frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10)

btn_converter = ctk.CTkButton(frame_botoes, text="Converter", command=converter, width=100)
btn_converter.grid(row=0, column=0, padx=10)

btn_limpar = ctk.CTkButton(frame_botoes, text="Limpar", command=limpar, width=80, fg_color="red")
btn_limpar.grid(row=0, column=1, padx=10)

resultado = ctk.CTkLabel(app, text="", font=("Courier", 18, "bold"))
resultado.pack(pady=15)

historico = ctk.CTkTextbox(app, width=350, height=100, corner_radius=10, state="disabled", font=("Courier", 12))
historico.pack(pady=10)

app.mainloop()