from app.models import Nota
from datetime import date
import pdfkit

current_year = date.today().year

css = "./app/static/css/nota.css"

# turns a float into a string with custom precision and a comma
def cs(input:float, precision:int=2):
    return f"{input:.{precision}f}".replace('.', ',')

def createNotaTable(nota:Nota):
    html_table = """
    <table class="nota_tabel">
    <tr><th class="omschrijving">Omschrijving</th><th class="bedrag">Bedrag</th></tr>
    """
    # Contributie
    html_table += f"<tr><td class=\"omschrijving\">Contributie</td><td class=\"number\">&euro;{cs(nota.contributie)}</td></tr>\n"

    # Pacht
    html_table += f"<tr><td class=\"omschrijving\">Pacht voor {cs(nota.nr_tuinen, 1)} tuin/en</td><td class=\"number\">&euro;{cs(nota.pacht)}</td></tr>\n"
    
    # Borg
    if nota.borg > 0:
        html_table += f"<tr><td class=\"omschrijving\">Borg</td><td  class=\"number\">&euro;{cs(nota.borg)}</td></tr>\n"
    
    # Ploegen
    if nota.ploegen > 0:
        html_table += f"<tr><td class=\"omschrijving\">Ploegen</td><td class=\"number\">&euro;{cs(nota.ploegen)}</td></tr>\n"
    
    # Roteren
    if nota.roteren > 0:
        html_table += f"<tr><td class=\"omschrijving\">Roteren</td><td class=\"number\">&euro;{cs(nota.roteren)}</td></tr>\n"
    
    # overig
    if nota.overig > 0:
        html_table += f"<tr><td class=\"omschrijving\">Overig</td><td class=\"number\">&euro;{cs(nota.overig)}</td></tr>\n"
    
    # Totaal
    html_table += f"<tr class=\"total\"><td class=\"omschrijving\"><b>Totaal<b></td><td class=\"number\">&euro;{cs(nota.totaal)}</td></tr>\n"

    html_table += "</table>\n"

    return html_table

def createNotaHeaderHTML(title:str="Notas Tuinvereniging"):
    html_header = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <link rel="stylesheet" href="../static/css/nota.css">
            <title>{title}</title>
        </head>
        <body>
    """
    return html_header

def createNotaFooterHTML():
    html_footer = """
        </body>
    </html>
    """
    return html_footer

def createNotaContentHTML(nota:Nota, year:int=current_year):
    html_nota_table = createNotaTable(nota)
    #type_of_nota_content = "multi_nota" if multiple_notas else "single_nota"
    type_of_nota_content = "a4_size_nota"

    nota_content_html = f"""
        <div class="{type_of_nota_content}">
            <p class="nota_information">
                <b>Volkstuinvereniging &ldquo;Niervaert&rdquo; te Klundert</b>
                <br />
                Bank: NL95 RABO 0126 0084 26 
                <br />
                E-mail: volkstuinklundert@gmail.com
            </p>

            <p class="nota_subject">
            Onderwerp: nota seizoen {year} Complex Stoofdijk / Schansweg
            </p>

            <p class="salutation">
            Geachte {nota.aanhef} {nota.naam},
            </p>

            <p>
            In de onderstaande tabel vind u de kostenopbouw van de huur van uw tuin(en):

            <div class="nota_tabel_container">
            {html_nota_table}
            </div>

            <p>
            U wordt vriendelijk verzocht het totale bedrag z.s.m. 
            over te maken op bovenstaand rekeningnummer.
            </p>
            
            <p class="valediction">
            Bij voorbaat onze hartelijke dank, 
            <br />
            <br />
            Namens het bestuur 
            <br />
            <img src="http://localhost/static/img/paraaf_100px.png" style="height: 50px; margin-top:10px; margin-bottom:10px;">
            <br />
            de penningmeester
            </p>  
        </div>
    """
    return nota_content_html

def createSingleNotaHTML(nota:Nota, year:int=current_year):
    header = createNotaHeaderHTML(nota.naam)
    content = createNotaContentHTML(nota, year)
    footer = createNotaFooterHTML()
    nota_html = "".join([header, content, footer])

    # clean the html
    lines = [line.strip() for line in nota_html.splitlines()]   
    nota_html = "\n".join(lines)
    return nota_html

def createAllNotaHTML(year:int=current_year):
    header = createNotaHeaderHTML()
    notas = Nota.query.all()
    new_page = "<div class=\"new_page\"></div>"
    content = new_page.join([createNotaContentHTML(nota) for nota in notas])
    footer = createNotaFooterHTML()
    notas_html = "".join([header, content, footer])

    # clean the html
    lines = [line.strip() for line in notas_html.splitlines()]   
    notas_html = "\n".join(lines)
    return notas_html


options = {'quiet': '',
           'page-size': 'A4',
           'margin-top': '0.75in',
           'margin-right': '0.75in',
           'margin-bottom': '0.75in',
           'margin-left': '0.75in',}

def createSingleNotaPDF(nota:Nota):  
    html = createSingleNotaHTML(nota)
    datum = f"{date.today().day}_{date.today().month}_{date.today().year}"
    pdf_name = f"Nota_Tuinvereniging_{nota.naam}_{datum}.pdf"
    pdf_location = f"./app/static/client/pdf/{pdf_name}"  
    pdfkit.from_string(html, pdf_location, options=options, css=css)
    return pdf_name

def createAllNotasPDF():
    html = createAllNotaHTML()
    datum = f"{date.today().day}_{date.today().month}_{date.today().year}"
    pdf_name = f"Notas_Tuinvereniging_{datum}.pdf"
    pdf_location = f"./app/static/client/pdf/{pdf_name}"
    pdfkit.from_string(html, pdf_location, options=options, css=css)
    return pdf_name