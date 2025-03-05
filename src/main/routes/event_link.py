from flask import Blueprint, jsonify, request

events_link_route_bp = Blueprint("events_link_route", __name__) #AGREGADOR DE ROTAS

from src.http_types.http_request import HttpRequest

from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.eventos_link_repository import EventosLinkRepository


@events_link_route_bp.route("/events_link", methods=["POST"]) #ROTA DE CRIAÇÃO DE EVENTOS
def create_new_link():
    eventos_link_repo = EventosLinkRepository()
    events_link_creator = EventsLinkCreator(eventos_link_repo)

    http_request = HttpRequest(body=request.json) #SEPARANDO O QUE PRECISO NA REQUISIÇAO HTTP

     # EXECUTANDO A LOGICA
    http_response = events_link_creator.create(http_request)

    #RETORNANDO AO USUÁRIO A INFORMAÇÃO
    return jsonify(http_response.body), http_response.status_code

    