from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'testapp/index.html')

def movies_views(request):
    head_msg = 'Movies Information'
    sub_msg1='RRR ready to release'
    sub_msg2 = 'Background support must be required to get chance'
    sub_msg3 = 'Indian cine industry is struggling like anything for covid'
    sub_msg4 = 'Biggest benefit of covid for industry: OTT'
    sub_msg5='Durga sir is here in upcoming Django movie'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'sub_msg4':sub_msg4, 'sub_msg5':sub_msg5}
    return render(request, 'testapp/demo.html', my_dict)

def sports_views(request):
    head_msg = 'Sports Information'
    sub_msg1='Now we have two Indian teams for international cricket'
    sub_msg2 = 'Srilanka blaming India for sending second grade team'
    sub_msg3 = 'Popolation is 130 crores but medals are very less'
    sub_msg4 = 'Sports sector should be improved like IT'
    sub_msg5='Very soon good days are coming for Indian team'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'sub_msg4':sub_msg4, 'sub_msg5':sub_msg5}
    return render(request, 'testapp/demo.html', my_dict)
