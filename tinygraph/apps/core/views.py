# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

from utils import get_details

def test(request):
    if request.method == 'POST':
        data = None
        error = None
        try:
            data = get_details(request.POST['host'], request.POST['community'])
            
            for index, store in data['storage'].items():
                store['sizeInBytes'] = int(store['hrStorageAllocationUnits']) * int(store['hrStorageSize'])
                store['usedInBytes'] = int(store['hrStorageAllocationUnits']) * int(store['hrStorageUsed'])
                if int(store['sizeInBytes']) > 0:
                    store['usage'] = (float(store['usedInBytes']) / float(store['sizeInBytes'])) * 100
                else:
                    store['usage'] = 0.0
        except Exception as e:
            error = e
        return render_to_response('core/test_result.html', {
            'data': data,
            'error': error,
            'host': request.POST['host'],
            'community': request.POST['community'],
        }, context_instance=RequestContext(request))
    else:
        return render_to_response('core/test.html', context_instance=RequestContext(request))