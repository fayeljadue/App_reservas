from db.Reservas_db import actualizar_reserva,get_idReserva,update_CancelarReserva,get_reservas
from db.ReservasHabitaciones_db import buscar_reserva_rango_f
from models.Reserva_models import CheckOut,ReservasCancelado,ReservasVisualizar
from models.Reserva_models import ReservasHabitaciones,ReservasVisualzarCompletoOut
from datetime import date
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.get("/")
async def index():
    return {"mensaje":"Bienvenido a la app de nuestras reservas"}

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

@api.get("/reserva/empleado/visualizar/{f_inicial}/{f_final}")
async def visualizar_reservas(f_inicial:str,f_final:str):
    fecha_incial = date(int(f_inicial[0:4]),int(f_inicial[4:6]),int(f_inicial[6:8]))
    fecha_final = date(int(f_final[0:4]),int(f_final[4:6]),int(f_final[6:8]))

    reservas_id,reservas_habitaciones = buscar_reserva_rango_f(fecha_incial,fecha_final)
    
    if reservas_habitaciones == None or reservas_id == None:
        return {"mensaje": "No hay reservas para estas fechas"}
    
    reservas = get_reservas(*reservas_id)
    salidaReservasCompletas = []

    for reserva in reservas:
        habitaciones_reservadas =[]
        for reserva_habitacion in reservas_habitaciones:
            if reserva_habitacion[1].id_reserva == reserva.id_reserva:
                habitaciones_reservadas.append(reserva_habitacion)
        ReservasVisualzarCompletoOut = {**reserva.dict(),"lista_habitaciones":dict(habitaciones_reservadas)}
        salidaReservasCompletas.append(ReservasVisualzarCompletoOut)
        habitaciones_reservadas.clear()
    return salidaReservasCompletas