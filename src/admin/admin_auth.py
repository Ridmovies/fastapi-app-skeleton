from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.auth.jwt_utils import get_current_user, create_access_token
from src.auth.service import AuthService


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        """ login with session token """
        # TODO: add check password
        form = await request.form()
        username, password = form["username"], form["password"]

        user = await AuthService.get_user_by_username(username)
        if user:
            access_token = create_access_token({"sub": username})
            request.session.update({"token": access_token})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        user = await get_current_user(token)
        if not user:
            return False
        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="...")