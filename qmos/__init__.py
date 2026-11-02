"""QMOS — Qurilish Monitoringi Ochiq Standarti, Python kutubxonasi.

    from qmos import hodisa_xatolari, sign_request, imzoni_tekshir

Yuboruvchi tizim (masalan BuildOps) hodisani yuborishdan OLDIN
`hodisa_xatolari()` bilan tekshiradi; markaz qabul qilganda ham AYNAN
shu funksiyani chaqiradi.
"""
from .imzo import imzoni_tekshir, imzola, sign_request
from .tekshiruv import hodisa_xatolari, mazmun_xatolari, sxema_xatolari, sxemalar, tekshir, validator

SPEC_VERSION = '1.1'
# Markaz qabul qiladigan kichik versiyalar (1.x ichida faqat qo'shimchalar: eski yuboruvchilar buzilmaydi).
SPEC_VERSIONS = ('1.0', '1.1')

# Kunlik hisobot oilasi: bu turlar `supersedes` orqali bir-birini almashtira oladi (1.1).
KUNLIK_HISOBOT_OILASI = ('site.daily_report', 'site.daily_report_retracted')

__all__ = [
    'SPEC_VERSION', 'SPEC_VERSIONS', 'KUNLIK_HISOBOT_OILASI',
    'hodisa_xatolari', 'mazmun_xatolari', 'sxema_xatolari', 'sxemalar', 'tekshir', 'validator',
    'imzola', 'imzoni_tekshir', 'sign_request',
]
