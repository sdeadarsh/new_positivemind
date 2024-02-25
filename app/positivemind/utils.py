from rest_framework.response import Response


def error_response(message):
    return Response(
        {

            "data": {},
            "message": message,
            "error": True}

    )


def successful_response(data):
    return Response(
        {
            'result': {
                "data": data,
                "message": "success",
                "error": False}
        }
    )
