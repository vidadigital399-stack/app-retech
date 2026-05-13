# App Retech v1.0 - Plataforma Full (Base Productiva)

Plataforma para gestión remota legal de CPE/routers y testing autorizado.

## Incluye
- API FastAPI con JWT auth, usuarios, routers y jobs.
- Persistencia PostgreSQL con SQLAlchemy.
- Dashboard React para login y consulta de routers.
- Stack Docker Compose (api + web + db).
- Script k6 para smoke testing.

## Levantar
```bash
cp backend/.env.example backend/.env
cd infra
docker compose up --build
```

## Flujo inicial
1. Registrar usuario: `POST /auth/register`
2. Login: `POST /auth/login`
3. Usar token Bearer en `/routers` y `/jobs`

## Siguientes pasos enterprise
- RBAC granular, auditoría y logs inmutables.
- Integración ACS (GenieACS), SNMP polling, QoS policies.
- Cola de tareas (Celery/RQ), workers distribuidos y scheduler.
