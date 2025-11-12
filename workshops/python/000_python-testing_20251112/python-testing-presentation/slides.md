---
theme: seriph
background: https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80
title: Python Testing Workshop
info: |
  ## Python Testing Workshop
  Aprende a escribir tests efectivos en Python
  
  - unittest, pytest, hypothesis
  - Fixtures, mocking, parameterización
  - Tests unitarios, integración, end-to-end
  - TDD y mejores prácticas

class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
duration: 45min
---

# Python Testing Workshop

## Aprende a escribir tests efectivos en Python

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover:bg="white op-10">
    Empezar el taller <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---
transition: fade-out
---

# ¿Por qué hacer tests?

Los tests son fundamentales para el desarrollo de software de calidad

<v-clicks>

- 🐛 **Detectar bugs** - Encuentra errores antes de que lleguen a producción
- 🔒 **Confianza** - Refactoriza y cambia código sin miedo
- 📚 **Documentación** - Los tests documentan cómo funciona tu código
- 🚀 **Velocidad** - Desarrollo más rápido a largo plazo
- 🛡️ **Regresiones** - Evita que bugs antiguos vuelvan a aparecer

</v-clicks>

<br>
<br>

<v-click>

> "Testing shows the presence, not the absence of bugs" - Edsger Dijkstra

</v-click>

---

# Tipos de Tests

<div class="grid grid-cols-2 gap-8">

<div>

## Por Alcance
<v-clicks>

- **Unit Tests** - Funciones/métodos individuales
- **Integration Tests** - Interacción entre componentes  
- **End-to-End Tests** - Flujo completo de usuario
- **Smoke Tests** - Funcionalidad básica

</v-clicks>

</div>

<div>

## Por Propósito
<v-clicks>

- **Regression Tests** - Evitar bugs conocidos
- **Performance Tests** - Rendimiento del sistema
- **Security Tests** - Vulnerabilidades
- **Property Tests** - Propiedades matemáticas

</v-clicks>

</div>

</div>

<v-click>

<div class="mt-8 p-4 bg-dark-50 rounded">
💡 <strong>Pirámide de Tests:</strong> Muchos unit tests, algunos integration tests, pocos E2E tests
</div>

</v-click>

---

# Herramientas del Taller

Las librerías que vamos a explorar hoy

<div class="grid grid-cols-2 gap-6 mt-8">

<div>

## Testing Frameworks
- **unittest** - Librería estándar de Python
- **pytest** - Framework moderno y potente
- **hypothesis** - Property-based testing

</div>

<div>

## Herramientas Adicionales
- **testcontainers** - Tests con Docker
- **FastAPI TestClient** - Tests de APIs
- **pytest-cov** - Cobertura de código
- **pytest-xdist** - Tests en paralelo

</div>

</div>

<v-click>

<div class="mt-8">

## Conceptos Clave
**Fixtures** • **Mocking** • **Parametrización** • **Marks** • **TDD**

</div>

</v-click>

---
layout: two-cols
---

# Nuestro Código de Ejemplo

Vamos a testear una calculadora simple

```python {*|1-3|5-7|9-11|*}
class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base: float, exponent: int) -> float:
        return base**exponent
```

::right::

<v-click>

## ¿Qué deberíamos testear?

</v-click>

<v-clicks>

- ✅ Suma de números positivos
- ✅ Suma de números negativos
- ✅ División normal
- ✅ División por cero (excepción)
- ✅ Potencias
- ✅ Casos edge (0, decimales)

</v-clicks>

---
zoom: 0.8
---

# unittest - La Base

Tests con la librería estándar de Python

```python {*|1-2|5-7|9-11|13-16|18-21|23-26|*}
import unittest
from src.testing_workshop.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Fixture: setup antes de cada test."""
        self.calc = Calculator()

    def tearDown(self):
        """Fixture: teardown después de cada test."""
        self.calc = None

    def test_add_positive_numbers(self):
        """Unit test: suma básica."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_divide_by_zero_raises_error(self):
        """Unit test: manejo de excepciones."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power_calculation(self):
        """Regression test: potencias funcionan."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
```

---

# unittest - Ejecutar Tests

Diferentes formas de ejecutar nuestros tests

