from app import db

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(120))
    aanhef = db.Column(db.String(25))
    contributie = db.Column(db.Float)
    pacht = db.Column(db.Float)
    nr_tuinen = db.Column(db.Float)
    borg = db.Column(db.Float)
    ploegen = db.Column(db.Float) 
    roteren = db.Column(db.Float)
    overig = db.Column(db.Float)
    totaal = db.Column(db.Float)

    def __repr__(self):
        return f'''{self.naam} betaalt: {self.totaal}.'''

    def createNewNota():
        emptyNota = Nota(id = None,
                        naam = "nieuw lid",
                        aanhef = "m/v",
                        contributie = 0.00,
                        pacht = 0.00,
                        nr_tuinen = 0.00,
                        borg = 0.00,
                        ploegen = 0.00,
                        roteren = 0.00,
                        overig = 0.00,
                        totaal = 0.00,
                        )
        return emptyNota

    def notaTotaal(self):
        self.totaal = (self.contributie +
                        self.pacht +
                        self.borg +
                        self.ploegen +
                        self.roteren +
                        self.overig)
        return

    def updateDatabase(self):

        # new nota?
        if self.id == None:
            db.session.add(self)
        
        # update database
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return
    
    def deleteNota(id):
        nota = Nota.query.get(id)

        db.session.delete(nota)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return