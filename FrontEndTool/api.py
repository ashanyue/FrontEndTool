import re

from django.http import JsonResponse

from utils import json_response_format


def index(request):
    if request.method == "POST":
        key = request.POST.get('key')
        if key:
            keys = re.split(r'\.', key)
            from Guests import views as guest
            if len(keys) == 2:
                view_name = keys[0]
                view_method = keys[1]
                context = locals()
                if view_name in context.keys():
                    view = context[view_name]
                    if hasattr(view, view_method):
                        view_method = getattr(view, view_method)
                        try:
                            result = view_method()
                            JsonResponse(result, safe=False)
                        except:
                            # TODO 完善错误信息
                            return JsonResponse(
                                json_response_format(data=None, message="invoke api method error " + key, status=500))
                    else:
                        return JsonResponse(json_response_format(message='API not found', status=404),
                                            status=404)
                else:
                    return JsonResponse(json_response_format(message='API not found', status=404), status=404)
            else:
                return JsonResponse(json_response_format(message='API not found', status=404), status=404)
        else:
            return JsonResponse(json_response_format(message='API not found', status=404), status=404)

    else:
        return JsonResponse(json_response_format(message='Page not found', status=404), status=404)
