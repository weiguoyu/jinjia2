# -*- coding: utf-8 -*-

import ujson
from flask import Response


def to_resp(data, code=200):
    """将一条数据处理成Response。

    Args:
        data: 要处理的数据。
        code: 状态码

    Returns:
        object: Http Response。
    """
    message = {
        'code': code,
        'result': data
    }
    return Response(ujson.dumps(message))


def error_resp(msg, code, is_status_code=False):
    """生成错误响应。

    Args:
        msg (string): 错误信息。
        code (int): 错误码。

    Returns:
        响应对象。
    """
    message = {
        'code': code,
        'msg': msg
    }
    resp = Response(ujson.dumps(message, ensure_ascii=False))
    if is_status_code:
        resp.status_code = code
    else:
        resp.status_code = 500
    return resp







