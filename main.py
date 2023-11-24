from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from schemas import *

app = FastAPI()

last_driver_solicitude = None

solicitudes: Solicitude = [] 

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/driver")
async def create_driver(driver: DriverSolicitude):
    global last_driver_solicitude
    last_driver_solicitude = driver
    return {"driver": driver}

@app.post("/vehicle")
async def create_vehicle(vehicle: VehicleModel):
    global last_driver_solicitude
    if last_driver_solicitude is None:
        raise HTTPException(status_code=400, detail="No driver solicitude found")
    
    # Crea una nueva solicitud combinada y la agrega a la lista de solicitudes
    new_solicitude = Solicitude(DriverSolicitude=last_driver_solicitude, VehicleModel=vehicle)
    solicitudes.append(new_solicitude)

    # Resetea la solicitud de conductor para esperar una nueva
    last_driver_solicitude = None
    print(solicitudes)
    return {"solicitude": new_solicitude}

@app.get("/solicitudes")
async def get_solicitudes():
    return {"solicitudes": solicitudes}

@app.delete("/solicitude/{driver_solicitude_id}")
async def delete_solicitude(driver_solicitude_id: str):
    global solicitudes
    # Verifica si el id existe en la lista
    if not any(s.DriverSolicitude.id == driver_solicitude_id for s in solicitudes):
        raise HTTPException(status_code=404, detail="Solicitude not found")

    # Filtra la lista para eliminar la solicitud
    solicitudes = [s for s in solicitudes if s.DriverSolicitude.id != driver_solicitude_id]
    return {"message": "Solicitude deleted"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)