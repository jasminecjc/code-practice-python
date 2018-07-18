# -*- coding: utf-8 -*-

import qrcode
import base64

# 生成二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6,
    border=4,
)

# 加密二维码的源码
base64_str = ('{加密方式}:{pwd}@{ip_address}:{server_port}').encode(
    encoding="utf-8")
encodestr = base64.b64encode(base64_str)  # 使用base64加密
shareqrcode_str = 'ss://' + encodestr.decode()  # 最前面加上`ss://`

filename = 'ssqrcode.png'  # 导出的图片名字

# 导出二维码
qr.add_data(shareqrcode_str)
qr.make(fit=True)
img = qr.make_image()
img.save(filename)
