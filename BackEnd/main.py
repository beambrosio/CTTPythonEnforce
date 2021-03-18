
'''
Projeto feito para a trilha de Python da Campinas Tech Talents 2021.
Projeto de processo seletivo para a empresa Enforce. Um sistema de Imobiliaria com CRUD.
Banco de dados PostgreSQL, backend em Python/Flask interligando com o banco de dados através do SQLAlchemy, e frontend em Angular. 
Projeto ainda em desenvolvimento e polimento.
'''

''' atualizar com pip install Werkzeug==0.16.1'''

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restplus import Api, Resource,fields, model
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import PrimaryKeyConstraint
from datetime import date



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://[NOME_USER_DO_BANCO_DE_DADOS]:[SUA SENHA]@localhost/Imobiliaria' 
CORS(app)

ma = Marshmallow(app)
#api que conecta com o swagger para documentação
api = Api(version="0.1.2",
            title="Imobiliaria Swagger",
            description="Destinado a documentação do sistema de venda de imoveis em uma Imobiliária. | Desenvolvido por: Beatriz Ambrosio")
api.init_app(app)
db = SQLAlchemy(app)


# Declaração das tabelas do banco de dados que farão CRUD
class Gastos(db.Model):
    __tablename__ = 'gastos'
    imoveis = db.relationship('Imoveis', backref='gastos', lazy=True)
    id_gastos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    luz = db.Column(db.String)
    agua = db.Column(db.String)
    condominio = db.Column(db.String)

class Cliente(db.Model):
    __tablename__ = 'clientes'
    compras = db.relationship('Compras', backref='clientes', lazy=True)

    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String)
    data_nasc_cliente = db.Column(db.Date)
    cpf_cliente = db.Column(db.String)
    rg_cliente = db.Column(db.Integer)
    est_civil_cliente = db.Column(db.String)
    tel_cliente = db.Column(db.String)
    formacao_cliente = db.Column(db.String)
    rua = db.Column(db.String)
    num = db.Column(db.String)
    andar = db.Column(db.String)
    bloco = db.Column(db.String)
    cidade = db.Column(db.String)
    cep = db.Column(db.String)
    estado = db.Column(db.String)

class Proprietario(db.Model):
    __tablename__ = 'proprietarios'
    imoveis = db.relationship('Imoveis', backref='proprietarios', lazy=True)

    id_prop = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_prop = db.Column(db.String)
    data_nasc_prop = db.Column(db.Date)
    cpf_prop = db.Column(db.String)
    rg_prop = db.Column(db.Integer)
    est_civil_prop = db.Column(db.String)
    tel_prop = db.Column(db.String)
    formacao = db.Column(db.String)
    temp_imovel = db.Column(db.String)
   
class Imoveis(db.Model):
    __tablename__='imoveis'
    compras = db.relationship('Compras', backref='imoveis', lazy=True)
    
    id_imovel = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rua = db.Column(db.String)
    num = db.Column(db.String)
    andar = db.Column(db.String)
    bloco = db.Column(db.String)
    cidade = db.Column(db.String)
    cep = db.Column(db.String)
    estado = db.Column(db.String)
    preco_imo = db.Column(db.String)
    obs = db.Column(db.String)
    id_prop = db.Column(db.Integer, db.ForeignKey('proprietarios.id_prop'))
    id_gastos = db.Column(db.Integer, db.ForeignKey('gastos.id_gastos'), nullable=True)

class Compras(db.Model):
    __tablename__= 'compras'


    id_compra  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_compra = db.Column(db.String)
    banco_finan = db.Column(db.String)
    preco = db.Column(db.String)

    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_imovel = db.Column(db.Integer, db.ForeignKey('imoveis.id_imovel'))

#Os esquemas, utilizando a biblioteca do Marshmellow
class CompraSchema(ma.Schema):
    class Meta: 
        fields = ('id_compra','tipo_compra','banco_finan',
            'preco','id_cliente','id_imovel')

class ImovelSchema(ma.Schema):
    class Meta: 
        fields = ('id_imovel','rua', 'num', 'andar', 'bloco', 'cidade', 'cep', 
            'estado', 'preco_imo', 'obs', 'id_prop', 'id_gastos', 'proprietario.nome_prop')

