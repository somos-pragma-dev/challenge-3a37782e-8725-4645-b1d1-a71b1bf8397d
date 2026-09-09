# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto arrancable. Si el adjunto es una carcasa (docs/placeholders),
el asistente debe materializar la estructura del stack del briefing, sin resolver las fases del reto.

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
API REST con FastAPI y SQLAlchemy

### Reto
- Tema: API REST con FastAPI y SQLAlchemy
- Seniority: junior-l1
- Tipo: practical
- Título: Diseño y Desarrollo de una API REST en Banca
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición de la Estructura de Datos — objetivo: Definir los modelos de datos para préstamos y clientes. — entregable (NO resolver): Modelos de datos definidos y relaciones establecidas.
- Fase 2: Implementación de las Rutas de la API — objetivo: Implementar las rutas CRUD para préstamos y clientes. — entregable (NO resolver): Rutas CRUD implementadas y funcionando.
- Fase 3: Integración con la Base de Datos — objetivo: Integrar la API con una base de datos relacional. — entregable (NO resolver): API integrada con la base de datos y funcionando.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
// === ARCHIVO: src/models/loan.py ===
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    interest_rate = Column(Float, index=True)
    duration = Column(Integer, index=True)
    status = Column(String, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Client', back_populates='loans')


// === ARCHIVO: src/models/client.py ===
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    credit_history = Column(Float, index=True)
    loans = relationship('Loan', back_populates='client')


// === ARCHIVO: src/schemas/loan.py ===
from pydantic import BaseModel
from typing import Optional

class LoanCreate(BaseModel):
    amount: float
    interest_rate: float
    duration: int
    status: str
    client_id: int

class Loan(LoanCreate):
    id: int
    client_id: int

    class Config:
        orm_mode = True


// === ARCHIVO: src/schemas/client.py ===
from pydantic import BaseModel
from typing import Optional, List

class ClientCreate(BaseModel):
    name: str
    age: int
    credit_history: float

class Client(ClientCreate):
    id: int
    loans: List[Optional['Loan']] = []

    class Config:
        orm_mode = True


// === ARCHIVO: src/crud/loans.py ===
from sqlalchemy.orm import Session
from..models import Loan, Client
from..schemas.loan import LoanCreate, Loan

def create_loan(db: Session, loan: LoanCreate):
    db_loan = Loan(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

def get_loan(db: Session, loan_id: int):
    return db.query(Loan).filter(Loan.id == loan_id).first()

def update_loan(db: Session, loan_id: int, loan: LoanCreate):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is not None:
        for key, value in loan.dict().items():
            setattr(db_loan, key, value)
        db.commit()
        db.refresh(db_loan)
    return db_loan

def delete_loan(db: Session, loan_id: int):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is not None:
        db.delete(db_loan)
        db.commit()


// === ARCHIVO: src/crud/clients.py ===
from sqlalchemy.orm import Session
from..models import Client
from..schemas.client import ClientCreate, Client

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, client: ClientCreate):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is not None:
        for key, value in client.dict().items():
            setattr(db_client, key, value)
        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is not None:
        db.delete(db_client)
        db.commit()


// === ARCHIVO: src/main.py ===
from fastapi import FastAPI
from sqlalchemy.orm import Session
from.database import SessionLocal, engine
from.models import Base
from.crud.loans import create_loan, get_loan, update_loan, delete_loan
from.crud.clients import create_client, get_client, update_client, delete_client
from.schemas.loan import LoanCreate, Loan
from.schemas.client import ClientCreate, Client

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/loans/', response_model=Loan)
def create_new_loan(loan: LoanCreate, db: Session = SessionLocal):
    return create_loan(db=db, loan=loan)

@app.get('/loans/{loan_id}', response_model=Loan)
def read_loan(loan_id: int, db: Session = SessionLocal):
    db_loan = get_loan(db=db, loan_id=loan_id)
    if db_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    return db_loan

@app.put('/loans/{loan_id}', response_model=Loan)
def update_existing_loan(loan_id: int, loan: LoanCreate, db: Session = SessionLocal):
    updated_loan = update_loan(db=db, loan_id=loan_id, loan=loan)
    if updated_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    return updated_loan

@app.delete('/loans/{loan_id}')
def delete_existing_loan(loan_id: int, db: Session = SessionLocal):
    deleted_loan = delete_loan(db=db, loan_id=loan_id)
    if deleted_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    return {'detail': 'Loan deleted'}

@app.post('/clients/', response_model=Client)
def create_new_client(client: ClientCreate, db: Session = SessionLocal):
    return create_client(db=db, client=client)

@app.get('/clients/{client_id}', response_model=Client)
def read_client(client_id: int, db: Session = SessionLocal):
    db_client = get_client(db=db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return db_client

@app.put('/clients/{client_id}', response_model=Client)
def update_existing_client(client_id: int, client: ClientCreate, db: Session = SessionLocal):
    updated_client = update_client(db=db, client_id=client_id, client=client)
    if updated_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return updated_client

@app.delete('/clients/{client_id}')
def delete_existing_client(client_id: int, db: Session = SessionLocal):
    deleted_client = delete_client(db=db, client_id=client_id)
    if deleted_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return {'detail': 'Client deleted'}


// === ARCHIVO: src/database/database.py ===
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


// === ARCHIVO: tests/test_loans.py ===
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from..main import app, get_db
from..database import Base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_loan():
    response = client.post('/loans/', json={'amount': 1000, 'interest_rate': 5, 'duration': 12, 'status': 'active', 'client_id': 1})
    assert response.status_code == 200

def test_read_loan():
    response = client.get('/loans/1')
    assert response.status_code == 200

def test_update_loan():
    response = client.put('/loans/1', json={'amount': 1500, 'interest_rate': 6, 'duration': 18, 'status': 'inactive', 'client_id': 1})
    assert response.status_code == 200

def test_delete_loan():
    response = client.delete('/loans/1')
    assert response.status_code == 200


// === ARCHIVO: tests/test_clients.py ===
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from..main import app, get_db
from..database import Base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_client():
    response = client.post('/clients/', json={'name': 'John Doe', 'age': 30, 'credit_history': 750})
    assert response.status_code == 200

def test_read_client():
    response = client.get('/clients/1')
    assert response.status_code == 200

def test_update_client():
    response = client.put('/clients/1', json={'name': 'Jane Doe', 'age': 35, 'credit_history': 800})
    assert response.status_code == 200

def test_delete_client():
    response = client.delete('/clients/1')
    assert response.status_code == 200

```
