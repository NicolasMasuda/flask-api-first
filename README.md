# APIFirst - API First con Flask y OpenAPI

## Descripción
Este proyecto es un ejemplo de **API First** utilizando **Flask** y **OpenAPI 3.1.1**.  
El objetivo es aprender a definir la API primero mediante un archivo de especificación (`openapi.yaml`) antes de implementar la lógica en Flask, siguiendo buenas prácticas de diseño y documentación.

Se incluye:
- Una estructura modular de Flask (`routes`, `controllers`, `models`).
- Un endpoint básico `/hello`.
- Documentación interactiva con **Swagger UI** disponible en `/docs`.
- Exposición del contrato OpenAPI en `/openapi.yaml`.

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

---

## Estructura del proyecto

```text
APIFirst/
│── app.py
│── requirements.txt
│── openapi.yaml
│
├── app/
│   ├── init.py
│   ├── routes/
│   │    └── hello.py
│   ├── controllers/
│   │    └── hello_controller.py
│   └── models/
│        └── init.py
```

