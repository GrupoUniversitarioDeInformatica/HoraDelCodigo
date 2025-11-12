# Guía del Taller de Testing en Python

## Configuración inicial

```bash
# Activar entorno virtual
uv sync

# Ejecutar todos los tests
uv run pytest

# Ejecutar tests específicos
uv run pytest tests/test_calculator_pytest.py
```

## Conceptos demostrados

### 1. Unit Tests
- `test_calculator_unittest.py` - Tests unitarios con unittest
- `test_calculator_pytest.py` - Tests unitarios con pytest

### 2. Fixtures
- `@pytest.fixture` en `test_calculator_pytest.py`
- `setUp()` en `test_calculator_unittest.py`

### 3. Parameterized Tests
- `@pytest.mark.parametrize` en `test_calculator_pytest.py`

### 4. Mocking
- `test_user_service.py` - Mock de requests HTTP

### 5. Property-based Testing
- `test_calculator_hypothesis.py` - Tests con Hypothesis

### 6. Integration Tests
- `test_api.py` - Tests de FastAPI
- `test_database.py` - Tests con testcontainers

### 7. Test Types
```bash
# Smoke tests
uv run pytest -m smoke

# Integration tests  
uv run pytest -m integration

# End-to-end tests
uv run pytest -m e2e
```

### 8. TDD Demonstration
- `test_tdd_example.py` - Tests escritos primero
- `string_processor.py` - Implementación después

## Comandos útiles

```bash
# Tests con coverage
uv run pytest --cov=src

# Tests en paralelo
uv run pytest -n auto

# Tests con output detallado
uv run pytest -v -s

# Ejecutar API para tests manuales
uv run uvicorn src.testing_workshop.api:app --reload
```

## Ejercicios para el taller

1. **TDD**: Implementar nuevos métodos en `StringProcessor` siguiendo TDD
2. **Mocking**: Añadir tests con mock para diferentes escenarios HTTP
3. **Parameterized**: Crear más casos de prueba parametrizados
4. **Property-based**: Escribir nuevas propiedades con Hypothesis
5. **Integration**: Añadir tests de integración con base de datos real
