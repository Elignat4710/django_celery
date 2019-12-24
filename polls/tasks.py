from polls_project.celery_app import app
from django.utils import timezone
import requests
from .models import (
    Worker, Statistic, APPROVED, WorkPlace,
)
from django.core.mail import send_mail


@app.task(name='polls.tasks.register_worker')
def register_worker():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    list_worker = response.json()
    for worker in list_worker:
        Worker.objects.create(
            name=worker['name']
        )
    return Worker.objects.all()


@app.task(name='polls.tasks.statistic')
def statistic():
    current_date = timezone.localdate()
    workplaces = WorkPlace.objects.filter(status=APPROVED)

    for workplace in workplaces:
        interval_workplace = WorkPlace.objects.filter(
            date__gte=current_date - timezone.timedelta(7),
            date__lte=current_date
        )
        hours_total = 0

        for worktime in interval_workplace:
            hours_total += worktime.hours_worked

        Statistic.objects.create(
            workplace=workplace,
            hours_worked=hours_total
        )

        company = workplace.work.compnay
        worker_name = workplace.worker.name
        mail_list = list(company.manager.value_list('email', flat=True))
        overtime = hours_total - company.work.time_limit
        if overtime > 0:
            send_mail_overtime.delat(
                worker_name=worker_name,
                limit_hours=overtime,
                recipient_list=mail_list
            )


@app.task(name='polls.tasks.send_mail_overtime')
def send_mail_overtime(worker_name, limit_hours, recipient_list):
    send_mail(
        subject=f'Worker: {worker_name}. Oblajalsya!!!(kick him)',
        message=f'Worker: {worker_name}, exceeded the limit of hours'
        f'{limit_hours} per week',
        from_email='blabla@gmail.com',
        recipient_list=recipient_list
    )
