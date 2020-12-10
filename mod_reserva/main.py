from db.Reservas_db import actualizar_reserva
from models.Reserva_models import CheckOut
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.put("/reserva/chekout")
async def checkout(estado: CheckOut):
    resultado = actualizar_reserva(estado.id_reserva, estado.estado_reserva)
    return resultado
