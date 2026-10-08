from celery import Celery

app = Celery(
    'demo',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)


@app.task
def add(x, y):
    return x + y


@app.task
def send_email(email):
    print(f"Sending email to {email}")
    return f"Email sent to {email}"
