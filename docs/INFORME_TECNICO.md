# Informe técnico — Arena Elemental

## 1. Análisis del problema
Arena Elemental es un videojuego de escritorio por turnos. El usuario elige un personaje, inicia una batalla, ataca y puede utilizar una poción. El programa permite practicar conceptos de programación orientada a objetos.

**Limitaciones:** funciona en una sola computadora, no tiene conexión en línea, no guarda partidas y cada batalla utiliza un enemigo aleatorio.

## 2. Diseño inicial
Se identificaron combatientes con atributos comunes (nombre y vida) y comportamientos diferentes (ataque). Se definió una clase abstracta `Combatiente`. `Guerrero`, `Mago`, `Slime` y `Dragon` especializan esa clase. `GestorBatalla` coordina los turnos y `VentanaPrincipal` presenta los controles.

## 3. Arquitectura
- `modelos/`: clases del dominio y reglas.
- `servicios/`: coordinación de la batalla.
- `interfaz/`: ventana y botones.
- `pruebas/`: pruebas automatizadas.
- `main.py`: punto de entrada.

## 4. Aplicación de POO
| Concepto | Aplicación |
|---|---|
| Clases y objetos | Guerrero, Mago, Slime y Dragón son clases que crean objetos. |
| Encapsulamiento | `_vida` se consulta mediante propiedades y se modifica con métodos validados. |
| Herencia | Los personajes y enemigos heredan de `Combatiente`. |
| Polimorfismo | Cada clase implementa su propia versión de `atacar()`. |
| Abstracción | `Combatiente` define el método abstracto `atacar()`. |
| Asociación | `GestorBatalla` utiliza al jugador y al enemigo. |
| Composición | La ventana crea y administra el gestor de batalla. |

## 5. Construcción de la interfaz
Se utilizó Tkinter. La ventana contiene selección de personaje, barras de vida, botones para iniciar, atacar y curarse, y un registro de eventos.

## 6. Proceso de desarrollo
1. Definir la idea de combate RPG por turnos.
2. Determinar las operaciones de iniciar, atacar y curar.
3. Diseñar la jerarquía abstracta de combatientes.
4. Implementar reglas de vida y combate.
5. Construir la ventana gráfica.
6. Conectar botones y lógica.
7. Agregar pruebas automatizadas.

## 7. Pruebas
Las pruebas están en `pruebas/test_combate.py`.
| Prueba | Resultado esperado |
|---|---|
| Vida mínima | La vida no baja de cero. |
| Curación máxima | La vida no supera el máximo. |
| Daño negativo | Se genera `ValueError`. |
| Inicio de batalla | Se crea un Slime o Dragón y la batalla queda activa. |

**Resultado:** las cuatro pruebas automatizadas se ejecutaron correctamente en el entorno de desarrollo. Se recomienda probar la interfaz gráfica en el equipo de entrega.

## 8. Problemas y soluciones
1. Se validaron daño y curación para evitar valores inválidos.
2. Se separaron las reglas de combate de la interfaz gráfica.

## 9. Conclusiones
El proyecto integra clases, objetos, encapsulamiento, herencia, polimorfismo, abstracción y relaciones entre objetos. Como mejora futura se podrían agregar sonidos, personajes, niveles y guardado de puntuaciones.
