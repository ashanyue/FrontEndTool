from django.db import models
from utils.models import BaseModel


class Bank(BaseModel):
    class Meta:
        db_table = 'sys_bank'

    bankName = models.CharField('银行名称', max_length=32)
    bankCode = models.CharField('银行代码', max_length=32)
    isBan = models.BooleanField('是否禁用', default=False)
    isMaintenance = models.BooleanField('是否禁用', default=False)