<div class="grid grid-cols-2 gap-6">

<div>

## Desde el archivo
```bash
python test_calculator_unittest.py
```

## Con el módulo unittest
```bash
python -m unittest test_calculator_unittest
```

## Descubrimiento automático
```bash
python -m unittest discover
```

</div>

<div>

## Salida típica
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## Con más detalle
```bash
python -m unittest -v test_calculator_unittest
```

```
test_add_positive_numbers ... ok
test_divide_by_zero_raises_error ... ok  
test_power_calculation ... ok
```

</div>

</div>

---
zoom: 0.8
---

# pytest - Más Potente y Simple

El framework de testing más popular para Python

```python {*|1-2|4-9|11-14|11-17|19-22|24-28|*}
import pytest
from src.testing_workshop.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture: proporciona instancia de calculadora."""
    print("setup")
    yield Calculator()
    print("teardown")

@pytest.mark.parametrize(
    "a,b,expected", 
    [(2, 3, 5), (0, 0, 0), (-1, 1, 0), (10.5, 2.5, 13.0)]
)
def test_add_parameterized(calculator, a, b, expected):
    """Test parametrizado: múltiples casos."""
    assert calculator.add(a, b) == expected

def test_divide_by_zero(calculator):
    """Unit test: excepción con pytest."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)

@pytest.mark.smoke
def test_basic_operations_work(calculator):
    """Smoke test: funcionalidad básica."""
    assert calculator.add(1, 1) == 2
    assert calculator.divide(4, 2) == 2
```

---

# pytest - Ventajas sobre unittest

¿Por qué pytest es tan popular?

<div class="grid grid-cols-2 gap-6">

<div>

## Sintaxis más simple
```python
# unittest
self.assertEqual(result, expected)
self.assertRaises(ValueError)

# pytest  
assert result == expected
with pytest.raises(ValueError):
    # código
```

## Fixtures más potentes
```python
@pytest.fixture
def database():
    db = create_db()
    yield db  # setup
    db.close()  # teardown
```

</div>

<div>

## Parametrización fácil
```python
@pytest.mark.parametrize("input,expected", [
    (1, 2), (2, 4), (3, 6)
])
def test_double(input, expected):
    assert double(input) == expected
```

## Marks personalizados
```python
@pytest.mark.slow
@pytest.mark.integration  
@pytest.mark.skip(reason="WIP")
def test_something():
    pass
```

</div>

</div>

---
zoom: 0.9
---

# pytest - Ejecutar Tests

Comandos útiles para ejecutar tests con pytest

<div class="grid grid-cols-2 gap-6">

<div>

## Comandos básicos
```bash
# Todos los tests
pytest

# Un archivo específico
pytest test_calculator.py

# Un test específico
pytest test_calculator.py::test_add

# Con verbose
pytest -v
```

## Filtrar por marks
```bash
# Solo smoke tests
pytest -m smoke

# Excluir tests lentos
pytest -m "not slow"
```

</div>

<div>

## Opciones útiles
```bash
# Parar en el primer fallo
pytest -x

# Mostrar variables locales
pytest -l

# Ejecutar en paralelo
pytest -n 4

# Con cobertura
pytest --cov=src
```

## Configuración (pytest.ini)
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers = 
    smoke: quick smoke tests
    slow: slow running tests
```

</div>

</div>

---

# Fixtures - Setup y Teardown

Las fixtures nos ayudan a preparar el entorno para los tests

````md magic-move {lines: true}
```python {*|5-7}
# Fixture simple
import pytest

@pytest.fixture
def calculator():
    """Proporciona una calculadora limpia."""
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5
```

```python {*|5-9}
# Fixture con setup y teardown
import pytest

@pytest.fixture
def database():
    """Proporciona conexión a BD."""
    db = create_connection()
    yield db  # Aquí se ejecutan los tests
    db.close()  # Cleanup automático

def test_user_creation(database):
    user = create_user(database, "John")
    assert user.name == "John"
```

```python {*|5-6|8-12}
# Fixture con scope
import pytest

@pytest.fixture(scope="session")  # Una vez por sesión
def expensive_resource():
    return create_expensive_thing()

