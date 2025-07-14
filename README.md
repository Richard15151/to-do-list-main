# To-Do List Completa 📝
Um projeto de To-Do List robusta e completa, desenvolvida com uma arquitetura full-stack. O frontend é construído com **HTML** e **CSS**, proporcionando uma interface de usuário intuitiva. O backend é em **Flask** um framework web **Python**, e a persistência dos dados é garantida por um banco de dados **MySQL**.

---

## 🚀 Tecnologias Utilizadas

- Frontend:
HTML5: Estrutura da interface do usuário da lista de tarefas.
CSS3: Estilização responsiva e atraente para uma boa experiência de uso.

- Backend:
Flask: Microframework Python para roteamento e renderização de templates.
Python: Linguagem de programação para a lógica de negócio e manipulação do banco de dados.

- Banco de Dados:
MySQL: Armazenamento e gerenciamento das tarefas.

---

## ✨ Recursos Principais
- Adicionar Tarefas: Funcionalidade para criar novas tarefas com facilidade.
  
- Visualizar Tarefas: Exibição de todas as tarefas cadastradas em uma lista organizada.
  
- Marcar como Concluída: Opção para marcar tarefas como finalizadas, com feedback visual.
  
- Excluir Tarefas: Capacidade de remover tarefas que não são mais necessárias.
  
- Persistência de Dados: Todas as tarefas são salvas no banco de dados e persistem mesmo após o fechamento da aplicação.
  
- Design Responsivo: Interface que se adapta a diferentes tamanhos de tela (desktops, tablets, smartphones).

---

## 💡 Propósito do Projeto
Este projeto foi desenvolvido com o objetivo de praticar e aprimorar habilidades em:

- Desenvolvimento Full-Stack: Integração de frontend (HTML/CSS com Flask) e backend (Python com Flask).

- Manipulação de Banco de Dados: Criação e interação com um banco de dados SQL para persistência de dados.

- Criação de APIs/Rotas com Flask: Gerenciamento de requisições HTTP para operações CRUD (Criar, Ler, Atualizar, Deletar).

- Design e Usabilidade: Desenvolvimento de uma interface de usuário limpa e funcional para uma aplicação prática.

---

## 💻 Como Executar o Projeto
Para configurar e rodar o projeto em sua máquina local, siga estes passos:

1. Clone o repositório:

```Bash
  git clone https://github.com/seu-usuario/nome-do-repositorio.git
````

2. Navegue até a pasta do projeto:

```Bash

cd nome-do-repositorio
````

3. Crie e ative um ambiente virtual (recomendado):

```Bash

python -m venv venv
````
### No Windows:
.\venv\Scripts\activate
### No macOS/Linux:
source venv/bin/activate

4. Instale as dependências:

```Bash

pip install -r requirements.txt
```
(Você precisará instalar Flask e outras bibliotecas manualmente: pip install Flask pymysql)

5. Inicialize o banco de dados:

```Bash

python scriptBd.sql
````

6. Execute a aplicação Flask:

```Bash

python app.py
```

7. Acesse a aplicação:
Abra seu navegador e vá para http://127.0.0.1:5000/ (ou o endereço que o terminal indicar).

---

## 🛠️ Estrutura do Projeto
- app.py (ou main.py): Contém a lógica principal da aplicação Flask, rotas e interação com o banco de dados.

- templates/: Pasta com os arquivos HTML (index.html, etc.).

- static/: Pasta para arquivos estáticos como CSS (style.css).

- scriptBd.sql: Script para criar a estrutura inicial do banco de dados.

---

## 👨‍💻 Criador
Projeto desenvolvido por Richard de Oliveira Ribeiro
- Github: https://github.com/Richard15151
- Linkedin: https://www.linkedin.com/in/richard-oliveira-b30a10315/
