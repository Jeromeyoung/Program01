# coding=gbk
import json

# 1.��JSON�ַ���ת��ΪPYTHON����
# 1.1׼��json�ַ���
json_str = '''[{"provinceName":"����","cityName":"","currentConfirmedCount":3424215,"confirmedCount":5494239},
 {"provinceName":"Ӣ��","cityName":"","currentConfirmedCount":279163,"confirmedCount":321098}]'''
# 1.2ת��
rs = json.loads(json_str)
# print(rs)
# print(type(rs))
# print(type(rs[0]))

# 2.��JOSN��ʽ�ļ�ת��ΪPYTHON���͵�����
# 2.1����ָ����ļ��Ķ���
with open('data/test.json', encoding='utf8') as fp:   #�ҵĵ�������Ҫ����encoding='utf8'��,��Ȼ������.
    # 2.2���ظ��ļ�����ת��
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    print(type(python_list[0]))