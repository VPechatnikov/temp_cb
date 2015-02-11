import json
from django.http import HttpResponse
from increasing.models import PageStats

def increasing_pages(request):
    try:
        if request.method == 'POST':
            request_body = json.loads(request.read())
            host_url = request_body.get('host')
        elif request.method == 'GET':
            host_url = request.GET.get('host')
        else:
            return jsonErrorResponse('Http method {} not supported.'.format(request.method))
        
        if host_url:
            pages_result = get_increasing_concurrents_pages(host_url)
            return jsonSuccessResponse(pages_result)
        else:
            return jsonErrorResponse("Missing required request param 'host'")
    except Exception:
        return jsonErrorResponse()


def jsonErrorResponse(error_message=None):
    return HttpResponse(json.dumps({'errorMessage': error_message or 'Unexpected error'}),
                        content_type='application/json',
                        status=400)

def jsonSuccessResponse(response=None):
    return HttpResponse(json.dumps(response),content_type='application/json',status=200)


def get_increasing_concurrents_pages(host):
    increasing_page_stats = PageStats.objects.filter(host=host, increasing=True)
    pg_data = [{"i":ps.page_path, "change":ps.last_speed} for ps in increasing_page_stats]
    return pg_data

