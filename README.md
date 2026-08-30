# Digimon Evolution Line

Aplicação web desenvolvida em Django para registrar e consultar linhas evolutivas de Digimon, permitindo ao usuário criar, editar e visualizar a linha evolutiva de seus personagens favoritos.

## Objetivo

O projeto tem como objetivo oferecer uma plataforma simples e funcional para organizar linhas evolutivas de Digimon, integrando dados de uma API externa para facilitar a consulta e a montagem da linha evolutiva.

A aplicação permite que o usuário:

- cadastre uma linha evolutiva;
- associe cada fase evolutiva a um Digimon;
- visualize a evolução em uma estrutura clara;
- consulte dados atualizados diretamente da Digi-API.

## Funcionalidades

- Cadastro de usuários;
- Autenticação e login com Django;
- Criação de linhas evolutivas;
- Edição e exclusão de linhas pelo usuário autenticado;
- Armazenamento de IDs de Digimon por fase evolutiva;
- Consulta de Digimons em uma API externa;
- Listagem de linhas evolutivas com os nomes dos Digimons;
- Página inicial com listagem paginada dos Digimons disponíveis;
- Tratamento de erros quando a API externa estiver indisponível.

## Tecnologias

- Python 3
- Django 5
- MySQL
- Requests
- HTML/CSS
- Bootstrap (caso usado nos templates, conforme o projeto)
- Django Auth

## Estrutura do projeto

```text
.
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── digimon/
│   ├── migrations/
│   ├── services/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd wsBackendFabricaDeSoftware26.2
```

2. Crie um ambiente virtual:

```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

- Linux/macOS:

```bash
source .venv/bin/activate
```

- Windows:

```bash
.venv\Scripts\activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Verifique se o MySQL está instalado e em execução em sua máquina.

## Configuração do banco

O projeto utiliza MySQL como banco de dados. A configuração atual está em `config/settings.py` e usa a engine `django.db.backends.mysql`.

Exemplo de configuração:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'digimon_site',
        'USER': 'root',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Crie o banco no MySQL:

```sql
CREATE DATABASE digimon_site CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Se necessário, ajuste usuário, senha e nome do banco conforme o ambiente local.

## Variáveis de ambiente

Para manter as configurações sensíveis fora do código, o ideal é usar variáveis de ambiente. A estrutura recomendada é a seguinte:

```env
SECRET_KEY=sua_chave_secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=digimon_site
DB_USER=root
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
```

A configuração do Django pode então ser feita com `os.getenv()` ou `os.environ`, por exemplo:

```python
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_key')
DEBUG = os.getenv('DEBUG', 'True') == 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
    }
}
```

> Observação: o projeto atual salva alguns valores diretamente em `config/settings.py`; em produção, prefira externalizar esses dados para variáveis de ambiente.

## Execução

1. Aplique as migrações do banco:

```bash
python manage.py migrate
```

2. Crie um superusuário para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

3. Inicie o servidor local:

```bash
python manage.py runserver
```

4. Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## API externa utilizada

A aplicação consome a Digi-API, uma API pública de Digimon, para buscar dados como:

- lista de Digimons;
- dados detalhados de cada Digimon;
- imagens e informações de cada espécie.

Base URL usada:

```text
https://digi-api.com/api/v1
```

No projeto, a integração fica em `digimon/services/digimon_api.py` e é utilizada para:

- listar Digimons paginados;
- consultar um Digimon específico por ID;
- apresentar os nomes dos Digimons nas linhas evolutivas.

Exemplo de chamada:

```python
response = requests.get('https://digi-api.com/api/v1/digimon', params={'page': 0, 'pageSize': 15})
```

## Fluxo principal da aplicação

- Usuário cria uma conta e faz login;
- Define uma linha evolutiva com nome e fases correspondentes;
- Cada fase recebe o ID de um Digimon;
- A aplicação busca os dados desses Digimons na Digi-API;
- A linha evolutiva é exibida ao usuário com os nomes de cada estágio.

## Observações finais

Este projeto é um exemplo prático de uso do Django para gestão de dados personalizados com integração em API externa. Ele pode ser expandido com:

- dashboard administrativo mais completo;
- filtros e busca por nome de Digimon;
- melhorias na interface do usuário;
- uso de variáveis de ambiente em produção;
- deploy em ambiente web real.

---

Se quiser, posso também transformar este README em uma versão mais profissional, com badges, licença, screenshots e instruções específicas para Linux/Windows.