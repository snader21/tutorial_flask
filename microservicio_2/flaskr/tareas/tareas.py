from ..app import db
from .. modelos import Cancion, CancionSchema
import os
from celery import Celery
from celery.signals import task_postrun

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

cancion_schema = CancionSchema()


@celery_app.task(name='tabla.registrar')
def registrar_puntaje(cancion_json):
    # se recibe el id de nuestro microservicio_1
    cancion = Cancion.query.get(cancion_json['id'])
    if cancion is None:
        cancion = Cancion(titulo=cancion_json['titulo'], minutos=cancion_json['minutos'],
                          segundos=cancion_json['segundos'], interprete=cancion_json['interprete'],
                          puntajes=[cancion_json['puntaje']])
        db.session.add(cancion)
    else:
        cancion.puntajes = cancion.puntajes + [cancion_json['puntaje']]
    db.session.commit()


@task_postrun.connect()
def close_session(*args, **kwargs):  # para no dejar abierta la base de datos
    db.session.remove()
