from .controllers.user import( 
    UsersApi, UserRegister, 
    UserLogin, ProtectedApi
)

def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserRegister, '/api/register')
    api.add_resource(UserLogin, '/api/login')
    api.add_resource(ProtectedApi, '/api/protected')
    