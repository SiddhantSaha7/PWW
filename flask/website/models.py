from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PUBLIC_ACCESS_VIEW(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    PWWTitle = db.Column(db.String(1000))
    PWWShortDescription = db.Column(db.String(2500)) 
    PWWAdditionalNotes = db.Column(db.String(2500))
    CitationPageStart = db.Column(db.Integer)
    CitationPageEnd = db.Column(db.Integer)
    CitationMediaType = db.Column(db.String(20))
    CitationDOI = db.Column(db.String(100)) 
    CitationYear = db.Column(db.Integer) 
    PWWSourceUrl = db.Column(db.String(100)) 
    PWWGraphicRightsHolder = db.Column(db.String(100))
    ProofPdf = db.Column(db.String(100))
    PrimaryMscCode = db.Column(db.String(15))
    SecondaryMscCode = db.Column(db.String(100))
    Topics = db.Column(db.String(500))
    Theorems = db.Column(db.String(500))
    Citations = db.Column(db.String(500))
    Authors = db.Column(db.String(200))
    EntryCreator = db.Column(db.String(50))

    def __repr__(self):
        return f"PUBLIC_ACCESS_VIEW {self.PWWTitle}"
