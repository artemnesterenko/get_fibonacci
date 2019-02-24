from drf_yasg.openapi import (
    Response as SchemaResponse,
    Schema,
    TYPE_INTEGER,
    TYPE_ARRAY,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from get_fibonacci.fibonacci import fibonacci
from get_fibonacci.serializers import SliceSerializer


class FibonacciView(APIView):
    """
    get: Return a list of fibonacci numbers
    """

    responses = {
        200: SchemaResponse(
            "Successful request",
            Schema(type=TYPE_ARRAY, items=Schema(type=TYPE_INTEGER)),
        ),
        400: SchemaResponse("Invalid request"),
    }

    @swagger_auto_schema(query_serializer=SliceSerializer, responses=responses)
    def get(self, request):
        serializer = SliceSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        start = data["from"]
        end = data["to"]
        fibonacci_list = [fibonacci(n) for n in range(start, end)]
        return Response(fibonacci_list)
