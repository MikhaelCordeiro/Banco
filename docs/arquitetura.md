# Arquitetura do Projeto — Banco Terminal

## Visão Geral

Este projeto é um sistema bancário executado no terminal, escrito em Python, organizado em **Front-end (CLI)** e **Back-end (Regras de Negócio)**, com persistência em arquivos.

A arquitetura segue o princípio de **separação de responsabilidades**:

* Front-end **não decide regras**
* Back-end **não interage com o usuário**
* Persistência é isolada

---

## Diagrama Conceitual

Usuário
↓
Front-end (CLI)
↓
Back-end (Core Bancário)
↓
Persistência (Arquivos)

---

## Estrutura de Pastas

```
banco-terminal/
│
├── backend/
│   ├── core/
│   ├── storage/
│   └── utils/
│
├── frontend/
│   ├── main.py
│   ├── menu.py
│   ├── inputs.py
│   └── outputs.py
│
├── data/
│   ├── contas.json
│   └── transacoes.log
│
└── docs/
    └── arquitetura.md
```

---

## Back-end

### Objetivo

Concentrar **todas as regras críticas do banco**.

### `backend/core/`

Contém a lógica de negócio:

* contas bancárias
* autenticação
* transferências
* empréstimos

Regras importantes:

* Não usa `input()`
* Não usa `print()`
* Não acessa arquivos diretamente

### `backend/storage/`

Responsável pela persistência:

* leitura e escrita de arquivos
* criação de arquivos se não existirem
* garantia de consistência dos dados

### `backend/utils/`

Funções auxiliares reutilizáveis:

* hash de senha
* validações genéricas

---

## Front-end

### Objetivo

Interagir com o usuário via terminal.

Responsabilidades:

* exibir menus
* coletar entradas
* chamar funções do back-end
* exibir mensagens

Regras importantes:

* Não valida regras bancárias
* Não acessa arquivos
* Não altera dados diretamente

---

## Persistência

### Arquivos

* `contas.json`: dados principais (contas, saldo, senha hash, dívida)
* `transacoes.log`: histórico de operações

Somente o back-end acessa esses arquivos.

---

## Benefícios da Arquitetura

* Código limpo e organizado
* Fácil manutenção
* Evolução futura para API ou interface gráfica
* Padrão profissional para portfólio

---

## Regra de Ouro

> Se o front-end desaparecer, o banco ainda funciona.
