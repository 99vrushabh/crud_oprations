from server.utils.database import Base, engine

def migrate_db():
    Base.metadata.create_all(engine)

