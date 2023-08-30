from flaskr import create_app
from flaskr.vistas.vistas import VistaAlbumsUsuario, VistaCancionesAlbum, VistaLogIn, VistaSignIn
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema, UsuarioSchema, CancionSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion, VistaAlbum, VistaAlbumsUsuario, VistaCancionesAlbum, VistaLogIn, VistaSignIn
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

# Inicializacion del api
api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')

jwt = JWTManager(app)

# Prueba
with app.app_context():
    album_schema = AlbumSchema()
    # usuario_schema = UsuarioSchema()
    # cancion_schema = CancionSchema()

    # c = Cancion(titulo='Cancion_prueba', minutos=2,
    #             segundos=25, interprete="Said Nader")
    # a = Album(titulo="Album_prueba", anio=2015,
    #           descripcion='album_prueba', medio=Medio.DISCO)
    # u = Usuario(nombre='said', contrasena="123")
    # u.albumes.append(a)
    # a.canciones.append(c)
    # db.session.add(u)
    # db.session.add(c)
    # db.session.commit()

    # print([album_schema.dumps(album) for album in Album.query.all()])
    # print([cancion_schema.dumps(cancion) for cancion in Cancion.query.all()])
    # print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])

    # print(Usuario.query.all())
    # print(Album.query.all())
    # print(Album.query.all()[0].canciones)
    # print(Cancion.query.all())
    # print(Usuario.query.all()[0].albumes)
    # db.session.delete(u)
    # db.session.delete(a)
    # print(Usuario.query.all())
    # print(Album.query.all())
    # print(Cancion.query.all())
