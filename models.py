# models.py
from extensions import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Projektname ist erforderlich

    # Metrics
    metrics_question1 = db.Column(db.Text, nullable=True)
    metrics_question2 = db.Column(db.Text, nullable=True)
    metrics_question3 = db.Column(db.Text, nullable=True)
    metrics = db.Column(db.Integer, nullable=True)
    metrics_comments = db.Column(db.Text, nullable=True)
    metrics_question_answered = db.Column(db.Boolean, nullable=False, default=False)

    # Economic Buyer
    economic_buyer_question1 = db.Column(db.Text, nullable=True)
    economic_buyer_question2 = db.Column(db.Text, nullable=True)
    economic_buyer_question3 = db.Column(db.Text, nullable=True)
    economic_buyer = db.Column(db.Integer, nullable=True)
    economic_buyer_comments = db.Column(db.Text, nullable=True)
    economic_buyer_question_answered = db.Column(db.Boolean, nullable=False, default=False)

    # Decision Criteria
    decision_criteria_question1 = db.Column(db.Text, nullable=True)
    decision_criteria_question2 = db.Column(db.Text, nullable=True)
    decision_criteria_question3 = db.Column(db.Text, nullable=True)
    decision_criteria = db.Column(db.Integer, nullable=True)
    decision_criteria_comments = db.Column(db.Text, nullable=True)
    decision_criteria_question_answered = db.Column(db.Boolean, nullable=False, default=False)

    # Decision Process
    decision_process_question1 = db.Column(db.Text, nullable=True)
    decision_process_question2 = db.Column(db.Text, nullable=True)
    decision_process_question3 = db.Column(db.Text, nullable=True)
    decision_process = db.Column(db.Integer, nullable=True)
    decision_process_comments = db.Column(db.Text, nullable=True)
    decision_process_question_answered = db.Column(db.Boolean, nullable=False, default=False)

    # Paper Process
    paper_process_question1 = db.Column(db.Text, nullable=True)
    paper_process_question2 = db.Column(db.Text, nullable=True)
    paper_process_question3 = db.Column(db.Text, nullable=True)
    paper_process = db.Column(db.Integer, nullable=True)
    paper_process_comments = db.Column(db.Text, nullable=True)
    paper_process_question_answered = db.Column(db.Boolean, nullable=False, default=False)

    # Implications of Pain
    implications_of_pain_question1 = db.Column(db.Text, nullable=True)
    implications_of_pain_question2 = db.Column(db.Text, nullable=True)
    implications_of_pain_question3 = db.Column(db.Text, nullable=True)
    implications_of_pain = db.Column(db.Integer, nullable=True)
    implications_of_pain_comments = db.Column(db.Text, nullable=True)
    implications_of_pain_question_answered = db.Column(db.Boolean, nullable=False, default=False)

    # Champion
    champion_question1 = db.Column(db.Text, nullable=True)
    champion_question2 = db.Column(db.Text, nullable=True)
    champion_question3 = db.Column(db.Text, nullable=True)
    champion = db.Column(db.Integer, nullable=True)
    champion_comments = db.Column(db.Text, nullable=True)
    champion_question_answered = db.Column(db.Boolean, nullable=False, default=False)

    # Competition
    competition_question1 = db.Column(db.Text, nullable=True)
    competition_question2 = db.Column(db.Text, nullable=True)
    competition_question3 = db.Column(db.Text, nullable=True)
    competition = db.Column(db.Integer, nullable=True)
    competition_comments = db.Column(db.Text, nullable=True)
    competition_question_answered = db.Column(db.Boolean, nullable=False, default=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    element = db.Column(db.String(50), nullable=False)  # z.B., 'metrics', 'economic_buyer', etc.
    number = db.Column(db.Integer, nullable=False)  # Frage Nummer: 1, 2, 3
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Question {self.element}_question{self.number}>"
