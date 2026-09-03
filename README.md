# Laboratorio 02: Aplicación Web de Gestión Veterinaria en Django

**Curso:** Desarrollo de Aplicaciones Empresariales  
**Integrante:** Sebastián Espíritu  

---

## 1. Problemática (Ejercicio 1)
En muchas veterinarias pequeñas, la programación y registro de citas de las mascotas se realiza manualmente o en agendas de papel. Esto origina desorganización, pérdida de datos, cruce de horarios y dificultad para consultar rápidamente la atención programada[cite: 1]. El sistema permite registrar y visualizar las citas de forma centralizada y será utilizado por el personal de la veterinaria para gestionar la atención.

---

## 2. Requisitos Funcionales (Ejercicio 2)
* **RF1:** El sistema debe permitir registrar una nueva cita médica.
* **RF2:** El sistema debe permitir ingresar el nombre de la mascota.
* **RF3:** El sistema debe permitir ingresar el nombre del propietario.
* **RF4:** El sistema debe permitir seleccionar el tipo de atención (Consulta, Vacunación, Desparasitación, Cirugía, Baño y Corte).
* **RF5:** El sistema debe permitir visualizar un listado tabular con las citas generadas.

---

## 3. Diseño del Modelo de Datos (Ejercicio 3)
**Entidad Principal:** 

| Campo | Tipo de Dato | Obligatorio | Justificación |
| :--- | :--- | :--- | :--- |
| **mascota** | Texto (`str`) | Sí | Identifica a la mascota que recibirá la atención médica. |
| **propietario** | Texto (`str`) | Sí | Identifica al cliente/dueño responsable de la mascota. |
| **tipo_atencion** | Texto / Select (`str`) | Sí | Indica el servicio o motivo de la consulta médica. |
| **fecha** | Fecha (`date`) | Sí | Establece el día programado para la cita. |
| **hora** | Hora (`time`) | Sí | Establece el horario asignado para la atención. |

---

## 4. Estructura del Proyecto y Flujo MVT (Ejercicios 4 - 9)

### Convivencia de Aplicaciones
El proyecto `sesion1` contiene dos aplicaciones independientes:
* **`landing`:** Administra la ruta principal (`/`) sirviendo la portada del laboratorio.
* **`veterinaria`:** Administra la ruta `/veterinaria/` ofreciendo la gestión de citas.

### Flujo MVT Aplicado
1. **Request:** El usuario navega a `/veterinaria/` o al formulario de creación `/veterinaria/crear/`.
2. **URL:** El archivo `urls.py` de la app enruta la petición hacia la vista correspondiente (`lista_citas` o `crear_cita`).
3. **View:** La vista procesa la solicitud[cite: 1]. En el caso del formulario (POST), valida los campos recibidos desde `forms.py` y agrega el nuevo registro en memoria.
4. **Model (Datos Estáticos):** Los datos se gestionan mediante una lista de diccionarios definida en `models.py`. *(Nota: Al no utilizar base de datos relacional ni migraciones, los nuevos registros persisten únicamente durante la ejecución del servidor)*.
5. **Template & Response:** La vista renderiza la plantilla HTML correspondiente (heredando de `templates/base.html`) devolviendo la respuesta al client.

---

## 5. Instrucciones de Ejecución

1. Activar el entorno virtual:
   ```bash
   .\venv\Scripts\activate

---

## 6. Evidencias del Funcionamiento

### Listado Inicial
<img width="1265" height="573" alt="Captura de pantalla 2026-09-03 093311" src="https://github.com/user-attachments/assets/60f0784b-6e8c-431b-bbc4-a791ae29d354" />

### Formulario de Registro
<img width="1268" height="690" alt="Captura de pantalla 2026-09-03 095040" src="https://github.com/user-attachments/assets/ec02f943-e2b6-44c9-927c-f5a1c23d7848" />

### Registro Agregado
<img width="1268" height="563" alt="Captura de pantalla 2026-09-03 095123" src="https://github.com/user-attachments/assets/cff8b79c-cbc2-4e65-af46-2ee33a5c1b0d" />
