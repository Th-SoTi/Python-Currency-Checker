# Sistema de Cotação de Moedas - Python

Este é um sistema simples, eficiente e intuitivo para obter a cotação atualizada das principais moedas: **Dólar (USD), Euro (EUR) e Bitcoin (BTC)**, utilizando a API da AwesomeAPI.

## 🔍 Funcionalidades

- Consulta em tempo real das cotações de **Dólar, Euro e Bitcoin**;
- Interface simples e interativa via terminal;
- Atualização automática ao selecionar uma nova consulta;
- Utiliza **requisições HTTP** para obter dados confiáveis e precisos;
- Sistema dinâmico com opção de **encerramento rápido**.

## 📚 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas:**
  - `requests` para conexão com a API de cotação
  - `json` para manipulação dos dados retornados
  - `os` para limpar o terminal e melhorar a experiência do usuário
  - `time` para pausas estratégicas no algoritmo

## 🛠️ Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Instale as dependências necessárias (caso não tenha `requests` instalado):
   ```bash
   pip install requests
   ```
4. Execute o script:
   ```bash
   python cotacao.py
   ```

## 🔨 Exemplo de Uso

Ao rodar o script, você verá o seguinte menu no terminal:

```
---Bem-vindo ao menu de cotações---
1. Cotações
2. Encerrar
-----------------------------------
Digite a opção:
```

Caso escolha "1. Cotações", poderá selecionar entre Dólar, Euro ou Bitcoin para obter a cotação em tempo real.

## 🏆 Diferenciais

- **Leve e rápido**: O código é otimizado para rodar em qualquer sistema com Python.
- **Atualização Automática**: As cotações são obtidas em tempo real diretamente da API.
- **Fácil de Usar**: Interface intuitiva com opções claras e objetivas.

## 🚀 Melhorias Futuras

- Adição de novas moedas e criptomoedas.
- Integração com interface gráfica.
- Exportação de dados para arquivos CSV ou JSON.

## 👤 Autor

Feito com ❤ por [SoTi](https://github.com/Th-SoTi). Sinta-se à vontade para contribuir e sugerir melhorias!

---

Se este projeto foi útil para você, deixe uma estrela no repositório! ⭐

