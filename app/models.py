from config import db

#Defino el modelo de la tabla de Usuario
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column("is_active", db.Boolean(), nullable=False, server_default="1")
    email = db.Column(db.String(255, collation="NOCASE"))
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default="")
    # User information
    first_name = db.Column(db.String(100, collation="NOCASE"))
    last_name = db.Column(db.String(100, collation="NOCASE"))
    username = db.Column(db.String(100))
    # Define the relationship to Role via UserRoles
    roles = db.relationship("Role", secondary="user_roles")
    nro_socio = db.Column(db.String(10))
    ya_voto = db.Column(db.String(2))


# Defino el modelo de la tabla de Rol
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# DEfino la relacion entre Usuario y Rol
class UserRoles(db.Model):
    __tablename__ = "user_roles"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="CASCADE"))
    role_id = db.Column(db.Integer(), db.ForeignKey("roles.id", ondelete="CASCADE"))

#Defino el modelo de la tabla del Padron
class Padron(db.Model):
    __tablename__ = "Padron"
    id = db.Column(db.Integer(), primary_key = True)
    nro_socio = db.Column(db.String(50), unique=True) 

#Defino el modelo de la tabla listas
class Listas(db.Model):
    __tablename__ = "Listas"
    id = db.Column(db.Integer(), primary_key = True)
    nro_lista = db.Column(db.String(50), unique=True)
    presidente = db.Column(db.String(50))
    vice_presidente = db.Column(db.String(50))

#Defino el modelo de la tabla votos
class Votos(db.Model):
    __tablename__ = "Votos"
    id = db.Column(db.Integer(), primary_key = True)
    lista_id = db.Column(db.Integer(), db.ForeignKey("Listas.id", ondelete="CASCADE"))