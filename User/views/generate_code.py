from utils import verification_code
from io import BytesIO
from django.shortcuts import HttpResponse
def generate_code(request):
    """生成图片验证码"""
    img, code_string = verification_code.check_code()
    # print(code_string)
    stream = BytesIO()
    request.session['code'] = code_string
    # 给Session设置60s超时
    #request.session.set_expiry(60)
    img.save(stream, 'png')
    print(img, code_string)
    stream.getvalue()
    return HttpResponse(stream.getvalue())