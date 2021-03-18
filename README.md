# CTTPythonEnforce
Projeto feito para a trila de Python da Campinas Tech Talents 2021 e processo seletivo da empresa Enforce. 

### Descrição do que foi pedido no projeto
Pelo facilitador: Jeferson Leal

#### Sistema de venda de Imóveis

Fazer um sistema (MVP 0) para cadastro de venda de Imóveis, tendo os seguintes critérios:

- O sistema deverá cadastrar os Imóveis seguindo os requisitos abaixo:
- Tipo do Imóvel: Casa, Apartamento, Kitnet
- Endereço do Imóvel: Rua, Número, Andar (se tiver), Bloco (se tiver), CEP, Cidade, UF
- Dados do proprietário: Nome, Data de Nascimento, CPF, RG, Estado Civíl,
Quanto tempo possuí o imóvel, Profissão
- Gastos com imóvel durante o período de pré-venda: Valor da conta de luz, valor
da conta de água, condomínio, propaganda para venda *

- O sistema deverá cadastrar a compra do imóvel pelo cliente:
- Valor de compra: Se é financiado ou a vista
- Dados do cliente: Nome, CPF, Data Nascimento, RG, Estado Civíl, Profissão, Endereço onde o
cliente mora (Rua, Número, Andar (se tiver), Bloco (se tiver), CEP, Cidade, UF)

- Em caso de financiamento, Dizer qual é o banco no qual o cliente está financiando,
em quantas parcelas e qual porcentagem de entrada *


- As ferramentas/Linguagens de desenvolvimento
- Banco de dados: PostgreSQL
- Flask / Swagger para geração de APIs
- Angular como Front-End

- A Forma de entrega
- O código deverá estar no Github seguindo os critérios:
- 3 pastas: Banco de Dados, API, Front-End
- Conteúdo para a pasta Banco de Dados deverá ser o Script SQL do Create do Banco de
dados e os Creates das tabelas com os seus relacionamentos e chaves.
-Como no sistema haverão tabelas de domínio (Tabelas que não precisam de rotinas de
CRUD), entregar o create table dessas tabelas junto com o insert dos dados.
- Na pasta de Banco de dados, deverá conter pelo menos o modelo físico do banco
(O diagrama poderá ser feito no [draw.io](http://draw.io/), miro ou outra ferramenta de sua escolha)
- Conteúdo para a pasta de API, deverá conter o projeto Flask API com o requirements.txt
(NÃO SUBIR O AMBIENTE VIRTUAL, SOMENTE A PASTA DO PROJETO)
- Conteúdo para a pasta Front-End, deverá conter todo projeto Angular exceto a pasta
node_modules

NICE TO HAVE
- Para o Angular, não precisa componentizar a aplicação, mas se o fizerem, é bom
- Para o Flask, não precisa criar um conjunto de microserviços (Vários Flasks APIs),
mas se o fizerem, é bom
- Para a modelagem do banco de dados, ter o modelo conceitual e modelo lógico
- Para o cadastro de gastos do imóvel, seria bom ter
- Para o cadastro de financiamento (caso a compra seja financiada), seria bom ter

- PRAZO PARA ENTREGA: 17/03 23:59:59

## Para o projeto funcionar

- No diretório BackEnd, criar uma virtual enviroment
``` 
python -m venv [NOME_DIRETORIO] 
```
``` 
cd [NOME_DIRETORIO]
```
``` 
.\Scripts\Activate
```

E seu virtual enviroment estará funcionando
instalar todos as bibliotecas necessarias através:

```
pip install -r requirements.txt
```
Rodar o arquivo e o Swagger estará funcionando com toda a documentação do projeto

- No diretorio do Frontend
``` 
npm install 
```

```
ng serve --open 
```
E o site estará no ar.
