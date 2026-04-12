💰 Gerenciador de Gastos Pessoais
Descrição do Problema Real
Muitas pessoas têm dificuldade em visualizar para onde o dinheiro está indo ao final do mês. A falta de um registro centralizado e simples resulta em descontrole financeiro. Este projeto resolve isso oferecendo uma interface direta para o lançamento e acompanhamento de despesas diárias, evitando planilhas complexas ou aplicativos cheios de anúncios.
👥 Público-Alvo
Estudantes e jovens profissionais.
Pessoas que buscam uma ferramenta minimalista de controle financeiro.
Usuários que preferem uma solução auto-hospedada ou local para seus dados.
🚀 Funcionalidades
✅ Cadastro de despesas com nome e valor.
✅ Listagem cronológica de gastos.
✅ Visualização de totais (opcional, dependendo da sua view).
✅ Interface administrativa via Django Admin.
🛠 Tecnologias Utilitárias
Framework: Django 4.2.30
Linguagem: Python 3.14+
Banco de Dados: SQLite (embutido)
Ambiente Virtual: venv
Linting: Flake8 / Black (Recomendados)
📥 Instalação e Execução
Clone o repositório:
bash
git clone https://github.com
cd Gerenciador-de-gastos-


Crie e ative o ambiente virtual:
bash
python -m venv .venv
# No macOS/Linux:
source .venv/bin/activate
# No Windows:
.venv\Scripts\activate


Instale as dependências:
bash
pip install django


Prepare o Banco de Dados:
bash
python manage.py makemigrations gastos
python manage.py migrate


Rode o servidor:
bash
python manage.py runserver


Acesse: http://127.0.0
🧹 Como rodar o Lint
Para garantir que o código esteja seguindo as boas práticas (PEP8), instale o ruff e execute:
bash
pip install ruff
ruff gastos/

📌 Informações do Projeto
Versão Atual: 1.0.0-beta
Coder: Eduardo
Status: Operacional ✅
