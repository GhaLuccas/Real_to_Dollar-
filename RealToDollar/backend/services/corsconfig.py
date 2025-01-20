# services/corsconfig.py
from fastapi.middleware.cors import CORSMiddleware


def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],  # Or specify your allowed origins here
        allow_credentials=True,
        allow_methods=['*'],  # Allows all HTTP methods
        allow_headers=['*'],  # Allows all headers
    )
