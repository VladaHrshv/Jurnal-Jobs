from flask import Flask, render_template

from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def distribution():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    print(jobs.first())
    return render_template('jobs.html', title='Журнал работ', jobs_list=jobs)


def main():
    db_session.global_init(f"db/mars.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()