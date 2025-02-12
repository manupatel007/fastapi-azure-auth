from typing import Dict, Union

from demo_project.api.dependencies import multi_auth
from demo_project.schemas.hello_world import TokenType
from fastapi import APIRouter, Depends, Request

from fastapi_azure_auth.user import User

router = APIRouter()


@router.get(
    '/hello-multi-auth',
    response_model=TokenType,
    summary='Say hello with an API key',
    name='hello_world_api_key',
    operation_id='helloWorldApiKey',
)
async def world(request: Request, auth: Union[str, User] = Depends(multi_auth)) -> Dict[str, bool]:
    """
    Wonder how this auth is done?
    """
    if isinstance(auth, str):
        # An API key was used
        return {'api_key': True, 'azure_auth': False}
    return {'api_key': False, 'azure_auth': True}
