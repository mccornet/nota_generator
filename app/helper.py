from app.forms import AddNotaForm
from app.models import Nota

def float_safe(input:str) -> float:
    val = 0.0
    try:
        val = float(input)
    except:
        val = -1.0
    return val

def str_to_float(input:str) -> float:
    number = float_safe(input.replace(",","."))
    return number

def float_to_str(input:float, precision=2):
    return f'{input:.{precision}f}'.replace('.', ',')

def form_to_nota(form:AddNotaForm, id=None):

    nota = None

    if id is not None:
        nota = Nota.query.get(id)
    else:
        nota = Nota.createNewNota()

    # copy data
    nota.naam = form.naam.data
    nota.aanhef = form.aanhef.data
    # filter these texts to floats
    nota.contributie = str_to_float(form.contributie.data)
    nota.pacht = str_to_float(form.pacht.data)
    nota.nr_tuinen = str_to_float(form.nr_tuinen.data)
    nota.borg = str_to_float(form.borg.data)
    nota.ploegen = str_to_float(form.ploegen.data)
    nota.roteren = str_to_float(form.roteren.data)
    nota.overig = str_to_float(form.overig.data)
    
    nota.notaTotaal()

    # return nota
    return nota

def nota_to_form(nota:Nota):
    form = AddNotaForm()

    form.naam.data = nota.naam
    form.aanhef.data = nota.aanhef
    form.contributie.data = float_to_str(nota.contributie)
    form.pacht.data = float_to_str(nota.pacht)
    form.nr_tuinen.data = float_to_str(nota.nr_tuinen, 1)
    form.borg.data = float_to_str(nota.borg)
    form.ploegen.data = float_to_str(nota.ploegen)
    form.roteren.data = float_to_str(nota.roteren)
    form.overig.data = float_to_str(nota.overig)

    return form
