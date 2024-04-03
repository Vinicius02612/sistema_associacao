# sistema_associacao
Projeto de desenvolvimento do sistema da Associação Quilombola Brejão dos Aipins


# Projeto Web - Sistema de reserva de passagens areas.

## Para colaboradores
### Após fazer o clone do projeto em sua máquina, realize os seguinte passos:
1.Crie uma branch de desenvolvimento contendo sua versão:

> git checkout -b nome_da_sua_branch

2.Faça o **commit** da sua nova branch:

> git commit -m "comentário da sua branch"

3.Suba a sua nova branch para o repositório do projeto:

> git push --set-upstream origin nome_da_sua_branch

### É IMPORTANTE SEMPRE MANTER AS DUAS BRANCHS (MAIN E SUA_BRANCH) ATUALIZADAS

Sempres que houver uma atualização na main, rode o comando:

> git pull origin main

Ou caso queira atualizar a sua branch direto com a do outro coleguinha:

> git pull origin nome_da_branch_do_coleguinha

Caso queira verificar a branch do coleguinha sem afetar a sua branch:

> git checkout nome_da_branch_do_coleguinha

## Rode na sua máquina
1. Instale o python3.11
2. Crie um ambiente virtual com o comando `python3 -m venv venv`
3. Ative o ambiente virtual com o comando `source venv/bin/activate`
4. Instale as dependências com o comando `pip install -r requirements.txt`
5. Execute o projeto com o comando `python manage.py runserver`
6. Acesse o projeto em http://localhost:8000
7. Para criar um superuser e ter acesso as funcionalidades de admin, execute o comando `python manage.py createsuperuser` e siga as instruções.
