import tkinter as tk


# Def do calculo por trás do programa, faz os cálculos
def calcular_preco():
    # Verificar se há algo digitado nas entradas e atribuir os valores padrão se estiverem vazias
    altura_tecido = int(altura_tecido_entry.get()) if altura_tecido_entry.get() else 115
    largura_tecido = (
        int(largura_tecido_entry.get()) if largura_tecido_entry.get() else 556
    )
    preco_tecido = float(preco_tecido_entry.get()) if preco_tecido_entry.get() else 13

    area_tecido = altura_tecido * largura_tecido

    altura_peca = int(altura_peca_entry.get())
    largura_peca = int(largura_peca_entry.get())

    area_peca = altura_peca * largura_peca

    preco_peca = (area_peca * preco_tecido) / area_tecido

    quantidade_peca = area_tecido / area_peca

    resultado_label.config(text="O preço da peça é € {:.2f}".format(preco_peca))
    pecas_label.config(
        text=f"Com as medidas de {altura_peca} x {largura_peca}, você pode fazer {quantidade_peca:.0f} peças."
    )


# abrir a janela
root = tk.Tk()
root.title("Calculadora de Preço de Peça")
root.geometry("400x300")  # Definindo o tamanho da janela

fonte = ("Arial", 12)  # Definindo a fonte

# Definindo os widgets dentro da janela
altura_tecido_label = tk.Label(root, text="Altura do tecido (cm):", font=fonte)
altura_tecido_entry = tk.Entry(root, font=fonte)
largura_tecido_label = tk.Label(root, text="Largura do tecido (cm):", font=fonte)
largura_tecido_entry = tk.Entry(root, font=fonte)
preco_tecido_label = tk.Label(root, text="Preço do tecido (€):", font=fonte)
preco_tecido_entry = tk.Entry(root, font=fonte)

altura_peca_label = tk.Label(root, text="Altura da peça (cm):", font=fonte)
altura_peca_entry = tk.Entry(root, font=fonte)
largura_peca_label = tk.Label(root, text="Largura da peça (cm):", font=fonte)
largura_peca_entry = tk.Entry(root, font=fonte)

calcular_button = tk.Button(root, text="Calcular", command=calcular_preco, font=fonte)
resultado_label = tk.Label(root, text="", font=fonte)
pecas_label = tk.Label(root, text="", font=fonte)

# Posicionando os widgets na janela
altura_tecido_label.grid(row=0, column=0, sticky="e")
altura_tecido_entry.grid(row=0, column=1)
largura_tecido_label.grid(row=1, column=0, sticky="e")
largura_tecido_entry.grid(row=1, column=1)
preco_tecido_label.grid(row=2, column=0, sticky="e")
preco_tecido_entry.grid(row=2, column=1)

altura_peca_label.grid(row=3, column=0, sticky="e")
altura_peca_entry.grid(row=3, column=1)
largura_peca_label.grid(row=4, column=0, sticky="e")
largura_peca_entry.grid(row=4, column=1)

calcular_button.grid(row=5, column=0, columnspan=2)
resultado_label.grid(row=6, column=0, columnspan=2)
pecas_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
