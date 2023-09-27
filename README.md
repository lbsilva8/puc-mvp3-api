<h1 align="center">Lista de séries/filmes para assistir</h1>

<p align="center">
 <a href="#descricao">Descrição do projeto</a> •
 <a href="#executar">Como executar</a> • 
 <a href="#funcionalidades">Funcionalidades</a> • 
 <a href="#autor">Autor</a>
</p>

---

##  Descrição do projeto:

<p> MVP para a disciplina de Full Stack avançado da pós-graduação em Desenvolvimento Full Stack da PUC-RJ. <br>
Foi desenvolvida uma API de uma whishlist, que será consumida por um front-end onde o usuário, poderá visualizar, adicionar ou excluir dados a sua lista de desejos. </p> 

#### *O Front-end relacionada a essa aplicação está disponível no link:* [https://github.com/lbsilva8/puc_mvp_3_front](https://github.com/lbsilva8/puc_mvp_3_front*)
---

## Como executar:

### Instalação
- Clonar o repositório ou realizar o download do mesmo;
- Criar um ambiente virtual e ativa-lo;
- Instalar todas as bibliotecas python listadas no `requirements.txt`:

```
(env)$ pip install -r requirements.txt
```
- Executar a API:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

- Abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

---

### Executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t puc_mvp_3_api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 puc_mvp_3_api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.


## Funcionalidades

- [x] Método GET, para visualizar todas as séries cadastradas no banco
- [x] Método GET, para Visualizar apenas os animes cadastrados no banco
- [x] Método GET, para busca de uma série atravez do ID
- [x] Método POST, para cadastro de novos dados a base de dados
- [x] Método DELETE, para exclusão de dados atravez do nome da série
- [ ] Método PUT, para edição de dados já cadastrados no banco


### Autor
---

<a>
 <sub><b>Lorena Borges</b></sub></a>


Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Lorena-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lorenadasilvaborges/)](https://www.linkedin.com/in/lorenadasilvaborges/) 
[![Gmail Badge](https://img.shields.io/badge/-sborges.lorena@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:sborges.lorena@gmail.com)](mailto:sborges.lorena@gmail.com)


                                                                                          🚧  Em construção  🚧
