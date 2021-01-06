from django.db import models

# Create your models here.
# table 구조 생성 : 컬럼명, 자료형(정수,문자열...)
# table이라는 하나의 객체 생성
# table 자료 삭제,추가, 검색 하는 기능들이 장고에서는 이미 구현되어 있음. 가져다 쓰는 것을 "상속"이라함.
# models.Model = 부모 클래스 

#테이블명 수정시 admin.py/models.py 수정필요 TableName 
class Order(models.Model):
    # 컬럼명 = 자료형
    field_name1 = models.IntegerField()                 #int(32bit) 형 필드 
    field_name2 = models.BigIntegerField()              #int(64bit) 필드
    field_name3 = models.DecimalField(                 #고정 소수점 필드
        max_digits=5,                                  #(max_digits이라는 속성) , 최대 자릿수
        decimal_places=2                               #(DicimalField에서는 이 두가지 속성은 반드시 필요), 소수점 자릿수 
    )
    field_name4 = models.FloatField()                   #부동 소수점 필드                    
    field_name5 = models.BooleanField()                 # 불린 필드(True, False)
    field_name6 = models.CharField(                     #문자열 필드
        max_length=30                                   #30자리까지 저장.최대 자릿수
    )
