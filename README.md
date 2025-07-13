## 📡 Captador de Temperatura de São Paulo

Projeto de automação para captar **temperatura**, **umidade** e **vento** atuais da cidade de São Paulo, diretamente do site [ClimaTempo](https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp). Os dados são salvos automaticamente em uma planilha `.xlsx`.


### 🧠 Objetivo

Automatizar a coleta de informações climáticas usando Python e Selenium, salvando os dados com marcação de data/hora para criar um histórico.


### 🛠️ Tecnologias utilizadas

* Python 3.13
* Selenium
* openpyxl
* Firefox + GeckoDriver


### 📁 Estrutura de Arquivos

```
captador-de-temperatura/
│
├── src/
│   ├── main.py                # Script principal
│   ├── scraper.py             # Lógica de raspagem dos dados do ClimaTempo
│   └── excel_handler.py       # Manipulação da planilha Excel
│
├── dados_clima.xlsx           # Planilha gerada com os dados (criada após execução)
├── README.md                  # Documentação do projeto
```

---

### ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/ichcamile/captador-de-temperatura.git
cd captador-de-temperatura/src
```

2. Instale as dependências:

```bash
pip install selenium openpyxl
```

3. Certifique-se de ter o navegador **Firefox** instalado e o **GeckoDriver** configurado no PATH.

4. Execute o script:

```bash
python main.py
```

### ✅ Saída esperada

O terminal mostrará:

```
[✔] Temperatura: 20°C
[✔] Umidade: 84%
[✔] Vento: 13 km/h
[✔] Dados salvos em dados_clima.xlsx
```

E a planilha `dados_clima.xlsx` será atualizada com:

| Data/Hora           | Temperatura | Umidade | Vento   |
| ------------------- | ----------- | ------- | ------- |
| 13/07/2025 22:40:12 | 20°C        | 84%     | 13 km/h |


### 📊 Aprendizados

* Identificar elementos usando XPath
* Trabalhar com automação no navegador com Selenium
* Manipular arquivos Excel com Python
* Organizar código com módulos reutilizáveis
