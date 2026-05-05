# Projeto de Automação de Testes (E2E + API)

## Visão Geral

Este projeto implementa automação de testes cobrindo **frontend (E2E)** e **backend (API)**, garantindo validação completa da aplicação.

### Objetivo

Validar:

* Fluxo real de compra via interface web
* Operações CRUD via API
* Performance básica (tempo de resposta)

---

## Tecnologias Utilizadas

* Python 3.12
* unittest
* Selenium WebDriver
* ChromeDriver + WebDriver Manager
* Postman (Collection)
* Newman (execução automatizada)
* GitHub Actions (CI/CD)

---

## Estrutura do Projeto

```
PROJETO-AUTOMACAO
│
├── .github/workflows
│   ├── api-test.yml
│   └── test_selenium.yml
│
├── test
│   └── e2e
│       └── test_login.py
│
├── postman
│   ├── automation.postman_collection.json
│   └── postman_environment.json
│
├── venv
├── requirements.txt
└── README.md
```

---

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/Vinizx-carv/Projeto-automacao.git
cd Projeto-automacao
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

#### Ativar:

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Execução dos Testes

---

### 🔹 Teste E2E (Selenium)

```bash
python -m unittest discover -s test -p "test_*.py"
```

### ✔ Fluxo testado:

* Login
* Adição ao carrinho
* Checkout
* Finalização da compra

### ✔ Validação final:

O teste confirma a mensagem:

```
Thank you for your order!
```

---

### Testes de API (Postman)

---

### 1 — Via Postman (manual)

1. Importar:

   * `automation.postman_collection.json`
   * `postman_environment.json`
2. Definir variável:

```
baseURL = https://petstore.swagger.io/v2
```

3. Executar a collection

---

## Cobertura dos Testes

### Pet

* Criar
* Buscar
* Atualizar
* Deletar

### Store

* Criar pedido
* Consultar inventário
* Buscar pedido
* Deletar pedido

### User

* Criar usuário
* Buscar usuário
* Atualizar usuário
* Deletar usuário

---

## Validações Implementadas

### ✔ Funcionais

* Status HTTP = 200
* Dados retornados corretamente

### ✔ Performance

* Tempo de resposta < 500ms (alguns endpoints até 1000ms)

---

## Pipeline (CI/CD)

O projeto utiliza GitHub Actions para automação dos testes.

### Executa automaticamente:

* Testes E2E (Selenium)
* Testes de API (Newman)

### Benefícios:

* Validação contínua
* Detecção de regressões
* Execução automatizada a cada push

---

## Evidências (Prints)

### Selenium (E2E)

Adicionar:

* Tela de login
* Carrinho
* Checkout final com sucesso

---

### Postman / Newman

Adicionar:

* Execução completa da collection
* Todos os testes passando (verde)
* Tempo de resposta

---

## Pontos de Atenção

### 1. Variável obrigatória

Certifique-se de definir:

```
baseURL = https://petstore.swagger.io/v2
```

---

### 2. Execução Headless

O Selenium roda em modo headless (sem interface gráfica).
Para debug, remova:

```python
--headless
```

---

### 3. Tempo de resposta

Os limites variam entre:

* 500ms
* 1000ms

Para maior consistência, recomenda-se padronizar.

---


## Conclusão

O projeto valida de forma integrada:

* Interface (frontend)
* Serviços (backend)

Garantindo maior confiabilidade e qualidade da aplicação através de automação completa.

---