class ProprietarioSchema(ma.Schema):
    class Meta:
        fields = ('id_prop','nome_prop', 'data_nasc_prop', 'cpf_prop',
                'rg_prop', 'est_civil_prop', 'tel_prop', 'formacao', 'temp_imovel')

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id_cliente', 'nome_cliente', 'data_nasc_cliente',
         'cpf_cliente','rg_cliente','est_civil_cliente','tel_cliente','formacao_cliente',
         'rua','num','andar','bloco','cidade','cep','estado')

class GastoSchema(ma.Schema):
    class Meta:
        fields = ('id_gastos','luz','agua', 'condominio')


# definição dos model para melhor documentação no Swagger
compra_modo= api.model('Compra', {'id_compra':fields.Integer(required= True,
                                        description='Identificador da Compra',
                                        help="Campo obrigatório"),
                                'tipo_compra':fields.String(required= True,
                                        description='Financiado ou outra forma de pagamento',
                                        help="Campo obrigatório"),
                                'banco_finan':fields.String(required= True,
                                        description='Se financiado, o banco que foi',
                                        help="Campo obrigatório"),
                                'preco':fields.String(required= True,
                                        description='Preço da compra do imóvel',
                                        help="Campo obrigatório"),
                                'id_cliente':fields.Integer(
                                        description='Identificador do Cliente que vai comprar',
                                        help="Campo obrigatório"),
                                'id_imovel':fields.Integer(required= True,
                                        description='Identificador do Imóvel que será comprado',
                                        help="Campo obrigatório")
})


imovel_modo = api.model('Imovel',{'id_imovel':fields.Integer(required= True,
                                        description='Identificador do Imóvel',
                                        help="Campo obrigatório"),
                                'rua':fields.String(required= True,
                                        description='Rua que se encontra o Imóvel',
                                        help="Campo obrigatório"), 
                                'num':fields.String(required= True,
                                        description='Número do Imóvel',
                                        help="Campo obrigatório"), 
                                'andar':fields.String(
                                        description='Andar, se tiver'), 
                                'bloco':fields.String(
                                        description='Bloco, se tiver'), 
                                'cidade':fields.String(required= True,
                                        description='Cidade do Imóvel',
                                        help="Campo obrigatório"), 
                                'cep':fields.String(required= True,
                                        description='CEP do Imóvel',
                                        help="Campo obrigatório"), 
                                'estado':fields.String(required= True,
                                        description='Estado do imóvel',
                                        help="Campo obrigatório"), 
                                'preco_imo':fields.String(required= True,
                                        description='Preço do Imóvel',
                                        help="Campo obrigatório"), 
                                'obs':fields.String(
                                        description='Observações, caso tenha, do Imóvel'), #nao pode ser obrigatório 
                                'id_prop':fields.Integer(required= True,
                                        description='Identificador do Proprietário do Imóvel',
                                        help="Campo obrigatório"),
                                'id_gastos':fields.Integer(
                                        description='Identificador dos Gastos acumulados do imóvel, caso tenha')
})

proprietario_modo = api.model('Proprietario',{'id_prop':fields.Integer(required= True,
                                                description='Identificador do Proprietário',
                                                help="Campo obrigatório"),
                                            'nome_prop':fields.String(required= True,
                                                description='Nome do Proprietário',
                                                help="Campo obrigatório"),
                                            'data_nasc_prop':fields.Date(required= True,
                                                description='Data de Nascimento do Proprietário',
                                                help="Campo obrigatório"), 
                                            'cpf_prop':fields.String(required= True,
                                                description='CPF do Proprietário',
                                                help="Campo obrigatório"),
                                            'rg_prop':fields.Integer(required= True,
                                                description='RG do Proprietário',
                                                help="Campo obrigatório"), 
                                            'est_civil_prop':fields.String(required= True,
                                                description='Estado Civil do Proprietário',
                                                help="Campo obrigatório"), 
                                            'tel_prop':fields.String(required= True,
                                                description='Telefone/Celular do Proprietário',
                                                help="Campo obrigatório"), 
                                            'formacao':fields.String(required= True,
                                                description='Formação do Proprietario',
                                                help="Campo obrigatório"), #não pode ser obrigatorio
                                            'temp_imovel':fields.String(required= True,
                                                description='Tempo que possui o Imóvel',
                                                help="Campo obrigatório")
})

