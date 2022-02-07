import fastapi

from . import (
    crud,
    database,
    models,
    schemas
)


# def orm_include_routers(app: fastapi.FastAPI):
#     from . import (
#         api
#     )

#     app.include_router(api.router)
