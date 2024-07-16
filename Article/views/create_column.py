from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core import serializers
from ..models import ArticleColumn
import json

@csrf_exempt
@require_http_methods(["POST"])
def create_column(request):
    try:
        data = json.loads(request.body)
        title = data.get('title')
        if not title:
            return JsonResponse({'error': '缺少标题'}, status=400)
        #字典的get方法从data中获取title键的值。如果data中没有title键，那么get方法将返回默认值"其他"。
        new_column = ArticleColumn.objects.create(title=title)
        new_column.save()
        response_data = serializers.serialize('json', [new_column])
        return JsonResponse(response_data, safe=False, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)