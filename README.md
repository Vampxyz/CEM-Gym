# 🏋️‍♂️ Academia Corpo em Movimento (CEM Gym)

Sistema web desenvolvido em **Django** e **SQLite** para a **Academia Corpo em Movimento**, permitindo à proprietária gerenciar modalidades e turmas pelo painel administrativo e disponibilizando aos alunos uma página inicial com as modalidades ativas e a grade de horários atualizada diretamente do banco de dados.

---

## 📋 Etapa 2 — Questionário de Aprofundamento

As respostas sobre o fluxo da aplicação, decisões de banco de dados (ORM), regras de negócio e conceitos aprendidos na segunda etapa estão disponíveis no arquivo abaixo:

👉 **[Clique aqui para acessar as respostas da etapa de pós entrega (`answers.md`)](https://github.com/Vampxyz/CEM-Gym/blob/main/ANSWERS.md)**

---

## 👨‍💻 Equipe de Desenvolvimento

* **Ryhan Nalbert Oliveira de Araújo**

---

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo no terminal para executar o projeto do zero em um ambiente virtual próprio:

**1. Clonar o repositório e acessar a pasta do projeto:**
```
git clone https://github.com/Vampxyz/CEM-Gym
cd CEM-Gym
```

**2. Criar e ativar o ambiente virtual (`venv`):**

```
python -m venv .venv

# No Linux/macOS:
source .venv/bin/activate

# No Windows:
.venv\Scripts\activate
```

**3. Instalar o Django:**

```
pip install django
```

**4. Gerar e aplicar as migrações no banco de dados SQLite:**

```
python manage.py makemigrations
python manage.py migrate
```

**5. Criar um superusuário para acessar o painel administrativo:**

```
python manage.py createsuperuser
```

**6. Iniciar o servidor de desenvolvimento:**

```
python manage.py runserver
```

### 🔗 Endereços da Aplicação
* **Página Inicial:** http://127.0.0.1:8000/
* **Grade de Turmas e Horários:** http://127.0.0.1:8000/turmas/
* **Painel Administrativo:** http://127.0.0.1:8000/admin/

---

## 🤖 Diário de IA do Dia

Registro do uso de Inteligência Artificial (Gemini) como ferramenta de apoio e estudo durante o desenvolvimento do projeto:

* **Arquitetura e Fluxo do Django:** Consulta sobre como estruturar o projeto e o app (`gym`), compreendendo a conexão entre `models.py`, `admin.py`, `views.py`, `urls.py` e a pasta `templates/`.
  
* **Modelagem de Dados (ORM) e Regras de Negócio:** Estudo prático de como implementar as regras de negócio no ORM do Django, incluindo o bloqueio de exclusão de modalidades com turmas vinculadas via `on_delete=models.PROTECT` (**RN03**), a criação automática do método `get_dayOfWeek_display()` em campos com `choices` (**RN04**) e a customização do painel administrativo com `list_display`, `list_filter` e `search_fields` (**RF03, RF04 e RF05**).

* **Estilização Front-End (HTML/CSS):** A partir da estrutura de tabelas e templates criada pela equipe e de referências visuais selecionadas, utilizamos a IA para agilizar a escrita do CSS (`global.css`, `index.css` e `classes.css`), ajustando a responsividade dos cards de modalidades.
