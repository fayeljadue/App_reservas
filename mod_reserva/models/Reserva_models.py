from pydantic import BaseModel

class CheckOut(BaseModel):
    id_reserva: int
    estado_reserva: str

class ReservasCancelado(BaseModel):
      id_reserva: int

class ReservasVisualizar(BaseModel):
    id_reserva: int
    id_quien_realiza: int
    nombre_cliente: str
    apellido_cliente: str
    cedula_cliente: str
    contacto_cliente: str
    estado_reserva: str
    cantidad_personas: int
