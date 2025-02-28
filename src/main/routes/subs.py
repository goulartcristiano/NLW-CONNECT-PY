from flask import Blueprint, jsonify, request

subs_route_bp = Blueprint("subs_route", __name__) #AGREGADOR DE ROTAS

from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.model.repositories.inscritos_repository import InscritosRepository

from src.controllers.inscritos.subscribers_creator import SubscriberCreator

@subs_route_bp.route("/subscriber", methods=["POST"]) #ROTA DE CRIAÇÃO DE INSCRITOR
def create_new_subs():
    subscribers_creator_validator(request) #CRIA VALIDAÇÃO
    http_request = HttpRequest(body=request.json) #SEPARANDO O QUE PRECISO NA REQUISIÇAO HTTP

    subs_repo = InscritosRepository()
    subs_creator = SubscriberCreator(subs_repo)


    http_response = subs_creator.create(http_request)


    return jsonify(http_response.body), http_response.status_code