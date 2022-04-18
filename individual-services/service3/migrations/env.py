import sys
from logging.config import fileConfig
from os.path import dirname, realpath

from alembic import context
from sqlalchemy import create_engine

# this is a trick to bypass "No module named 'app'"
# this is equal to `export PYTHONPATH=.`
base_dir = dirname(dirname(realpath(__file__)))
sys.path.append(base_dir)
from app import settings
from app.database.orm import Base  # noqa: E402
from app.models import *  # noqa: F401,E402,F403 (autogenerate)


def get_uri():
    return settings.config.DB_CONNECTION_STRING


config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=get_uri(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(get_uri())

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
