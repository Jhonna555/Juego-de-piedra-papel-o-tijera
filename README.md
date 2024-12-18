# Piedra, Papel o Tijera - Juego en Python

## Descripción
Este proyecto es un sencillo juego de "Piedra, Papel o Tijera" desarrollado en Python. El usuario compite contra la computadora, que realiza su elección de manera aleatoria. Es una implementación interactiva que permite al jugador disfrutar de partidas consecutivas hasta que decida finalizar.

## Objetivo del programa
El objetivo del programa es ofrecer una experiencia divertida y educativa para el usuario, permitiéndole aprender sobre:

- Lógica condicional.
- Uso de funciones en Python.
- Manejo de entradas del usuario.
- Generación de valores aleatorios.

## Principales funcionalidades del código

### 1. **Generación de la elección de la computadora**
La función `obtener_eleccion_computadora()` utiliza la librería `random` para generar una elección aleatoria entre "piedra", "papel" y "tijera". Esto garantiza que la computadora tenga resultados imparciales y aleatorios.

### 2. **Determinación del ganador**
La función `determinar_ganador(jugador, computadora)` aplica las reglas del juego para decidir el resultado:

- **Empate**: Si el jugador y la computadora eligen lo mismo.
- **Gana el jugador**: Si el jugador elige:
  - "piedra" y la computadora "tijera".
  - "papel" y la computadora "piedra".
  - "tijera" y la computadora "papel".
- **Pierde el jugador**: En cualquier otro caso.

### 3. **Ejecución del juego**
La función principal `jugar()`:

- Da la bienvenida al usuario.
- Solicita al jugador su elección.
- Valida la entrada para asegurarse de que sea válida ("piedra", "papel" o "tijera").
- Muestra la elección de la computadora.
- Muestra el resultado del juego.
- Permite jugar repetidamente hasta que el jugador decida salir.

### 4. **Interactividad y validaciones**
El programa está diseñado para manejar errores comunes, como entradas inválidas, y permite al usuario decidir si desea jugar otra partida.

## Instrucciones para ejecutar el programa
1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Descarga o clona este repositorio en tu computadora:
   ```bash
   git clone https://github.com/tu_usuario/piedra-papel-tijera.git
   ```
3. Navega al directorio del proyecto:
   ```bash
   cd piedra-papel-tijera
   ```
4. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

## Ejemplo de ejecución
```plaintext
¡Bienvenido al juego de Piedra, Papel o Tijera!
Elige piedra, papel o tijera: piedra
La computadora eligió: tijera
Resultado: Ganaste
¿Quieres jugar otra vez? (sí/no): no
Fin del juego. ¡Gracias por jugar!
```

## Datos del equipo
- **Integrante 1:** Jhonnatan Francisco Salazar Cadena
- **Institución:** Universidad Internacional del Ecuador
- **Carrera:** Ingeniería en Software Modalidad En Línea
- **Fecha:** 18 de diciembre del 2024

## Tecnologías utilizadas
- Lenguaje: Python 3
- Librería: `random`

## Notas adicionales
Este proyecto está desarrollado como parte de las actividades prácticas para aprender fundamentos de programación. Si tienes sugerencias o mejoras, no dudes en contribuir a través de pull requests.
