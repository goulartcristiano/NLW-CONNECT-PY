from flask import Blueprint, jsonify, request

event_route_bp = Blueprint("event_route", __name__) #AGREGADOR DE ROTAS

from src.validators.events_creator_validator import events_creator_validator

from src.http_types.http_request import HttpRequest

from src.controllers.eventos.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

@event_route_bp.route("/event", methods=["POST"]) #ROTA DE CRIAÇÃO DE EVENTOS
def create_new_event():
    events_creator_validator(request) #CRIA VALIDAÇÃO
    http_request = HttpRequest(body=request.json) #SEPARANDO O QUE PRECISO NA REQUISIÇAO HTTP

    # CRIANDO A LOGICA JUNTO AO REPOSITORIO
    eventos_repo = EventosRepository()
    events_creator = EventsCreator(eventos_repo)

    # EXECUTANDO A LOGICA
    http_response = events_creator.create(http_request)

    #RETORNANDO AO USUÁRIO A INFORMAÇÃO
    return jsonify(http_response.body), http_response.status_code