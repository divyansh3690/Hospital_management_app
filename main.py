from fastapi import  FastAPI
from database import engine
from router import auth, doctors,patients
import model

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(patients.router)

@app.get("/")
async def hello():
    return {"Working"}
