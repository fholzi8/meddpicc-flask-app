# forms.py
import json
import os
import logging
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_edit_questions_form():
    """
    Dynamisch eine FlaskForm-Klasse erstellen basierend auf questions.json.
    """
    class EditQuestionsForm(FlaskForm):
        submit = SubmitField('Speichern')

    questions_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'questions.json')
    try:
        with open(questions_path, 'r', encoding='utf-8') as f:
            questions = json.load(f)
            for element, element_questions in questions.items():
                for q_key, q_text in element_questions.items():
                    field_name = f"{element}_{q_key}"  # z.B., metrics_question1
                    label = f"{q_key.replace('question', 'Frage ')} ({element.replace('_', ' ').capitalize()})"
                    # Hinzufügen eines TextAreaField zur Formularklasse
                    setattr(EditQuestionsForm, field_name, TextAreaField(label, validators=[DataRequired()]))
    except FileNotFoundError:
        logger.error("questions.json Datei wurde nicht gefunden.")
    except json.JSONDecodeError:
        logger.error("Fehler beim Parsen der questions.json Datei.")
    
    return EditQuestionsForm

def load_questions():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    questions_path = os.path.join(base_dir, 'static', 'questions.json')
    try:
        with open(questions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Begrenze die Anzahl der Fragen pro Element auf 3
            for element, questions in data.items():
                if len(questions) > 3:
                    logger.warning(f"Element '{element}' hat mehr als 3 Fragen. Überschüssige Fragen werden ignoriert.")
                    data[element] = {k: v for k, v in list(questions.items())[:3]}
            return data
    except FileNotFoundError:
        logger.error(f"Die Datei {questions_path} wurde nicht gefunden.")
        return {}
    except json.JSONDecodeError:
        logger.error("Fehler beim Parsen der JSON-Datei.")
        return {}

questions = load_questions()

def create_project_form():
    # Basisfelder
    form_fields = {
        'name': StringField('Projektname', validators=[DataRequired()]),  # Erforderlich
    }

    # Dynamisch Felder hinzufügen
    for element, element_questions in questions.items():
        for q_key, q_text in element_questions.items():
            field_name = f"{element}_question{q_key[-1]}"  # z.B., metrics_question1
            form_fields[field_name] = TextAreaField(q_text)  # Optional
            #logger.info(f"Hinzufügen von Feld: {field_name}")
        # IntegerField für den Score
        form_fields[element] = IntegerField(f'{element.replace("_", " ").capitalize()} Wert (1-10)', validators=[NumberRange(min=1, max=10)])
        #logger.info(f"Hinzufügen von Feld: {element}")

    # Submit-Button
    form_fields['submit'] = SubmitField('Speichern')

    # Erstellen der Form-Klasse
    #logger.info("ProjectForm-Klasse wird erstellt.")
    return type('ProjectForm', (FlaskForm,), form_fields)

# Erstelle die Form-Klasse
ProjectForm = create_project_form()
