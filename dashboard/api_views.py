from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import YieldRecord

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def push_yield(request):

    line_id = request.data.get('line_id')
    output = request.data.get('output')

    YieldRecord.objects.create(
        production_line_id=line_id,
        yield_percentage=output   # 🔥 FIXED FIELD NAME
    )

    return Response({"message": "Yield recorded"})
