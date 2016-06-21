from datetime import date, datetime
from app import db


class BlankFill(db.Model):
    __tablename__ = 'blank_fill'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    difficult_level = db.Column(db.Float)
    add_date = db.Column(db.Date, default=date.today)
    faq = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    knowledge_points = db.Column(db.Integer)
    subject = db.Column(db.Integer)
    knowledge_points_name = db.Column(db.String(127))
    subject_name = db.Column(db.String(127))

    answer = db.Column(db.String(255))

    def to_json(self):
        json = {
            'question': self.question,
            'difficult_level': self.difficult_level,
            'faq': self.faq,
            'timestamp': self.timestamp,
            'knowledge_points': self.knowledge_points_name,
            'subject': self.subject_name,
            'answer': self.answer,
        }
        return json

    @staticmethod
    def generate_fake(count=200):
        from random import seed, random, randint
        from models import Points, Subject
        import forgery_py

        seed()
        for i in range(count):
            bf = BlankFill(question=forgery_py.lorem_ipsum.sentence(),
                           difficult_level=random(),
                           faq=forgery_py.lorem_ipsum.sentence(),
                           knowledge_points=randint(1, 10),
                           subject=1,
                           answer=forgery_py.lorem_ipsum.sentence())

            p = Points.query.filter_by(id=bf.knowledge_points).first()
            bf.knowledge_points_name = p.name
            s = Subject.query.filter_by(id=bf.subject).first()
            bf.subject_name = s.name

            db.session.add(bf)
            db.session.commit()
