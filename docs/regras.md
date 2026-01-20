# Regras do Sistema Bancário

Este documento define **todas as regras de negócio** do banco. Qualquer implementação deve seguir estas regras.

---

## 1. Conta Bancária

Cada conta possui:

* identificador único
* nome do usuário
* senha (armazenada como hash)
* saldo
* dívida ativa (se houver)
* status (ativa / bloqueada)

---

## 2. Cadastro

### Regras

* Identificador deve ser único
* Senha **nunca** é armazenada em texto puro
* Saldo inicial não pode ser negativo

### Resultado esperado

* Conta criada
* Conta persistida em arquivo

---

## 3. Login

### Regras

* Usuário inexistente → falha
* Senha incorreta → falha
* Conta bloqueada → falha

### Segurança

* Não revelar qual campo está errado

---

## 4. Transferência

### Regras obrigatórias

* Conta de origem deve existir
* Conta de destino deve existir
* Valor deve ser maior que zero
* Saldo da origem deve ser suficiente
* Não permitir transferência para si mesmo

### Regra crítica

> A transferência é atômica: ou tudo acontece ou nada acontece.

---

## 5. Empréstimo

### Regras

* Existe limite máximo por conta
* Juros fixos definidos pelo sistema
* Não permitir múltiplos empréstimos ativos
* Dívida deve ser persistida

---

## 6. Persistência

### Regras

* Dados devem sobreviver ao encerramento do programa
* Arquivos devem ser criados se não existirem
* Nunca salvar dados parcialmente

---

## 7. Segurança Geral

* Nenhuma regra crítica no front-end
* Nenhum acesso direto aos arquivos fora do back-end
* Tratamento de erros obrigatório

---

## Regra Final

> O sistema deve sempre priorizar consistência dos dados sobre conveniência.
