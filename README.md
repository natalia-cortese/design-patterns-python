# Patrones de diseño GoF en Python

Guía de uso de los **patrones de diseño del Gang of Four (GoF)** implementados en Python.

Los patrones están organizados en tres categorías según el libro *Design Patterns: Elements of Reusable Object-Oriented Software* (Gamma, Helm, Johnson, Vlissides):

## Patrones creacionales
- **Abstract Factory** — Familias de objetos relacionados
- **Builder** — Construcción paso a paso de objetos complejos
- **Factory Method** — Delegación de la creación en subclases
- **Prototype** — Clonación de objetos
- **Singleton** — Una única instancia

## Patrones estructurales
- **Adapter** — Adaptar interfaces incompatibles
- **Bridge** — Separar abstracción e implementación
- **Composite** — Estructuras en árbol de objetos
- **Decorator** — Añadir responsabilidades dinámicamente
- **Facade** — Interfaz simplificada a un subsistema
- **Flyweight** — Compartir estado para ahorrar memoria
- **Proxy** — Sustituto con control de acceso

## Patrones de comportamiento
- **Chain of Responsibility** — Pasar una petición por una cadena de manejadores
- **Command** — Encapsular una petición como objeto
- **Iterator** — Acceso secuencial a elementos
- **Mediator** — Objeto que centraliza la comunicación
- **Memento** — Capturar y restaurar estado interno
- **Observer** — Dependencia uno-a-muchos entre objetos
- **State** — Comportamiento según estado interno
- **Strategy** — Familias de algoritmos intercambiables
- **Template Method** — Esqueleto de algoritmo con pasos variables
- **Visitor** — Operaciones sobre una estructura sin modificarla

---

## Estructura del proyecto

```
design-patterns-python/
│
├── README.md
├── pyproject.toml
├── patterns/
│   ├── SOLID/
│   │   ├── dependencyInversion/
│   │   ├── interfaceSegregation/
│   │   ├── liskovSubstitution/
│   │   ├── openClose/
│   │   ├── overview/
│   │   ├── singleResponsability/
│   │
│   ├── creational/
│   │   ├── singleton/
│   │   ├── factory_method/
│   │   ├── abstract_factory/
│   │   ├── builder/
│   │   └── prototype/
│   │
│   ├── structural/
│   │   ├── adapter/
│   │   ├── bridge/
│   │   ├── composite/
│   │   ├── decorator/
│   │   ├── facade/
│   │   ├── flyweight/
│   │   └── proxy/
│   │
│   └── behavioral/
│       ├── chain_of_responsibility/
│       ├── command/
│       ├── interpreter/
│       ├── iterator/
│       ├── mediator/
│       ├── memento/
│       ├── observer/
│       ├── state/
│       ├── strategy/
│       ├── template_method/
│       └── visitor/
│
└── tests/

```

## Uso

Crear y activar el entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
```

Cada patrón incluye ejemplos ejecutables y explicaciones de cuándo y cómo usarlo.
