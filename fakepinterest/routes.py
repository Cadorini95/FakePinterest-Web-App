## CRIAÇÃO DA LÓGICA DE INTERAÇÃO DO SITE

import os
import werkzeug
from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.forms  import FormLogin, FormCriarConta, FormFoto
from fakepinterest.models import Usuario, Foto 
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename

import logging
logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=["GET", "POST"])
def homepage():
    
    form_login = FormLogin()

    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario:
            bcrypt.check_password_hash(usuario.senha, form_login.senha.data)
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))    

    return render_template("homepage.html", form=form_login)


@app.route("/criar_conta", methods=["GET", "POST"])
def criarconta():
    
    print("Rota /criar conta acessada.", flush=True)
    form_criar_conta = FormCriarConta()
    
    if form_criar_conta.validate_on_submit():
        print("Formulário validado com sucesso", flush=True)
        senha = bcrypt.generate_password_hash(form_criar_conta.senha.data)  ## BIBLIOTECA PARA CRIPTOGRAFIA DE SENHAS NO BANCO DE DADOS
        usuario = Usuario(  
                            username=form_criar_conta.username.data 
                          , senha=senha 
                          , email=form_criar_conta.email.data
                         )
        
        # ADIÇÃO DO NOVO USUÁRIO DENTRO DO BANCO DE DADOS
        try:
            database.session.add(usuario)
            database.session.commit()
            print("Usuário salvo no banco de dados", flush=True)
        except Exception as e:
            database.session.rollback()
            print(f"Erro ao salvar no banco de dados: {e}", flush=True)

        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    else:
        print("Formulário não validado", flush=True)
        print("Erros:", form_criar_conta.errors, flush=True)

    
    return render_template("criar_conta.html", form=form_criar_conta)


@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):

    if int(id_usuario) == int(current_user.id): ## USUÁRIO ESTÁ VERIFICANDO O PRÓPRIO PERFIL - PERMISSÃO DE UPLOAD DE FOTOS
        form_foto = FormFoto()
        
        if form_foto.validate_on_submit():
            arquivo        = form_foto.foto.data
            nome_seguro    = secure_filename(arquivo.filename)

            ## SALVANDO ARQUIVO NA PASTA /static/fotos_posts
            path_file = os.path.join(   
                                        os.path.abspath(os.path.dirname(__file__)),  ## LOCAL ONDE ARQUIVO routes.py ESTÁ HOSPEDADO
                                        app.config["UPLOAD_FOLDER"], 
                                        nome_seguro
                                    )
            arquivo.save(path_file)

            ## ADICIONANDO REGISTRO DA IMAGEM DENTRO DO BANCO DE DADOS
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()

        return render_template("perfil.html",usuario=current_user, form=form_foto)
    
    else:                                       ## USUÁRIO ESTÁ VERIFICANDO O PERFIL DE OUTRO USUÁRIO
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html",usuario=usuario, form=None)

@app.route('/logout')
@login_required
def logout():
    logout_user() 
    return redirect(url_for('homepage'))


@app.route("/feed")
@login_required
def feed():
    fotos=Foto.query.order_by(Foto.data_criaçao).all()
    return render_template('feed.html',fotos=fotos)

