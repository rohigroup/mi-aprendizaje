# Plan de Estudio — Full Stack Developer + Python + SQL
**Jessica Leal Corzo | 2026**

## Stack objetivo
Python 3.12 | PostgreSQL 16 | React + TypeScript | FastAPI

---

## Fase 1 — Python real + SQL con sentido (semanas 1–6)

### Semana 1 — Python: tipos, variables, control de flujo
**Temas:** int, float, str, bool, None, f-strings, if/elif/else, for, while, range(), enumerate()
**Ejercicio:** Script de ingresos mensuales Hotel Urak con f-strings y control de flujo
**Archivo:** semana-01-python/reporte-hotel.py ✓

### Semana 2 — Python: funciones, listas, diccionarios
**Temas:** def, return, *args, **kwargs, scope, list comprehensions, dict comprehension, map(), filter()
**Ejercicio:** Procesador de habitaciones con dicts, list comprehensions y funciones propias

### Semana 3 — SQL: SELECT real y JOINs que entiendes
**Temas:** WHERE, AND/OR, IN, BETWEEN, LIKE, INNER/LEFT JOIN, GROUP BY, HAVING, COUNT, SUM, AVG
**Ejercicio:** Schema de Hotel Urak en PostgreSQL + 6 queries de reporte con JOINs reales

### Semana 4 — Python: OOP, archivos, manejo de errores
**Temas:** Clases, __init__, self, herencia, open(), csv module, json module, try/except, virtual environments
**Ejercicio:** Clase Reserva + Hotel con OOP, leer CSV, manejar errores, exportar a JSON

### Semana 5 — SQL: CTEs, subqueries, window functions
**Temas:** Subqueries, WITH (CTEs), ROW_NUMBER, RANK, LAG, LEAD, OVER PARTITION BY, transacciones
**Ejercicio:** CTEs de ocupación, ranking con window functions, upsert con ON CONFLICT

### Semana 6 — Python + SQL juntos
**Temas:** psycopg2, queries parametrizadas, python-dotenv, CRUD desde Python, supabase-py
**Ejercicio:** CRUD completo de reservas — Python + Supabase + .env + error handling

---

## Fase 2 — Frontend con fundamentos (semanas 7–14)

### Semana 7 — HTML semántico + CSS box model
**Temas:** Semántica HTML, box model, Flexbox completo, variables CSS, responsive sin frameworks
**Ejercicio:** Página de inicio Hotel Urak — HTML semántico + CSS puro

### Semana 8 — JavaScript: DOM, eventos, fetch()
**Temas:** querySelector, addEventListener, bubbling, Promises, async/await, fetch(), closures
**Ejercicio:** Disponibilidad de habitaciones en vanilla JS — DOM, fetch, sin frameworks

### Semanas 9–10 — React: componentes, hooks, estado
**Temas:** JSX, componentes funcionales, useState, useEffect, props, formularios, TypeScript básico
**Ejercicio:** Módulo de reservas de Arribo desde cero — React + TypeScript + hooks

### Semanas 11–12 — CSS Grid, Tailwind y responsive real
**Temas:** CSS Grid, Tailwind utility classes, mobile-first, breakpoints
**Ejercicio:** Dashboard de Arribo con CSS Grid + Tailwind — responsive real

### Semanas 13–14 — React avanzado: Context, Router, TypeScript
**Temas:** Context API, React Router, TypeScript estricto, llamadas a Supabase
**Ejercicio:** Mini Arribo completo — Router, Context, TypeScript + Supabase real

---

## Fase 3 — Backend con Python y FastAPI (semanas 15–24)

### Semanas 15–16 — HTTP, APIs REST y FastAPI básico
**Temas:** HTTP methods, status codes, headers, CORS, FastAPI routing, Pydantic, Swagger automático
**Ejercicio:** API REST de Hotel Urak en FastAPI — CRUD con Pydantic y Swagger

### Semanas 17–18 — FastAPI + PostgreSQL + autenticación JWT
**Temas:** SQLAlchemy, JWT, endpoints protegidos, dependencias, Alembic migraciones
**Ejercicio:** FastAPI + PostgreSQL + JWT — auth completa, migraciones Alembic

### Semanas 19–20 — Testing, Docker y deploy real
**Temas:** pytest, fixtures, Dockerfile, docker-compose, variables de entorno, Railway deploy
**Ejercicio:** Tests con pytest + Dockerfile + deploy real en Railway

### Semanas 21–24 — Proyecto integrador full stack
**Stack:** React + FastAPI + PostgreSQL + deploy completo
**Proyecto:** Portal de reportes y gestión de Hotel Urak — tu portafolio real

---

## Reglas del juego

1. Antes de copiar código, escribe en papel qué hace
2. Commit diario, aunque sea un archivo con notas
3. 15 minutos de debugging antes de preguntar
4. Cada ejercicio en su propio repositorio de GitHub
5. Usa tus contextos reales — Hotel Urak, Arribo, Sin Enredo, De Casa
6. Codecademy para el concepto, ejercicio propio para el aprendizaje real
7. No avances de semana si no puedes explicar la anterior

---

## Herramientas instaladas
- iTerm2 + Oh My Zsh ✓
- Homebrew ✓
- pyenv + Python 3.12.4 ✓
- PostgreSQL 16 + TablePlus ✓
- Git con SSH a GitHub ✓
- VS Code + 12 extensiones ✓
- Node v24 + npm v11 con nvm ✓
