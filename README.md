# Arena Elemental — Batallas RPG

Videojuego de escritorio por turnos desarrollado en Python con programación orientada a objetos y Tkinter.

## Problema
El proyecto busca ofrecer un juego corto y fácil de utilizar que permita practicar la organización de un programa mediante clases, objetos y una interfaz gráfica.

## Objetivos
- Aplicar los principios principales de POO.
- Separar la lógica del combate de la interfaz.
- Permitir jugar una batalla por turnos desde una ventana gráfica.

## Funcionalidades
1. Elegir entre Guerrero y Mago.
2. Iniciar una batalla contra un enemigo aleatorio (Slime o Dragón).
3. Atacar y observar el daño realizado y recibido.
4. Usar una poción que recupera hasta 25 puntos de vida.
5. Consultar las barras de vida y el registro del combate.

## Tecnologías
- Python 3.10 o superior.
- Tkinter para la interfaz gráfica.
- `abc` para la clase abstracta.
- `random` para los ataques y selección de enemigos.
- `unittest` para las pruebas.

No se requieren bibliotecas externas.

## Instalación
1. Instala Python 3.10 o superior desde https://www.python.org/.
2. Descarga o clona este repositorio.
3. Abre una terminal en la carpeta del proyecto.

En algunas distribuciones de Linux puede ser necesario instalar el paquete `python3-tk`.

## Ejecución
```bash
python main.py
```

## Manual de usuario
1. Ejecuta el programa.
2. Selecciona Guerrero o Mago.
3. Presiona **Iniciar batalla**.
4. Presiona **Atacar** para realizar un ataque y recibir la respuesta del enemigo.
5. Presiona **Usar poción (+25)** para recuperar vida; la acción consume el turno.
6. Cuando termine el combate, presiona **Nueva batalla**.

## Pruebas
```bash
python -m unittest discover -s pruebas -v
```

## Estructura
```text
arena_elemental/
├── main.py
├── modelos/
│   ├── entidad.py
│   ├── personajes.py
│   └── enemigos.py
├── servicios/
│   └── gestor_batalla.py
├── interfaz/
│   └── ventana_principal.py
├── pruebas/
│   └── test_combate.py
├── docs/
│   └── INFORME_TECNICO.md
└── README.md
```

## Autor
Estudiante: completar con nombre y grupo antes de entregar.
