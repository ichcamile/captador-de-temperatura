import tkinter as tk
from scraper import buscar_temperatura_umidade
from excel_handler import salvar_dados_em_excel
from datetime import datetime

def executar_busca():
    temperatura, umidade = buscar_temperatura_umidade()
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    if temperatura and umidade:
        salvar_dados_em_excel(agora, temperatura, umidade)
        resultado.config(text=f"Salvo: {temperatura} / {umidade}")
    else:
        resultado.config(text="Erro ao buscar dados.")

janela = tk.Tk()
janela.title("Captador de Temperatura - SP")

botao = tk.Button(janela, text="Buscar previsão", command=executar_busca)
botao.pack(pady=10)

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()
python main.py
