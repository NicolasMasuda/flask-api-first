# APIFirst - API First con Flask y OpenAPI

## Descripción
Este proyecto es un ejemplo de **API First** utilizando **Flask** y **OpenAPI 3.1.1**.  
El objetivo es aprender a definir la API primero mediante un archivo de especificación (`openapi.yaml`) antes de implementar la lógica en Flask, siguiendo buenas prácticas de diseño y documentación.

Se incluye:
- Una estructura modular de Flask (`routes`, `controllers`, `models`).
- Un endpoint básico `/hello`.
- Documentación interactiva con **Swagger UI** disponible en `/docs`.
- Exposición del contrato OpenAPI en `/openapi.yaml`.
- **Validación automática de requests** usando OpenAPI Validator.

---

## Conceptos básicos

### API First
API First significa que **primero se define la API** como un contrato (OpenAPI) y luego se implementa. Esto permite:
- Mejor comunicación entre equipos.
- Validación temprana de la API.
- Generación de documentación y clientes automáticamente.

### OpenAPI
OpenAPI es un **estándar para describir APIs REST**. Define:
- Endpoints (`paths`)
- Métodos HTTP (GET, POST, PUT, DELETE)
- Estructura de datos (`schemas`)
- Respuestas esperadas (`responses`)

### Swagger UI
Swagger UI permite **visualizar y probar la API** directamente desde el navegador a partir del archivo OpenAPI.

### OpenAPI Validator
El validador OpenAPI permite **validar automáticamente** las peticiones entrantes contra la especificación definida, similar al middleware.

#### Validación Global (como Express middleware)
- **Una sola configuración** en `app/__init__.py`
- **Validación automática** de todos los requests
- **Sin código repetitivo** en las rutas

#### Rutas Limpias
- **Sin decoradores** en cada función
- **Sin validación manual** en el código
- **Enfoque en la lógica de negocio**

#### Consistencia con OpenAPI
- **Validación directa** desde el archivo `openapi.yaml`
- **Sincronización automática** entre documentación y validación
- **API First** real: el contrato define el comportamiento

#### Conclusión

La implementación de OpenAPI Validator en Flask proporciona:

✅ **Validación automática** de requests contra la especificación OpenAPI  
✅ **Rutas limpias** sin código de validación repetitivo  
✅ **Middleware global** similar a Express.js  
✅ **Manejo consistente** de errores de validación  
✅ **API First** verdadero donde el contrato define el comportamiento  

Este enfoque optimiza el desarrollo al garantizar que todas las peticiones cumplan con la especificación OpenAPI definida, facilitando el mantenimiento y la comunicación entre equipos.

---

## Estructura del proyecto

```text
APIFirst/
│── app.py
│── requirements.txt
│── openapi.yaml                    ← Actualizado con /users
│
├── app/
│   ├── __init__.py                 ← Validador global
│   ├── routes/
│   │    ├── hello.py               ← Sin cambios
│   │    ├── users.py               ← NUEVO - endpoint usuarios
│   │    └── docs.py
│   └── controllers/
│        ├── hello_controller.py
│        └── user_controller.py     ← NUEVO - lógica de usuarios
```
