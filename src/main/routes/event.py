from flask import Blueprint, jsonify

event_route_bp = Blueprint("event_route", __name__) #AGREGADOR DE ROTAS

@event_route_bp.route("/event", methods=["POST"]) #ROTA DE CRIAÇÃO DE EVENTOS
def create_new_event():

    return jsonify({ "Estou": "AQUI!"}), 201