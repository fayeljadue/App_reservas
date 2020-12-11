from db.Reservas_db import actualizar_reserva,get_idReserva,update_CancelarReserva
from models.Reserva_models import CheckOut,ReservasCancelado,ReservasVisualizar
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.put("/reserva/chekout")
async def checkout(estado: CheckOut):
    resultado = actualizar_reserva(estado.id_reserva, estado.estado_reserva)
    return resultado


@api.put("/reserva/cancelar")
async def reservas_Cancelar(Reservas_Cancelado:  ReservasCancelado):
    Reserva_in_db = get_idReserva(Reservas_Cancelado.id_reserva)

    print(Reserva_in_db.estado_reserva)
    if  Reserva_in_db.estado_reserva in ["progreso","completada"]:
         raise HTTPException(status_code=404, detail="La reserva no se puede cancelar")

    if Reserva_in_db == None:
        raise HTTPException(status_code=404,detail="la reserva no existe")

    update_CancelarReserva(Reservas_Cancelado.id_reserva)
    return {"mensaje":"la reserva ha sido cancelada exitosamente"}

#pasar por url
@api.get("/reserva/visualizar/{id_reserva}")
async def reservas_Visualizar(id_reserva:int):
    Reserva_in_db = get_idReserva(id_reserva)
    
    if Reserva_in_db == None:
        raise HTTPException(status_code=404, detail="La reserva no existe")

    Reservas_Visualizar = ReservasVisualizar(**Reserva_in_db.dict())
    return  Reservas_Visualizar
