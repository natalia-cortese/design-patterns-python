# Patrones de diseño GoF en Python

Guía de uso de los **patrones de diseño del Gang of Four (GoF)** implementados en Python.

Vamos a comenzar agregando un pequeño apartado para repasar los principios SOLID, como veran estos principios se aplican en varios de los patrones luego
descriptos.

## SOLID
- **Dependency Inversion Principle** - Los módulos de alto nivel no deben depender de módulos de bajo nivel, ambos deben depender de abstracciones. Las abstracciones no deben depender de los detalles, los detalles deben depender de las abstracciones. Este principio promueve desacoplar el código, facilitando el mantenimiento y la escalabilidad de la aplicación. 
- **Interface Segregation Principle** - Los clientes no deben verse obligados a depender de interfaces que no utilizan. Es mejor tener varias interfaces específicas y pequeñas, en lugar de una sola interfaz grande. Esto ayuda a evitar la implementación de métodos innecesarios y permite que las clases sean más fáciles de mantener y extender.
- **Liskov Substitution Principle** - Los objetos de una subclase deben poder sustituir a objetos de la clase base sin alterar el correcto funcionamiento del programa. Es decir, si una clase hija hereda de una clase padre, debe poder ser utilizada en lugar de la clase padre sin que se produzcan errores o resultados inesperados. Este principio promueve la coherencia y la correcta utilización de la herencia en el diseño orientado a objetos.
- **Open Close Principle** - Las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para su extensión, pero cerradas para su modificación. Esto significa que el comportamiento de una entidad puede extenderse sin tener que modificar su código fuente, permitiendo agregar nuevas funcionalidades sin afectar el código existente. De esta manera, se promueve la reutilización y el mantenimiento, y se evitan errores causados por cambios en implementaciones ya probadas.
- **Single Responsibility Principle** - Cada módulo, clase o función debe tener una única responsabilidad, es decir, debe encargarse de una sola cosa o motivo para cambiar. Aplicar este principio facilita la comprensión, el mantenimiento y la reutilización del código, ya que los cambios en una responsabilidad específica impactan únicamente al módulo encargado de ella, y no afectan otras partes del sistema.

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
