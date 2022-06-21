#view
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view





@api_view(['GET'])
def joblistapi(request):
    all_job = Job.objects.all()
    data = JobSerializer(all_job , many=True).data
    return  Response({'data':data})