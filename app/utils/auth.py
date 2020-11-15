from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    AuthCredentials,
    SimpleUser
)
import base64
import binascii

from fastapi import HTTPException

from utils.secret import Secret


class KeyAuth(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            raise HTTPException(status_code=404, detail="Endpoint not found")

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "bearer":
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError("Error in decoding credentials")

        username, _, token = decoded.partition(":")
        if await self._check_token(token):
            return AuthCredentials(["authenticated"]), SimpleUser(username)
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

    async def _check_token(self, token: str):
        if token == Secret.api_key:
            return True
        else:
            return False

# @TODO When a user is denied, return a message stating so vs raising an
# exception
