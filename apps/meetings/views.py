from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.meetings.models import Meeting
from apps.meetings.serializers import MeetingSerializer

class MeetingListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def meetings_list(request):
        meetings = Meeting.objects.all()
        return render(request, 'meetings/meetings_list.html', {'meetings': meetings})    

    def get(self, request, *args, **kwargs):
        #meetings = Meeting.objects.filter(user = request.user.id)        
        meetings = Meeting.objects.all()      
        serializers = MeetingSerializer(meetings, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):        
        data = {            
            #'id': request.data.get('id'), 
            #'author': request.user.id,
            'author': request.data.get('author'), 
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'datetime': request.data.get('datetime'), 
            'duration': request.data.get('duration'), 
            'status': request.data.get('status'), 
            'contacts': request.data.get('contacts')
        }
        serializers = MeetingSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 