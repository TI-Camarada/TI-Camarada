import tkinter as tk
import CalcMaisValia
from PIL import Image, ImageTk

principal = tk.Tk()
principal.title("Mais-Valia = valor que o trabalhador produz mas não recebe")
principal.configure(bg="#800000")

quadro = tk.LabelFrame(principal, padx=20, pady=20, bg="#d9a040", bd=0)
quadro.pack(padx=25, pady=25)

explicacao = tk.Label(
    principal,
    padx=12, pady=4,
    text="*Digite os valores no seguinte formato, ex: 2100000.35",
    bg="#003300", fg="#33ff33", bd=10, font=("monospace", 12)
)
explicacao.pack(pady=(0, 8))

titulo = tk.Label(
    quadro,
    text="Calcule a Mais-Valia",
    padx=6, pady=2,
    bg="#ffbf00",
    font=("Consolas", 28, "bold")
)
titulo.pack(anchor="n", side="top", pady=(1, 10))

# Campos de entrada
tk.Label(quadro, text="\nLucro anual da empresa(R$):", bg="#d9a040", font=("Consolas", 14, "bold")).pack()
entrada_lucro = tk.Entry(quadro, font=("Consolas", 14, "bold"))
entrada_lucro.pack(anchor="n", pady=(7, 12))

tk.Label(quadro, text="Salário mensal do funcionário(R$):", bg="#d9a040", font=("Consolas", 14, "bold")).pack()
entrada_salario = tk.Entry(quadro, font=("Consolas", 14, "bold"))
entrada_salario.pack(anchor="n", pady=(7, 12))

tk.Label(quadro, text="Número de funcionários:", bg="#d9a040", font=("Consolas", 14, "bold")).pack()
entrada_funcionarios = tk.Entry(quadro, font=("Consolas", 14, "bold"))
entrada_funcionarios.pack(anchor="n", pady=(7, 7))


# Para manter referência da imagem
img_tk_global = None

def executar_calculo():
    global img_tk_global
    try:
        lucro = float(entrada_lucro.get())
        salario = float(entrada_salario.get())
        funcionarios = int(entrada_funcionarios.get())

        # Obter resultado do cálculo
        resultado = CalcMaisValia.calcular_mais_valia(lucro, salario, funcionarios)

        # Separar corpo e frase final
        partes = resultado.strip().rsplit("\n", 1)
        corpo = partes[0]
        frase_final = partes[1] if len(partes) > 1 else ""

        resultado_widget.config(state="normal")
        resultado_widget.delete("1.0", tk.END)

        # Configurar estilos
        resultado_widget.tag_config("corpo", font=("Consolas", 13, "bold"),lmargin1=18, lmargin2=18)
        resultado_widget.tag_config("frase",
                                    font=("Consolas", 16, "bold"),
                                    foreground="#800000",
                                    lmargin1=20,
                                    justify="center",
                                    spacing1=10)

        # Inserir texto
        resultado_widget.insert(tk.END, corpo + "\n", "corpo")
        resultado_widget.insert(tk.END, frase_final + "\n", "frase")

        # Carregar e redimensionar imagem (4x maior que antes → 256px)
        img_original = Image.open("foice_martelo.png")
        img_redimensionada = img_original.resize((200, 200), Image.NEAREST)
        img_tk_global = ImageTk.PhotoImage(img_redimensionada)

        # Centralizar imagem
        largura_texto = int(resultado_widget['width']) * 8  # aprox. px por caractere
        largura_imagem = img_tk_global.width()
        espacos = (largura_texto - largura_imagem) // 16
        resultado_widget.insert(tk.END, " " * espacos)
        resultado_widget.image_create(tk.END, image=img_tk_global)
        resultado_widget.insert(tk.END, "\n")

        resultado_widget.config(state="disabled")

    except ValueError:
        resultado_widget.config(state="normal")
        resultado_widget.delete("1.0", tk.END)
        resultado_widget.insert(tk.END, "Por favor, preencha os campos corretamente.")
        resultado_widget.config(state="disabled")

# Botão
botao = tk.Button(
    quadro,
    text="CALCULAR",
    font=("Consolas", 16, "bold"),
    bg="#003300",
    fg="#33ff33",
    activebackground="#005500",
    activeforeground="#66ff66",
    relief="groove",
    bd=3,
    padx=20,
    pady=6,
    command=executar_calculo
)
botao.pack(pady=(12, 12))

# Resultado
resultado_widget = tk.Text(
    quadro,
    width=66,
    height=16,
    bg="#ffbf00",
    fg="black",
    font=("Consolas", 12),
    wrap="word",
    bd=8,
    padx=10,
    pady=12,
    spacing1=3,
    spacing3=3
)
resultado_widget.pack(pady=(15, 10))
resultado_widget.config(state="disabled")
principal.mainloop()
