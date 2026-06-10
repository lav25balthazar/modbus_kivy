#  Supervisório Modbus com KivyMD

Atividade avaliativa da disciplina Informática Industrial, ministrada pelo prof. Dr. Eng. Guilherme Márcio, da Universidade Federal de Juiz de Fora.

---
##  Arquitetura

### 1. Interface (KivyMD)

- Entrada de IP e porta do servidor
- Configuração de endereço Modbus
- Seleção de tipo de dado
- Exibição de leitura
- Botões de ação

### 2. Cliente Modbus

- Comunicação TCP com o servidor Modbus
- Leitura de registradores e coils
- Escrita de valores no dispositivo

---

##  Tecnologias Utilizadas

- Kivy
- KivyMD
- Modbus TCP 

---


## Leitura Recorrente (Clock)

O sistema utiliza:

Clock.schedule_interval(callback, 1.0)

para atualizar automaticamente os valores na tela.

---

##  Executar
### 1. Criar Ambiente Virtual

python -m venv nome

---
### 2. Instalar dependências

pip install -r requirements.txt

---

### 3. Executar o projeto

python main.py

---


