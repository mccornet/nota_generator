from types import MethodType
from flask import Flask, render_template, request, redirect, url_for, send_file, abort
from app import app, db
from app.models import Nota
from app.forms import AddNotaForm
from app.nota_generator import createAllNotasPDF, createSingleNotaPDF
from app.helper import nota_to_form, form_to_nota
import time

@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:id>', methods=['GET', 'POST'])
def index(id=None):
    nota = None 
    if id is not None:
        nota = Nota.query.get(id)
    else:
        nota = Nota.createNewNota()
    form = nota_to_form(nota)
    notas = Nota.query.order_by(Nota.id.desc()).all()
    token = time.time()

    return render_template('index.html', notas = notas, form = form, id = id, token = token)
 


@app.route('/update', methods=['GET', 'POST'])
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id=None):
    form = AddNotaForm()
    if request.method == 'POST':
        nota:Nota = form_to_nota(form, id)
        nota.updateDatabase()
    
    if id is not None:
        return redirect(url_for('index', _anchor=id))
    else:
        return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    Nota.deleteNota(id)
    return redirect(url_for('index'))

@app.route('/pdf/<int:id>/<float:token>')
def create_pdf(id, token):
    # -1 is used to create all notas
    pdf_name = None
    if id == 0:
        print("creating all pdfs")
        pdf_name = createAllNotasPDF()
    else:
        nota = Nota.query.get(id)
        pdf_name = createSingleNotaPDF(nota)
    
    path = f"./static/client/pdf/{pdf_name}"
    result = send_file(path, as_attachment=True)
    return result

    

