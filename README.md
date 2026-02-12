🎫 Assistente de Abertura de Chamados – TI
==========================================

Sistema de abertura de chamados via Discord integrado ao n8n para automação
de classificação automática, geração de protocolo e envio de notificações
por e-mail.

--------------------------------------------------------------------------

## 📌 Visão Geral

O Assistente de Abertura de Chamados é composto por:

- Bot Discord com comando Slash
- Interface de formulário (Modal)
- Comunicação via Webhook
- Processamento automatizado no n8n
- Geração automática de protocolo
- Retorno estruturado ao usuário

A solução foi projetada para operar de forma desacoplada, mantendo a lógica centralizada no n8n.

---

## 🎯 Objetivos

- Centralizar a abertura de chamados internos
- Padronizar o registro de demandas
- Automatizar a geração de protocolo
- Permitir classificação automática de criticidade
- Garantir retorno imediato ao colaborador
- Reduzir solicitações informais via mensagens diretas

---

## 🏗️ Arquitetura

### Componentes

#### 1️⃣ Bot Discord

- Implementado em Python utilizando `discord.py`
- Utiliza Slash Command `/abertura_chamado`
- Exibe Modal para coleta de dados
- Envia requisição via Webhook
- Aguarda resposta estruturada do n8n
- Retorna confirmação via Embed (ephemeral)

#### 2️⃣ Automação (n8n)

- Recebe requisição via Webhook
- Executa validações e lógica de negócio
- Classifica criticidade
- Gera número de protocolo
- Envia e-mail automático 
- Retorna JSON com campo `Protocolo`

---

## 🔄 Fluxo de Funcionamento

1. Colaborador executa `/abertura_chamado`
2. Modal é exibido com os campos obrigatórios
3. Bot envia payload JSON ao Webhook do n8n
4. O fluxo processa a demanda
5. Protocolo é gerado
6. Resposta é enviada ao Bot
7. Bot retorna confirmação ao usuário

---

## ⚙️ Funcionalidades

- Abertura estruturada de chamados
- Captura de identificação do usuário Discord
- Integração via Webhook HTTPS
- Geração automática de protocolo
- Retorno imediato e privado (ephemeral)
- Integração com automações corporativas

---

## 📦 Estrutura do Projeto

```
abertura-chamado/
│
├── main.py
├── .env
├── requirements.txt
└── venv/
```

---

## 🔐 Segurança

- Token do Discord armazenado via variável de ambiente
- Comunicação via HTTPS com o n8n
- Sem armazenamento local de dados sensíveis
- Respostas privadas ao usuário (ephemeral)

---

## 📈 Benefícios Técnicos

- Arquitetura leve
- Baixo acoplamento ao sistema principal
- Governança centralizada das regras no n8n
- Facilidade de expansão para novos fluxos
- Escalabilidade baseada em automação

---

## 🚀 Roadmap

- Dashboard web para acompanhamento de chamados
- Controle de SLA
- Histórico por colaborador
- Relatórios gerenciais

---

## 🧠 Considerações Técnicas

Toda a lógica de negócio permanece centralizada no n8n, permitindo:

- Alterações operacionais sem necessidade de alterar o Bot
- Evolução contínua dos fluxos
- Integrações com múltiplos serviços internos
- Manutenção simplificada

O Bot atua apenas como interface de entrada e retorno estruturado das informações.

