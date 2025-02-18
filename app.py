from flask import Flask, render_template, redirect, request
from dbconfig import *
from pymysql import MySQLError as erroBD     #alterado aqui

app = Flask(__name__)

# ROTA PRINCIPAL
@app.route('/')
def index():
    try:
        conexao, cursor = conectar_db()
        comandoSQL = 'SELECT * FROM tarefas ORDER BY status'
        cursor.execute(comandoSQL)
        tarefas = cursor.fetchall()
    except erroBD as erro:    #alterado aqui
        print(f"Erro de BD: {erro}")
    except Exception as erro:    #alterado aqui
        print(f"Erro de backend: {erro}")
    finally:
        encerrar_db(cursor, conexao)
        return render_template('pages/index.html', tarefas=tarefas)

# ROTA PARA NOVA TAREFA
@app.route('/novatarefa', methods=['GET','POST'])
def novatarefa():
    if request.method == 'POST':
        try:
            descricao = request.form['descricao']
            data = request.form['data']
            conexao, cursor = conectar_db()
            comandoSQL = 'INSERT INTO tarefas (descricao, data) VALUES (%s, %s)'
            cursor.execute(comandoSQL,(descricao, data))
            conexao.commit()
        except Exception as erro:
            print(f'Erro de backend: {erro}')
        except erroBD as erro:
            print(f'Erro de Banco de Dados: {erro}')
        finally:
            encerrar_db(cursor, conexao)
    
    return redirect('/')

# ROTA PARA EDITAR TAREFA
@app.route('/excluir/<int:id_tarefa>')
def excluir(id_tarefa):
    try:
        conexao, cursor = conectar_db()
        comandoSQL = 'DELETE FROM tarefas WHERE id_tarefa = %s'
        cursor.execute(comandoSQL,(id_tarefa,))
        conexao.commit()
    except Exception as erro:
        print(f'Erro de backend: {erro}')
    except erroBD as erro:
        print(f'Erro de Banco de Dados: {erro}')
    finally:
        encerrar_db(cursor, conexao)
    return redirect('/')

# ROTA PARA EDITAR TAREFA
@app.route('/editartarefa/<int:id_tarefa>', methods=['GET','POST'])
def editartarefa(id_tarefa):
    if request.method == 'GET':
        try:
            conexao, cursor = conectar_db()
            comandoSQL = 'SELECT * FROM tarefas WHERE id_tarefa = %s'
            cursor.execute(comandoSQL,(id_tarefa,))
            tarefa = cursor.fetchone()
            # DUAS CONSULTAS
            comandoSQL = 'SELECT * FROM tarefas ORDER BY status'
            cursor.execute(comandoSQL)
            tarefas = cursor.fetchall()
        except Exception as erro:
            print(f'Erro de backend: {erro}')
        except erroBD as erro:
            print(f'Erro de Banco de Dados: {erro}')
        finally:
            encerrar_db(cursor, conexao)
        return render_template('pages/index.html',editar=True, tarefa=tarefa, tarefas=tarefas)

    if request.method == 'POST':
        try:
            conexao, cursor = conectar_db()
            descricao = request.form['descricao']
            data = request.form['data']
            comandoSQL = 'UPDATE tarefas SET descricao = %s, data = %s WHERE id_tarefa = %s'
            cursor.execute(comandoSQL,(descricao, data, id_tarefa))
            conexao.commit()
        except Exception as erro:
            print(f'Erro de backend: {erro}')
        except erroBD as erro:
            print(f'Erro de Banco de Dados: {erro}')
        finally:
            encerrar_db(cursor, conexao)
            return redirect('/')

# ROTA PARA MUDAR STATUS DA TAREFA
@app.route('/alterarstatus/<int:id_tarefa>')
def alterarstatus(id_tarefa):
    try:
        conexao, cursor = conectar_db()
        comandoSQL = 'SELECT status FROM tarefas WHERE id_tarefa = %s'
        cursor.execute(comandoSQL,(id_tarefa,))
        tarefa = cursor.fetchone()
        if tarefa['status'] == 'Pendente':
            novo_status = 'Concluída'
        else:
            novo_status = 'Pendente'
        comandoSQL = 'UPDATE tarefas SET status = %s WHERE id_tarefa = %s'
        cursor.execute(comandoSQL,(novo_status, id_tarefa))
        conexao.commit()
    except Exception as erro:
        print(f'Erro de backend: {erro}')
    except erroBD as erro:
        print(f'Erro de Banco de Dados: {erro}')
    finally:
        encerrar_db(cursor, conexao)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)