@pytest.fixture(scope="function")  # Por defecto
def clean_state():
    state = {}
    yield state
    state.clear()
```
````

---
zoom: 0.9
---

# Mocking - Simulando Dependencias

Cuando necesitamos simular partes del sistema

```python {*|1-2|4-7|9-14|17-24|*}
from unittest.mock import patch, Mock
import pytest

# Mock de una función externa
@patch("src.testing_workshop.api.user_service.get_user")
def test_user_endpoint_success(mock_get_user, client):
    mock_get_user.return_value = {"id": 1, "name": "John"}
    
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John"}
    
    # Verificar que se llamó correctamente
    mock_get_user.assert_called_once_with(1)

# Mock object
def test_with_mock_object():
    mock_service = Mock()
    mock_service.get_data.return_value = "test data"
    
    result = process_data(mock_service)
    
    assert result == "processed: test data"
    mock_service.get_data.assert_called_once()
```

---
zoom: 0.9
---

# Tests de APIs con FastAPI

Testing de endpoints HTTP con TestClient

```python {*|1-2|4-7|9-13|15-19}
from fastapi.testclient import TestClient
from src.testing_workshop.api import app

@pytest.fixture
def client():
    """Fixture: cliente de pruebas FastAPI."""
    return TestClient(app)

def test_root_endpoint(client):
    """Integration test: endpoint raíz."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Testing Workshop API"}

def test_calculator_endpoint(client):
    """Integration test: endpoint calculadora."""
    response = client.get("/calculate/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}
```

<v-click>

<div class="mt-4 p-4 bg-dark-50 rounded">
💡 <strong>TestClient</strong> simula requests HTTP sin necesidad de servidor real
</div>

</v-click>

---
zoom: 0.9
---

# Property-Based Testing con Hypothesis

Tests que verifican propiedades matemáticas

```python {*|1-2|4-8|10-17|19-24}
from hypothesis import given
from hypothesis import strategies as st

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_add_zero_identity(x):
    """Propiedad: sumar cero no cambia el valor."""
    calc = Calculator()
    assert calc.add(x, 0) == x

@given(
    st.floats(allow_nan=False, allow_infinity=False),
    st.floats(allow_nan=False, allow_infinity=False),
)
def test_add_commutative(a, b):
    """Propiedad: la suma es conmutativa."""
    calc = Calculator()
    assert calc.add(a, b) == calc.add(b, a)

@given(st.integers(min_value=1, max_value=100))
def test_power_positive(base):
    """Propiedad: potencias de números positivos."""
    calc = Calculator()
    result = calc.power(base, 2)
    assert result == base * base
```

---
zoom: 0.9
---

# Tests de Integración con Testcontainers

Testing con bases de datos reales usando Docker

```python {*|1-2|4-12|14-20}
import pytest
from testcontainers.postgres import PostgresContainer

@pytest.mark.integration
def test_database_connection():
    """Integration test con testcontainers: PostgreSQL."""
    with PostgresContainer("postgres:13") as postgres:
        # Obtener detalles de conexión
        connection_url = postgres.get_connection_url()
        
        assert connection_url.startswith("postgresql")
        assert postgres.get_exposed_port(5432) is not None

# Ejemplo más complejo con Redis
def test_redis_operations():
    """Test con Redis container."""
    with RedisContainer() as redis:
        client = redis.get_client()
        client.set("test_key", "test_value")
        assert client.get("test_key") == b"test_value"
```

<v-click>

<div class="mt-4 p-4 bg-dark-50 rounded">
🐳 <strong>Testcontainers</strong> levanta contenedores Docker automáticamente para tests
</div>

</v-click>

---

# Test-Driven Development (TDD)

El ciclo Red-Green-Refactor. Muy usado para investigar y solucionar bugs

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="text-center">
<div class="w-20 h-20 bg-red-500 rounded-full mx-auto mb-4 flex items-center justify-center text-white font-bold text-2xl">1</div>

## 🔴 Red


<v-click>
Escribe un test que falle

```python
def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
```

</v-click>

</div>

<div class="text-center">
<div class="w-20 h-20 bg-green-500 rounded-full mx-auto mb-4 flex items-center justify-center text-white font-bold text-2xl">2</div>

## 🟢 Green

<v-click>

Implementa el mínimo código para que el test pase (no tiene por qué estar correcto)

```python
def multiply(self, a, b):
    return int(a) * int(b)
```

</v-click>

</div>

<div class="text-center">
<div class="w-20 h-20 bg-blue-500 rounded-full mx-auto mb-4 flex items-center justify-center text-white font-bold text-2xl">3</div>

## 🔵 Refactor

<v-click>

Mejora el test, de manera que puedas coger más edge cases

```python
def test_multiply():
    calc = Calculator()
    real = calc.multiply(3.0, 4.0)

    assert isinstance(real, float)
    assert real == 12.0
```

</v-click>

</div>

</div>

---

# TDD en Acción

Ejemplo práctico: implementando una función paso a paso

````md magic-move {lines: true}
```python
# Paso 1: Test que falla
def test_string_reverser():
    reverser = StringProcessor()
    assert reverser.reverse("hello") == "olleh"

# Error: StringProcessor no existe
```

```python
# Paso 2: Implementación mínima
class StringProcessor:
    def reverse(self, text):
        return "olleh"  # Hardcoded para pasar el test

def test_string_reverser():
    reverser = StringProcessor()
    assert reverser.reverse("hello") == "olleh"  # ✅ Pasa
```

```python
# Paso 3: Más tests
def test_string_reverser():
    reverser = StringProcessor()
    assert reverser.reverse("hello") == "olleh"
    assert reverser.reverse("world") == "dlrow"  # ❌ Falla

class StringProcessor:
    def reverse(self, text):
        return "olleh"  # Ya no funciona para todos los casos
```

```python
# Paso 4: Implementación real
class StringProcessor:
    def reverse(self, text: str) -> str:
        return text[::-1]

def test_string_reverser():
    reverser = StringProcessor()
    assert reverser.reverse("hello") == "olleh"  # ✅
    assert reverser.reverse("world") == "dlrow"  # ✅
```
````

---

# Cobertura de Código

Midiendo qué tanto código testean nuestros tests

<div class="grid grid-cols-2 gap-6">

<div>

## Instalar pytest-cov
```bash
pip install pytest-cov
```

## Ejecutar con cobertura
```bash
# Cobertura básica
pytest --cov=src

# Con reporte HTML
pytest --cov=src --cov-report=html

# Solo mostrar líneas faltantes
pytest --cov=src --cov-report=term-missing
```

</div>

<div>

## Ejemplo de salida
```
Name                    Stmts   Miss  Cover
-------------------------------------------
src/calculator.py          10      2    80%
src/api.py                 15      5    67%
src/user_service.py         8      0   100%
-------------------------------------------
TOTAL                      33      7    79%
```

## Configuración en pytest.ini
```ini
[tool:pytest]
addopts = --cov=src --cov-report=term-missing
```

</div>

</div>

<v-click>

<div class="mt-4 p-4 bg-dark-50 rounded">
⚠️ <strong>Cuidado:</strong> 100% cobertura ≠ tests perfectos. Calidad > Cantidad
</div>

</v-click>

---
zoom: 0.9
---

# Mejores Prácticas

Consejos para escribir tests efectivos

<div class="grid grid-cols-2 gap-6">

<div>

## Estructura de Tests
- **AAA Pattern**: Arrange, Act, Assert
- **Nombres descriptivos**: `test_divide_by_zero_raises_error`
- **Un concepto por test**: No mezclar múltiples verificaciones
- **Tests independientes**: No dependencias entre tests

## Organización
```
tests/
├── unit/
├── integration/  
├── e2e/
└── conftest.py  # Fixtures compartidas
```

</div>

<div>

## Qué Testear
- ✅ Casos felices (happy path)
- ✅ Casos edge y límites
- ✅ Manejo de errores
- ✅ Lógica de negocio crítica
- ❌ Getters/setters simples
- ❌ Código de terceros

## Performance
- Tests rápidos (< 1s por test unitario)
- Usar mocks para dependencias externas
- Paralelización con `pytest-xdist`

</div>

</div>

---
zoom: 0.9
---

# Debugging Tests

Herramientas para debuggear tests que fallan

<div class="grid grid-cols-2 gap-6">

<div>

## Con pytest
```bash
# Mostrar prints
pytest -s

# Parar en primer fallo
pytest -x

# Mostrar variables locales
pytest -l --tb=long

# Modo verbose
pytest -vv
```

## Con ipdb
```python
import ipdb

def test_complex_logic():
    result = complex_function()
    ipdb.set_trace()  # Breakpoint
    assert result == expected
```

</div>

<div>

## Información útil
```python
# Capturar stdout/stderr
def test_with_output(capsys):
    print("Debug info")
    captured = capsys.readouterr()
    assert "Debug" in captured.out

# Archivos temporales
def test_file_processing(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    result = process_file(test_file)
    assert result == "processed"
```

</div>

</div>

---

# Configuración del Proyecto

Archivos de configuración importantes

<div class="grid grid-cols-2 gap-6">

<div>

## pytest.ini
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --cov=src
    --cov-report=term-missing
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests
```

</div>

<div>

## pyproject.toml
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = [
    "--cov=src",
    "--cov-report=html",
    "--cov-report=term-missing"
]

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError"
]
```

</div>

</div>

---

# Ejercicios Prácticos

¡Hora de practicar! 🚀

<div class="grid grid-cols-2 gap-6">

<div>

## Ejercicio 1: Tests Básicos
1. Clona el repositorio del taller
2. Ejecuta los tests existentes
3. Añade un test para el método `subtract`
4. Implementa el método para que pase

## Ejercicio 2: Fixtures
1. Crea una fixture para datos de prueba
2. Úsala en múltiples tests
3. Añade setup y teardown

</div>

<div>

## Ejercicio 3: Mocking
1. Crea un test que mockee una API externa
2. Verifica que se llama correctamente
3. Testea diferentes respuestas

## Ejercicio 4: Property Testing
1. Escribe un property test para una función matemática
2. Usa Hypothesis para generar casos de prueba
3. Encuentra edge cases automáticamente

</div>

</div>

<v-click>

<div class="mt-6 p-4 bg-dark-50 rounded text-center">
💻 <strong>Repositorio:</strong> Todos los ejemplos están en el código del taller
</div>

</v-click>

---
zoom: 0.75
---

# Comandos Útiles - Cheat Sheet

Referencia rápida para el día a día

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

## Ejecutar Tests
```bash
# Todos los tests
pytest

# Un archivo
pytest test_calculator.py

# Un test específico  
pytest test_calculator.py::test_add

# Por marca
pytest -m "unit"
pytest -m "not slow"

# Con cobertura
pytest --cov=src --cov-report=html
```

## Debugging
```bash
# Verbose
pytest -v

# Parar en fallo
pytest -x

# Mostrar prints
pytest -s

# Variables locales
pytest -l --tb=long
```

</div>

<div>

## Configuración
```bash
# Crear pytest.ini
echo "[tool:pytest]
testpaths = tests
addopts = --cov=src" > pytest.ini

# Instalar dependencias
pip install pytest pytest-cov hypothesis
pip install testcontainers fastapi
```

## Marks Útiles
```python
@pytest.mark.skip(reason="WIP")
@pytest.mark.skipif(sys.version < "3.8")
@pytest.mark.parametrize("a,b", [(1,2), (3,4)])
@pytest.mark.slow
@pytest.mark.integration
```

</div>

</div>

---
layout: center
class: text-center
---

# ¡Gracias!

## Recursos Adicionales

<div class="flex justify-center gap-8 mt-8">

<div class="text-left">

**Documentación:**
- [pytest.org](https://pytest.org)
- [hypothesis.readthedocs.io](https://hypothesis.readthedocs.io)
- [testcontainers-python.readthedocs.io](https://testcontainers-python.readthedocs.io)

</div>

<div class="text-left">

**Libros:**
- "Test-Driven Development with Python" - Harry Percival
- "Architecture Patterns with Python" - Harry Percival & Bob Gregory
- "Effective Python" - Brett Slatkin

</div>

</div>

<div class="mt-8">

### ¿Preguntas? 🤔

</div>

<div class="abs-br m-6 text-xl">
  <a href="https://github.com/slidevjs/slidev" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>
