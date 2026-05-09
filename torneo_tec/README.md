# Sistema de Registro para Torneo de Videojuegos

Este proyecto consiste en un sistema básico en Python para registrar participantes de un torneo de videojuegos utilizando Programación Orientada a Objetos (POO) y herencia.

## Archivos incluidos

- `Jugador.py` → Clase base que contiene la información general de los jugadores.
- `Competidor.py` → Clase derivada que representa a los jugadores competidores.
- `Observador.py` → Clase derivada que representa a los observadores del torneo.
- `main.py` → Archivo principal donde se crean objetos y se prueban los métodos.

---

## Objetivo

Aplicar los conceptos básicos de Programación Orientada a Objetos en Python mediante:

- Creación de clases y objetos
- Uso de herencia
- Sobreescritura de métodos
- Uso de `super()`
- Manejo de atributos y métodos

---

## Funcionalidades del sistema

### Clase Jugador
La clase base permite:

- Registrar nombre del jugador
- Registrar número de control
- Registrar nivel del jugador
- Llevar control de puntos
- Ganar puntos
- Perder puntos sin permitir valores negativos
- Mostrar el perfil del jugador

---

### Clase Competidor
La clase `Competidor` hereda de `Jugador` y además:

- Guarda el nombre del equipo
- Sobreescribe el método `mostrar_perfil()`

---

### Clase Observador
La clase `Observador` hereda de `Jugador` y además:

- Lleva registro de partidas vistas
- Gana puntos automáticamente al ver partidas
- Sobreescribe el método `mostrar_perfil()`

---

## Conceptos aplicados

Durante esta práctica se utilizaron los siguientes conceptos:

- Clases y objetos
- Herencia
- Encapsulación básica
- Métodos
- Constructores `__init__`
- Sobreescritura de métodos
- Uso de `super()`
- Condicionales