cliente_modo = api.model('Cliente',{'id_cliente':fields.Integer(required= True,
                                        description='Identificador do Cliente',
                                        help="Campo obrigatório"),
                                    'nome_cliente':fields.String(required= True,
                                        description='Nome do Cliente',
                                        help="Campo obrigatório"),
                                    'data_nasc_cliente':fields.Date(required= True,
                                        description='Data de Nascimento do Cliente',
                                        help="Campo obrigatório"),
                                    'cpf_cliente':fields.String(required= True,
                                        description='CPF do Cliente',
                                        help="Campo obrigatório"),
                                    'rg_cliente':fields.Integer(required= True,
                                        description='RG do Cliente',
                                        help="Campo obrigatório"),
                                    'est_civil_cliente':fields.String(required= True,
                                        description='Estado Civil do Cliente',
                                        help="Campo obrigatório"),
                                    'tel_cliente':fields.String(required= True,
                                        description='Telefone do Cliente',
                                        help="Campo obrigatório"),
                                    'formacao_cliente':fields.String(required= True,
                                        description='Formação do Cliente',
                                        help="Campo obrigatório"), #não pode ser obrigatorio
                                    'rua':fields.String(required= True,
                                        description='Rua que mora atualmente',
                                        help="Campo obrigatório"),
                                    'num':fields.String(required= True,
                                        description='Número da casa',
                                        help="Campo obrigatório"), #colocar opção de casa ou apartamento
                                    'andar':fields.String(
                                        description='Andar, se tiver'),
                                    'bloco':fields.String(
                                        description='Bloco, se tiver'),
                                    'cidade':fields.String(required= True,
                                        description='Cidade que a casa se encontra',
                                        help="Campo obrigatório"),
                                    'cep':fields.String(required= True,
                                        description='CEP da Cidade',
                                        help="Campo obrigatório"),
                                    'estado':fields.String(required= True,
                                        description='Estado da Cidade',
                                        help="Campo obrigatório")
})

gastos_modo = api.model('Gastos', {'id_gastos': fields.Integer(required= True,
                                        description='Identificador dos Gastos',
                                        help="Campo obrigatório"),
                                    'luz': fields.String(
                                        description='Conta de Luz'),
                                    'agua': fields.String(
                                        description='Conta de Água'),
                                    'condominio': fields.String(
                                        description='Conta do Condomínio')
})


#Definindo os esquemas para leitura de uma entrada da tabela e leitura da tabela toda, cada tabela com teu esquema especifico
compra_schema = CompraSchema()
compras_schema = CompraSchema(many=True)

imovel_schema= ImovelSchema()
imoveis_schema = ImovelSchema(many=True)

proprietario_schema= ProprietarioSchema()
proprietarios_schema=ProprietarioSchema(many=True)

cliente_schema= ClienteSchema()
clientes_schema = ClienteSchema(many=True)

gasto_schema = GastoSchema()
gastos_schema = GastoSchema(many=True)


# ---  Compra  ---

#definição da rota através do namespace para a compra definido como buy
buy = api.namespace('Compra', description='CRUD Compra')

#classe responsavel por retornar todos os dados da tabela através de um JSON
@buy.route('/getcompra') #rota do get /Compra/getcompra
class getdatacompra(Resource):
    def get(self):
        return jsonify(compras_schema.dump(Compras.query.all()))

#classe responsavel por retornar o dado de uma determinada entrada na tabela, pesquisa de compra
@buy.route('/getid/<int:id_compra>') #rota do get /Compra/getid/id
class getdataidcompra(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Invalido', 500: 'Error'}, 
			 params={ 'id_compra': 'Entre com o ID que deseja PESQUISAR'})
    def get(self, id_compra):
        try:
            compra = Compras.query.get(id_compra) #pegando o id da compra
            return jsonify(compra_schema.dump(compra))
        except KeyError as e:
            buy.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            buy.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por entrar com uma compra nova, input de dado
