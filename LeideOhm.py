# Lei de Ohm
# Esse código utiliza a lei de Ohm para descobrir a resistência elétrica utilizando a fórmula V = R*I.

import tkinter as tk

corfundo = "#054F77"

def LeideOhm():
    try:
        i = float(entrada1.get())
        v = float(entrada2.get())
        r = v/i
        resultado3 = f"A resistência dessa corrente elétrica é de: {r:.4f}".rstrip("0").rstrip(".") + " ohms."
        exibirResultado.config(text=f'{resultado3}')

    except ValueError:
        exibirResultado2.config(text="Valor inválido, tente novamente.")

# Criando Janela
janela = tk.Tk()
janela.title("Calculando Lei de Ohm")
janela.resizable("False", "False")
# Cor de fundo
janela.config(bg=corfundo)

# Definindo tamanho. Por que tá dando erro...? Ata, descobri.
janela.geometry("600x500")

# Entrada pro cara digitar os treco
# Corrente em amperes
entrada1 = tk.Entry(janela, width=20, font=20)
entrada1.grid(row = 2, column= 2,pady=20)
titulo_da_entrada = tk.Label(text="Coloque a corrente elétrica em amperes aqui.", width=35, font=10)
titulo_da_entrada.grid(row = 1, column= 2, pady=20)

# Tensão em volts
entrada2 = tk.Entry(janela, width=20, font=20)
entrada2.grid(row = 5, column= 2, pady=20)
titulo_da_entrada2 = tk.Label(text="Coloque a tensão em volts aqui.", width=35, font=10)
titulo_da_entrada2.grid(row = 4, column= 2, pady=20)


# botão pra rodar o calculo
iniciar = tk.Button(text="Pressione aqui para ver a resistência.", command=LeideOhm, width=35, font=0.2)
iniciar.grid(row = 7, column= 2, padx=75)

# Label que vai exibir o nosso resultado
exibirResultado = tk.Label(janela)
exibirResultado.config(bg=corfundo, fg="white", font=2, padx=20)
exibirResultado.grid(row = 10, column= 2, pady=40)

exibirResultado2 = tk.Label(janela)
exibirResultado2.config(bg=corfundo, fg="black", font=2)
exibirResultado2.grid(row = 11, column= 2, pady=20)


# Rodando janela.
janela.mainloop()