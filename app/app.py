from fastapi import FastAPI, Form, HTTPException
import uvicorn
import requests
from sqlalchemy import desc

from models import session, Question

app = FastAPI()


def get_question(questions_num):
    response = requests.get(f"https://jservice.io/api/random?count={questions_num}")
    if response.status_code == 200:
        question_data = response.json()
        return question_data
    else:
        return None


def check_data_uniqueness(data):
    with session as session_obj:
        question = session_obj.query(Question).filter(Question.question_id == data['id']).first()

        if not question:
            return data

        new_data = get_question(1)
        return check_data_uniqueness(new_data)


@app.post('/question')
def add_question_on_database(questions_num: int = Form(...)):
    if not questions_num:
        raise HTTPException(status_code=400, detail="Question num is required")
    questions_data = get_question(questions_num)
    with session as session_obj:
        for i in questions_data:
            data = check_data_uniqueness(i)

            if not data:
                return 'Что-то пошло не так'

            new_question = Question(question_id=data['id'], question_text=data['question'],
                                    question_answer=data['answer'], created_at=data['created_at'])
            session_obj.add(new_question)
            session_obj.commit()

        latest_question = session_obj.query(Question).order_by(desc(Question.id)).first()

        if latest_question:
            return latest_question
        else:
            return {}


@app.get('/question/all')
def get_all():
    with session as session_obj:
        questions = session_obj.query(Question).all()
        return questions


if __name__ == "__main__":
    uvicorn.run(app)
