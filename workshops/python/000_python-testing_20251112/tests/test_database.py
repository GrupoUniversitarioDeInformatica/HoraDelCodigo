"""Database tests using testcontainers."""

import pytest
from testcontainers.postgres import PostgresContainer


@pytest.mark.integration
def test_database_connection():
    """Integration test with testcontainers: PostgreSQL."""
    with PostgresContainer("postgres:13") as postgres:
        # Get connection details
        connection_url = postgres.get_connection_url()

        # Simple connection test (would normally use actual DB operations)
        assert connection_url.startswith("postgresql")
        assert postgres.get_exposed_port(5432) is not None


@pytest.mark.skip(reason="Docker required - demo only")
def test_redis_container():
    """Example of Redis container test (requires docker)."""
    # from testcontainers.redis import RedisContainer
    # with RedisContainer() as redis:
    #     redis_client = redis.get_client()
    #     redis_client.set("test", "value")
    #     assert redis_client.get("test") == b"value"
    pass
