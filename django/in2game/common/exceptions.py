from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def in2game_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        print(response)
        response.data["error_code"] = response.status_code

    return response
