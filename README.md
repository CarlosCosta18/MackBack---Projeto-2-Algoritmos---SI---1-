# MackBack---Projeto-2-Algoritmos---SI---1-
Segundo Projeto da matéria de algoritmos - Faculdade Presbiteriana Mackenzie


Entendido! Aqui está o README ajustado para descrever o que você já implementou no seu projeto:

---

# Projeto Conta Corrente Bancária

## Descrição

Este projeto é uma implementação de uma conta corrente bancária, desenvolvida como parte de um exercício acadêmico para praticar conceitos de decisão, repetição, funções e listas em Python. O programa simula operações básicas de uma conta bancária, incluindo cadastro, depósito, saque, consulta de saldo e consulta de extrato.

## Funcionalidades Implementadas

1. **Cadastro da Conta**
   - Realiza o cadastro inicial dos dados da conta: nome, telefone, email, saldo inicial, limite de crédito e senha.
   - Validações incluídas:
     - Nome, telefone e email não podem estar em branco.
     - Saldo inicial deve ser maior ou igual a R$1000.
     - Limite de crédito deve ser maior ou igual a R$0.
     - Senha deve ter 6 caracteres e ser confirmada corretamente.
   - O número da conta é gerado aleatoriamente com quatro dígitos.
   - Esta ação é executada uma única vez.

2. **Depósito**
   - Permite acrescentar dinheiro na conta, atualizando o saldo e o histórico de operações.
   - Validações realizadas:
     - Número da conta deve ser fornecido corretamente.
     - Valor do depósito deve ser maior que zero.

3. **Saque**
   - Permite retirar dinheiro da conta mediante fornecimento de senha válida.
   - Validações realizadas:
     - Número da conta e senha devem ser fornecidos corretamente.
     - Valor do saque deve ser maior que zero.
     - O saque é permitido se houver saldo suficiente ou limite de crédito disponível.
     - Até 3 tentativas de senha são permitidas antes de bloquear operações de saque, consulta de saldo e extrato.

4. **Consulta de Saldo**
   - Exibe o saldo da conta e o limite de crédito mediante fornecimento de senha válida.
   - Validações realizadas:
     - Número da conta e senha devem ser fornecidos corretamente.

5. **Consulta de Extrato**
   - Exibe o histórico de operações da conta mediante fornecimento de senha válida.
   - Validações realizadas:
     - Número da conta e senha devem ser fornecidos corretamente.
     - Exibe a lista de operações e o saldo em conta. Se o saldo for negativo, uma mensagem de alerta é exibida.

## Proposta

O objetivo deste projeto é simular uma conta corrente bancária com funcionalidades básicas, permitindo ao usuário realizar operações como cadastro, depósito, saque, consulta de saldo e extrato. A implementação inclui diversas validações de entrada para garantir a integridade dos dados e a segurança das operações, proporcionando uma experiência semelhante à de um banco real.

## Desenvolvedores

Este programa foi desenvolvido por:
- [Carlos Eduaro da Costa Oliveira]

---