@buy.route('/postcompra') #rota /Compra/postcompra
class postdatacompra(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' })
    @api.expect(compra_modo) #utilizando o modelo definido anteriormente no codigo
    def post(self): #metodo post
        try:
            compra = Compras( #pega os dados inseridos pelo usuario
                                tipo_compra=request.json['tipo_compra'],
                                banco_finan=request.json['banco_finan'],
                                preco=request.json['preco'], 
                                id_cliente=request.json['id_cliente'],
                                id_imovel=request.json['id_imovel']
                                )
            db.session.add(compra) #adiciona no banco
            db.session.commit() #confirma que os dado foram adicionados no banco
            return {'Status':'Compra adicionada ao sistema'}
        except KeyError as e:
            buy.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            buy.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por alterar um dado de compra
@buy.route('/put/<int:id_compra>') #rota /Compra/put/id
class putdatacompra(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_compra': 'Entre com o ID que deseja EDITAR as informações' })
    @api.expect(compra_modo) #utilizando o modelo declarado
    def put(self, id_compra): #precisa do id para fazer atualização, pega os dados ja utilizados e requisita novos dados ao usuario
        try: 
            compra = Compras.query.get(id_compra)
            compra.tipo_compra = request.json['tipo_compra']
            compra.banco_finan = request.json['banco_finan']
            compra.preco = request.json['preco']
            compra.id_cliente = request.json['id_cliente']
            compra.id_imovel = request.json['id_imovel']
            db.session.commit() #confirma atualização no banco
            return {'Status':'Compra foi editada com sucesso'}
        except KeyError as e:
            buy.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            buy.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por deletar uma determinada entrada da tabela
@buy.route('/delete/<int:id_compra>') #rota /Compra/id
class deletedataicompra(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_compra': 'Entre com o ID que deseja DELETAR' })
    def delete(self,id_compra): #pede o id para poder deletar
        try:
            compra = Compras.query.get(id_compra) #carrega os dados na variavel compra
            db.session.delete(compra) #deleta
            db.session.commit() #confirma que foi deletado
            return {'Status':'Compra deletada com sucesso'}
        except KeyError as e:
            buy.abort(500, e.__doc__, status = "Nao conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            buy.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

# --- Imoveis --- 

#namespace que vai ser utilizado na rota
imov = api.namespace('Imoveis', description='CRUD Imóveis')

#classe que retorna todos os dados da tabela Imovel em um JSON
@imov.route('/getimov') #rota Imoveis/getimov/
class getdataimov(Resource):
    def get(self):
        return jsonify(imoveis_schema.dump(Imoveis.query.all()))

#classe que pesquisa um determinado id na tabeça
@imov.route('/getid/<int:id_imovel>') #rota /Imoveis/getid/id
class getdataidimov(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_imovel': 'Entre com o ID que deseja PESQUISAR' })
    def get(self, id_imovel): #id como parametro para pesquisa
        try:
            imov = Imoveis.query.get(id_imovel) #pesquisa pelo id
            return jsonify(imovel_schema.dump(imov)) #retorna um JSON
        except KeyError as e:
            imov.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            imov.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por inserir um novo imovel na tabela
@imov.route('/postimov') #rota /Imoveis/postimov
class postdataimov(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' })
    @api.expect(imovel_modo) #seguindo o modelo declarado anteriormente
    def post(self):
        try:
            imovel = Imoveis(rua=request.json['rua'], #pega as info digitadas pelo usuario
                                num=request.json['num'],
                                andar=request.json['andar'],
                                bloco=request.json['bloco'], 
                                cidade=request.json['cidade'],
                                cep=request.json['cep'],
                                estado=request.json['estado'],
                                preco_imo=request.json['preco_imo'],
                                obs=request.json['obs'],
                                id_prop=request.json['id_prop'],
                                id_gastos=request.json['id_gastos']
                                )
            db.session.add(imovel) #adiciona no banco
            db.session.commit() #confirma que foi adicionado no banco
            return {'Status':'Imovel adicionado com sucesso'}
        except KeyError as e:
            imov.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            imov.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por atualizar um dado do Imovel
@imov.route('/put/<int:id_imovel>') #rota /Imoveis/put/id
class putdataimov(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_imovel': 'Entre com o ID que deseja atualizar' })
    @api.expect(imovel_modo) #utilizando o modo ja declarado
    def put(self, id_imovel):#id como parametro pra saber qual sera editado
        try:
            imovel = Imoveis.query.get(id_imovel) #pega os dados digitados pelo usuário
            imovel.rua = request.json['rua']
            imovel.num = request.json['num']
            imovel.andar = request.json['andar']
            imovel.bloco = request.json['bloco']
            imovel.cidade = request.json['cidade']
            imovel.cep = request.json['cep']
            imovel.estado = request.json['estado']
            imovel.preco_imo = request.json['preco_imo']
            imovel.obs = request.json['obs']
            imovel.id_prop = request.json['id_prop']
            imovel.id_gastos = request.json['id_gastos']
            db.session.commit() #conforma no banco
            return {'Status':'Imovel atualizado'} 
        except KeyError as e:
            imov.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            imov.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por deletar um determinado dado na tabela
@imov.route('/delete/<int:id_imovel>') #rota Imoveis/delete/id
class deletedataimov(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_imovel': 'Entre com o ID do cadastro que deseja DELETAR' })
    def delete(self, id_imovel): #id como parametro pra saber qual deletar
        try:
            imovel = Imoveis.query.get(id_imovel)
            db.session.delete(imovel) #deleta o imovel
            db.session.commit() #confirma
            return {'Status':'Imovel deletado com sucesso'}
        except KeyError as e:
            imov.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            imov.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

# --- Proprietario --- 

#namespace para definição da rota /Proprietarios/
prop = api.namespace('Proprietarios', description='CRUD Proprietarios')

#classe responsavel por pegar todos os dados da tabela
@prop.route('/getprop') #rota /Proprietarios/getprop/
class getdataprop(Resource):
    def get(self):
        return jsonify(proprietarios_schema.dump(Proprietario.query.all()))

#classe responsavel por pesquisar um determinado dado da tabela
@prop.route('/getid/<int:id_prop>')  #rota /Proprietarios/getid/id
class getdataidprop(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Invalido', 500: 'Error' }, 
			 params={ 'id_prop': 'Entre com o ID que deseja PESQUISAR' })
    def get(self, id_prop): #passa id como parametro para a pesquisa
        try:
            prop = Proprietario.query.get(id_prop) 
            return jsonify(proprietario_schema.dump(prop)) #retorna um JSON com os dados
        except KeyError as e:
            prop.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            prop.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsável por atualizar um inserir uma nova entrada na tabela
@prop.route('/postprop') #rota /Proprietarios/postprop
class postdataprop(Resource): 
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' })
    @api.expect(proprietario_modo)
    def post(self):
        try:
            proprietario = Proprietario(nome_prop=request.json['nome_prop'], #atribui aos dados digitados do proprietario
                                data_nasc_prop=request.json['data_nasc_prop'],
                                cpf_prop=request.json['cpf_prop'],
                                rg_prop=request.json['rg_prop'], 
                                est_civil_prop=request.json['est_civil_prop'],
                                tel_prop=request.json['tel_prop'],
                                formacao=request.json['formacao'],
                                temp_imovel=request.json['temp_imovel'],
                                )
            db.session.add(proprietario)
            db.session.commit() #confirma a entrada do dado na tabela
            return {'Status':'Proprietário adicionado com sucesso'}
        except KeyError as e:
            prop.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            prop.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por atualizar um dado na tabela
@prop.route('/put/<int:id_prop>') #rota /Proprietarios/put/id
class putdataprop(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento inválido', 500: 'Error' }, 
			 params={ 'id_prop': 'Entre com o ID que deseja EDITAR as informações' })
    @api.expect(proprietario_modo)
    def put(self, id_prop): #id como parametro pra saber qual dado atualizar
        try:
            proprietario = Proprietario.query.get(id_prop) #pega os dados digitados pelo usuario
            proprietario.nome_prop = request.json['nome_prop']
            proprietario.data_nasc_prop = request.json['data_nasc_prop']
            proprietario.cpf_prop = request.json['cpf_prop']
            proprietario.rg_prop = request.json['rg_prop']
            proprietario.est_civil_prop = request.json['est_civil_prop']
            proprietario.tel_prop = request.json['tel_prop']
            proprietario.formacao = request.json['formacao']
            proprietario.temp_imovel = request.json['temp_imovel']
            db.session.commit() #confirma a atualização
            return {'Status':'Proprietário atualizado'}
        except KeyError as e:
            prop.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            prop.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por deletar um determinado dado na tabela
@prop.route('/delete/<int:id_prop>') #rota /Proprietarios/delete/id
class deletedataprop(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_prop': 'Entre com o ID que deseja DELETAR' })
    def delete(self, id_prop): #id como parametro pra saber qual deletar
        try:
            proprietario = Proprietario.query.get(id_prop)
            db.session.delete(proprietario)
            db.session.commit() #confirma o delete
            return {'Status':'Proprietário deletado com sucesso'}
        except KeyError as e:
            prop.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            prop.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")


# --- Cliente --- 

#namespace do cliente para definição das rotas
cli = api.namespace('Cliente', description='CRUD Clientes')

#classe responsavel por mostrar todos os dados da tabela cliente num JSON
@cli.route('/getcli') #rota /Cliente/getcli
class getdatacli(Resource):
    def get(self):
        return jsonify(clientes_schema.dump(Cliente.query.all()))

#classe responsavel por pesquisar determinado cliente na tabela por id
@cli.route('/getid/<int:id_cliente>') #rota /Cliente/getid/id
class getdataidcli(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_cliente': 'Entre com o ID que deseja PESQUISAR' })
    def get(self, id_cliente): #passa id como parametro 
        try:
            cliente = Cliente.query.get(id_cliente)
            return jsonify(cliente_schema.dump(cliente)) #retorna o cliente pesquisado conforme o id     
        except KeyError as e:
            cli.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            cli.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsável por entrar com novos dados na tabela 
@cli.route('/postcli') #rota /Cliente/postcli
class postdatacli(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' })
    @api.expect(cliente_modo) #no modelo declarado anteriormente 
    def post(self):
        try:
            cliente = Cliente(nome_cliente=request.json['nome_cliente'], #pega os dados digitados pelo cliente
                                data_nasc_cliente=request.json['data_nasc_cliente'],
                                cpf_cliente=request.json['cpf_cliente'],
                                rg_cliente=request.json['rg_cliente'], 
                                est_civil_cliente=request.json['est_civil_cliente'],
                                tel_cliente=request.json['tel_cliente'],
                                formacao_cliente=request.json['formacao_cliente'],
                                rua=request.json['rua'],
                                num=request.json['num'],
                                andar=request.json['andar'],
                                bloco=request.json['bloco'],
                                cidade=request.json['cidade'],
                                cep=request.json['cep'],
                                estado=request.json['estado'])
            db.session.add(cliente)
            db.session.commit() #confirma entrada do novo dado
            return {'Status':'Cliente adicionado com sucesso'}
        except KeyError as e:
            cli.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            cli.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por atualizar o dado do cliente por id
@cli.route('/put/<int:id_cliente>') #rota /Cliente/put/id
class putdatacli(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_cliente': 'Entre com o ID que deseja ATUALIZAR' })
    @api.expect(cliente_modo) #no modelo declarado anteriormente
    def put(self, id_cliente): #passa id como parametro pra saber qual atualizar 
        try:
            cliente = Cliente.query.get(id_cliente) 
            cliente.nome_cliente = request.json['nome_cliente'] #input do usuario
            cliente.data_nasc_cliente = request.json['data_nasc_cliente']
            cliente.cpf_cliente = request.json['cpf_cliente']
            cliente.rg_cliente = request.json['rg_cliente']
            cliente.est_civil_cliente = request.json['est_civil_cliente']
            cliente.tel_cliente = request.json['tel_cliente']
            cliente.formacao_cliente = request.json['formacao_cliente']
            cliente.rua = request.json['rua']
            cliente.num = request.json['num']
            cliente.andar = request.json['andar']
            cliente.cidade = request.json['cidade']
            cliente.cep = request.json['cep']
            cliente.estado = request.json['estado']
            db.session.commit() #confirma atualização do dado
            return {'Status':'Cliente atualizado com sucesso'}
        except KeyError as e:
            cli.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            cli.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por deletar um determinado cliente da tabela
@cli.route('/delete/<int:id_cliente>') #rota /Cliente/delete/id
class deletedatacli(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_cliente': 'Entre com o ID que deseja DELETAR' })
    def delete(self, id_cliente): #passa id como parametro pra saber qual deletar
        try:
            cliente = Cliente.query.get(id_cliente)
            db.session.delete(cliente)
            db.session.commit()
            return {'Status':'Cliente deletado com sucesso'}
        except KeyError as e:
            cli.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            cli.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

# --- Gastos ---              

#namespace pras rotas /Gastos/
spend = api.namespace('Gastos', description='CRUD Gastos')

#classe responsavel por retornar todos os dados da tabela
@spend.route('/get') #rota /Gastos/get
class getdata(Resource):
    def get(self):
        return jsonify(gastos_schema.dump(Gastos.query.all()))


#classe responsavel por pesquisar um determinado dado na tabela por id
@spend.route('/getid/<int:id_gastos>') #rota /Gastos/getid/id
class getdataid(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_gastos': 'Entre com o ID que deseja PESQUISAR' })
    def get(self, id_gastos): #passa id como parametro pra poder pesquisar
        try:
            gastos = Gastos.query.get(id_gastos)
            return jsonify(gasto_schema.dump(gastos))
        except KeyError as e:
            spend.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            spend.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por inserir novos dados na tabela      
@spend.route('/post') #rota /Gastos/post
class postdata(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' })  
    @api.expect(gastos_modo) #seguindo o modelo ja declarado anteriormente
    def post(self):
        try:
            gasto = Gastos(luz=request.json['luz'], #pega os dados digitados pelo usuario
                agua=request.json['agua'],
                condominio=request.json['condominio'])

            db.session.add(gasto)
            db.session.commit()#insere no banco
            return {
                'Status':'Gastos inserido com sucesso'
            }
        except KeyError as e:
            spend.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            spend.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

#classe responsavel por atualizar um dado de um determinado cadastro por id
@spend.route('/put/<int:id_gastos>') #rota /Gastos/put/id
class putdata(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_gastos': 'Entre com o ID que deseja ATUALIZAR' })
    @api.expect(gastos_modo)
    def put(self, id_gastos): #id como parametro pra saber qual atualizar
        try:
            gasto = Gastos.query.get(id_gastos)
            gasto.luz = request.json['luz'] #dados digitados pelo usuario
            gasto.agua = request.json['agua']
            gasto.condominio = request.json['condominio']
            db.session.commit()
            return {'Status':'Gastos Atualizado com sucesso'}
        except KeyError as e:
            spend.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            spend.abort(400, e.__doc__, status = "Nâo conseguiu retornar a informação", statusCode = "400")

#classe responsavel por deletar um dado da tabela por id
@spend.route('/delete/<int:id_gastos>') #rota /Gastos/delete/id
class deletedata(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Argumento Inválido', 500: 'Error' }, 
			 params={ 'id_gastos': 'Entre com o ID que deseja DELETAR' })
    def delete(self,id_gastos):
        try:
            gasto = Gastos.query.get(id_gastos)
            db.session.delete(gasto)
            db.session.commit()
            return {'Status':'Gastos deletado com sucesso'}
        except KeyError as e:
            spend.abort(500, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "500")
        except Exception as e:
            spend.abort(400, e.__doc__, status = "Não conseguiu retornar a informação", statusCode = "400")

if __name__ == '__main__':
    app.debug = True
    app.run()