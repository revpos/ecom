import uuid

from fastapi import FastAPI, Request

from user_site.infrastructure.logging import setup_logging, request_id_ctx_var

from user_site.api.v1.user_routes import user_router


setup_logging()

app = FastAPI(title="rev-store")

app.include_router(user_router)


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.middleware("http")
async def log_request_id(request: Request, call_next):
    # 1. Generate or grab ID from headers
    req_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    
    # 2. Set the context variable
    token = request_id_ctx_var.set(req_id)
    
    try:
        response = await call_next(request)
        response.headers["X-Request-ID"] = req_id
        return response
    finally:
        # 3. Clean up
        request_id_ctx_var.reset(token)