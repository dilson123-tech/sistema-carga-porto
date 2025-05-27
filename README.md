# Sistema de Cargas do Porto

Sistema de controle e análise de cargas para o porto, desenvolvido em Python.  
Permite cadastrar cargas, gerar estatísticas e gráficos dos destinos das cargas.  

---

## Funcionalidades

- Cadastro de cargas com código, destino, peso e data de cadastro
- Geração de cargas mock para testes (usando Faker)
- Exibição de estatísticas das cargas cadastradas
- Geração de gráfico de destinos das cargas (matplotlib)
- Persistência de dados em arquivo JSON

---

## Como usar

1. Clone este repositório:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd <NOME_DA_PASTA>

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

pip install -r requirements.txt

python main.py

controle_carga/
├── controllers/
│   └── carga_controller.py   # Lógica principal do sistema
├── data/
│   └── cargas.json           # Dados persistidos em JSON
├── models/
│   └── carga_model.py        # Modelos de dados
├── utils/
│   └── helpers.py            # Funções auxiliares
├── main.py                   # Ponto de entrada da aplicação
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto

Dependências
Python 3.8+

Faker

Matplotlib

Dicas
Use a opção 5 do menu para gerar cargas mock rapidamente.

Os dados são salvos em data/cargas.json.

Caso não tenha o arquivo cargas.json, ele será criado automaticamente.

Próximos passos
Implementar testes automatizados

Adicionar interface gráfica

Disponibilizar versão web

Autor
Dilson — estudante focado em Ciência da Computação e IA
Contato: dilsonpereira231@gmail.com

Obrigado por usar o Sistema de Cargas do Porto!

yaml
Copiar
Editar

---








