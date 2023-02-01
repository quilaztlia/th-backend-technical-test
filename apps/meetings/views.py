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

    def post(self, request, *args, **kwargs):        
        data = {            
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
        
        
class MeetingDetailApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get_object(self, meeting_id, user_id):
        try:
            return Meeting.objects.get(id=meeting_id)           
        except Meeting.DoesNotExist:
            return None 
        
    def get(self, request, meeting_id, *args, **kwargs):
        meeting = self.get_object(meeting_id, request.user.id) 
        if not meeting:
            return Response({"res": "This meeting does not exists"},   status=status.HTTP_400_BAD_REQUEST)       
        
        serializers = MeetingSerializer(meeting, many=False)
        return Response(serializers.data, status=status.HTTP_200_OK)    

    def put(self, request, meeting_id, *args, **kwargs):
        meeting = self.get_object(meeting_id, request.user.id)
        if not meeting:
            return Response({"res": "This meeting does not exists"},   status=status.HTTP_400_BAD_REQUEST)       
        
        data = {       
            'author': request.data.get('author'), 
            'title': request.data.get('title'),
            'description': request.data.get('description'), 
            'datetime': request.data.get('datetime'), 
            'duration': request.data.get('duration'), 
            'status': request.data.get('status'), 
            'contacts': request.data.get('contacts')
        }   
        serializers = MeetingSerializer(instance=meeting, data=data, partial=True)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)

        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, meeting_id, *args, **kwargs):
        meeting = self.get_object(meeting_id, request.user.id)
        if not meeting:
            return Response({"res": "This meeting does not exists"},   status=status.HTTP_400_BAD_REQUEST)       
        
        meeting.delete()
        return Response(status=status.HTTP_200_OK)
        
