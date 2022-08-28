# -*- encoding: cp936-*-
'''
 check 
'''
#from auto.check import AssertEqual
from exception import AutoException
#import share

class CheckException(AutoException):

    '''
    @param msg:�쳣��Ϣ
    @type msg: str  
	
    @note: [example] \n
        raise CheckException("Exception by xavier")\n
    '''
    def __init__(self,msg):
#        share.g_oTestLog.debug(msg)
        super(CheckException, self ).__init__("%s"%(msg))

def AssertStrListContains_x_times(listStrs, strKey, count=1):

    '''
    @param listStrs:��Ҫ�Ƚϵ��ַ����б�
    @type listStrs:list
    @param strKey:��׼�ַ���
    @type strKey:str	
    @param count:��������
    @type count:int
	
    @note: [example] �ж�һ���б��е��ַ���Ԫ���Ƿ����(in)��count��ĳ���ַ���\n
        lst = ['1233','2343','3435']
        AssertStrListContainsN(lst, '3', 2)     
    '''
    if type(strKey) == type(unicode("")):
        strKey = str(strKey)
    intCount = int(count)
    #print count
    for each in listStrs:
        if type(each) == type(strKey) and type(strKey) == type('str'):
            real_count = each.count(strKey)
            if real_count == intCount:
                continue;
            else:
                raise CheckException("item1 contain item2 %d times, not %d times"% (real_count,intCount));
        else:
            raise CheckException("type %s and type %s should be str" % (type(each), type(strKey)));    
    

def AssertNoNullItem(listObjs):
    '''
    @param listRe:�Ƚ϶���
    @type listRe: list

    @note: �ж�listRe���Ƿ�ÿ��Ԫ�ض���Ϊ�ա������itemΪ�գ��׳��쳣��
    '''

    if len(listObjs) == 0:
        raise CheckException("input list is null!");

    i = 0
    for item in listObjs:
        i+=1
        if item == "" or type(item) == type(None) or len(item) == 0: 
            raise CheckException("the %dth item in list is null!"%(i));            


def AssertEqual2String(s1,s2,msg=''):

    '''
    @param s1:�Ƚ϶���1      
    @type s1: str,int,bool,list,tuple  
    @param s2:�Ƚ϶���2  
    @type s2: str,int,bool,list,tuple    
    @param msg:����������ʱ�Ĵ�����Ϣ
    @type msg: str                     

    @note: [example] �ж�s1��s2ת��Ϊ�ַ������Ƿ����\n
        AssertEqual2String("�ʻ�","�ʻ�","ǰ�������ַ���Ӧ�����"); \n
        AssertEqual2String(1,1,"ǰ����������Ӧ�����"); \n            
    ''' 

    str1,str2 = str(s1),str(s2)
#    AssertEqual(str1,str2,msg)
    if str1 != str2:
        raise CheckException("%s is not equal to %s" % (str1,str2))
		
def AssertFileContains(strFileName,strKey):

    '''
    @param strFileName:�ļ���
    @type strFileName:str
    @param strKey:�ؼ���
    @type strKey:str	
	
    @note: [example] �ж�һ���������ļ����Ƿ���ĳ���ؼ���\n
        AssertFileContains("./123","123")\n        
    '''
	
    ret = False
    strFileName = str(strFileName)
    #print strFileName
    fp = open(strFileName)
    try:         
        for line in fp:
            if strKey.strip() in line.strip():
                ret = True
    finally:
        fp.close()
		
    if not ret:
        raise CheckException("%s can not found in file %s" % (strKey,strFileName)) 
		
    return ret
	
def AssertFileNotContains(strFileName,strKey):

    '''
    @param strFileName:�ļ���
    @type strFileName:str
    @param strKey:�ؼ���
    @type strKey:str	
	
    @note: [example] �ж�һ���������ļ����Ƿ񲻺���ĳ���ؼ���\n
        AssertFileContains("./123","123")\n        
    '''
	
    ret = True
    strFileName = str(strFileName)
    #print strFileName
    fp = open(strFileName)
    try:         
        for line in fp:
            if strKey.strip() in line.strip():
                ret = False
    finally:
        fp.close()
		
    if not ret:
        raise CheckException("%s found in file %s" % (strKey,strFileName)) 
		
    return ret

def _CheckSameType(obj1, obj2):
    '''
    ������������Ƿ����ͼ���.
    '''
    typeInt = (type(int("1")),type(long("1")))
    typeStr = (type(str("1")),type(unicode("1")))
    type1 = type(obj1)
    type2 = type(obj2)
    if type1 == type2:
        return True
    elif type1 in typeInt and type2 in typeInt:
        return True
    elif type1 in typeStr and type2 in typeStr:
        return True
    return False

def AssertListSort(listObjs, mode = "ge"):
    '''
    @param listObjs:��Ҫ�Ƚϵ��б�
    @type listObjs:list
    @param mode:�Ƚ�ģʽ
    @type mode:str,'lt''gt''le''ge'
	
    @note: [example] �ж�һ���б��е�����Ԫ���Ƿ�����mode�������������.\n
        lst = ['1','1','1']\n
        AssertListEqual(lst, 'ge')\n
    '''
    size = len(listObjs)
    if size <= 0:
        return
    objKey = listObjs[0]
    for i in range(1,size):
        objCurr = listObjs[i]
        bSame = _CheckSameType(objKey,objCurr)
        if not bSame:
            raise CheckException("type %s is not same as type %s" % (type(objKey), type(objCurr)));
           
    mode = str(mode)
    #print  mode,type(mode)
    if mode == 'lt':
        for i in range(1,size):
            prev = listObjs[i-1]
            curr = listObjs[i]
            if not prev < curr:
                raise CheckException("not (%s  %s %s)" % (str(prev), mode, str(curr)));
    elif mode == "le":
        for i in range(1,size):
            prev = listObjs[i-1]
            curr = listObjs[i]
            if not prev <= curr:
                raise CheckException("not (%s  %s %s)" % (str(prev), mode, str(curr)));
    elif mode == "gt":
        for i in range(1,size):
            prev = listObjs[i-1]
            curr = listObjs[i]
            if not prev > curr:
                raise CheckException("not (%s  %s %s)" % (str(prev), mode, str(curr)));
    elif mode == "ge":
        for i in range(1,size):
            prev = listObjs[i-1]
            curr = listObjs[i]
            if not prev >= curr:
                raise CheckException("not (%s  %s %s)" % (str(prev), mode, str(curr)));
    else:
        raise CheckException("not support sort type (%s)"%(mode))


def AssertList_or_Equal(listObjs, objKey1, objKey2, mode='eq'):
    '''
    add @20110718
    @param listObjs:��Ҫ�Ƚϵ��б�
    @type listObjs:list
    @param objKey1,objKey2:��׼����
    @type objKey:str,int	
    @param mode:�Ƚ�ģʽ
    @type mode:str,'eq' 'lt''gt''le''ge' 
	
    @note: [example] �ж�һ���б��е�����Ԫ���Ƿ���objKey1 or objKey2 ��������mode\n
        lst = ['1','1','1']
        AssertListEqual(lst, '2', 'lt')     
    '''
    if len(listObjs) == 0:
        raise CheckException("input list in null!");
    for each in listObjs:
        bSame1 = _CheckSameType(each,objKey1)
        bSame2 = _CheckSameType(each,objKey2) 
        if not bSame1:
            raise CheckException("type %s is not same as type %s" % (type(each), type(objKey1)));
        if not bSame2:
           raise CheckException("type %s is not same as type %s" % (type(each), type(objKey2)));
           
    mode = str(mode)
    #print  mode,type(mode)
    if(mode=='eq'):
        for each in listObjs:
            if each == objKey1 or each == objKey2:
                continue;
            else:
                raise CheckException("%s is not %s %s or %s" % (each, mode, objKey1,objKey2));
    
    if mode == 'lt':
        for each in listObjs:
            if each < objKey1 or each < objKey2:
                continue;
            else:
                raise CheckException("%s is not %s %s or %s" % (each, mode, objKeyi1, objKey2));
                
    if(mode=='gt'):
        for each in listObjs:
            if each > objKey1 or each > objKey2:
                continue;
            else:
                raise CheckException("%s is not %s %s or %s" % (each, mode, objKey1, objKey2));
                
    if(mode=='le'):
        for each in listObjs:
            if each <= objKey1 or each <= objKey2:
                continue;
            else:
                raise CheckException("%s is not %s %s or %s" % (each, mode, objKey1, objKey2));

    if(mode=='ge'):
        for each in listObjs or each >= objKey2:
            if each >= objKey:
                continue;
            else:
                raise CheckException("%s is not %s %s or %s" % (each, mode, objKey1,objKey2));

   
def AssertListEqual(listObjs, objKey, mode='eq'):
    '''
    @param listObjs:��Ҫ�Ƚϵ��б�
    @type listObjs:list
    @param objKey:��׼����
    @type objKey:str,int	
    @param mode:�Ƚ�ģʽ
    @type mode:str,'eq''lt''gt''le''ge'
	
    @note: [example] �ж�һ���б��е�����Ԫ���Ƿ���ĳ����������mode\n
        lst = ['1','1','1']
        AssertListEqual(lst, '2', 'lt')     
    '''
    if len(listObjs) == 0:
        raise CheckException("input list in null!");
    for each in listObjs:
        bSame = _CheckSameType(each,objKey)
        if not bSame:
            raise CheckException("type %s is not same as type %s" % (type(each), type(objKey)));
           
    mode = str(mode)
    #print  mode,type(mode)
    if(mode=='eq'):
        for each in listObjs:
            if each == objKey:
                continue;
            else:
                raise CheckException("%s is not %s %s" % (each, mode, objKey));
    
    if mode == 'lt':
        for each in listObjs:
            if each < objKey:
                continue;
            else:
                raise CheckException("%s is not %s %s" % (each, mode, objKey));
                
    if(mode=='gt'):
        for each in listObjs:
            if each > objKey:
                continue;
            else:
                raise CheckException("%s is not %s %s" % (each, mode, objKey));
                
    if(mode=='le'):
        for each in listObjs:
            if each <= objKey:
                continue;
            else:
                raise CheckException("%s is not %s %s" % (each, mode, objKey));

    if(mode=='ge'):
        for each in listObjs:
            if each >= objKey:
                continue;
            else:
                raise CheckException("%s is not %s %s" % (each, mode, objKey));

def _AssertTypeString(strKey):
    listTypeString = (type(str("")),type(unicode("")))
    if type(strKey) not in listTypeString:
        raise CheckException("[%s] not String,type is (%s)"%(strKey,type(strKey)))
def AssertListEqual2List(list_1,list_2):
    '''
    '''
    if len(list_1) != len(list_2):
        raise CheckException("list_1 not equal to list_2!")
    i = 0
    for item_1 in list_1:
        item_2 = list_2[i]
        if item_1 != item_2:
            raise CheckException("list_1 not equal to list_2, in item %d !"%i)
        i += 1
        
        
def AssertStrListEqual(listStrs, strKey, mode='in'):

    '''
    @param listStrs:��Ҫ�Ƚϵ��ַ����б�
    @type listStrs:list
    @param strKey:��׼�ַ���
    @type strKey:str	
    @param mode:�Ƚ�ģʽ
    @type mode:str,'in''eq''pre''post'
	
    @note: [example] �ж�һ���б��е��ַ���Ԫ���Ƿ���ĳ���ַ�������mode\n
        lst = ['123','234','345']
        AssertStrListEqual(lst, '3')     
    '''
    if len(listStrs) == 0:
        raise CheckException("input list in null!");

    if type(strKey) == type(unicode("")):
        strKey = str(strKey)
    mode = str(mode)
    #print mode
    if(mode=='in'):
        for each in listStrs:
#            _AssertTypeString(each)
#            _AssertTypeString(strKey)
#            if strKey in each:
#                continue;
#            else:
#                raise CheckException("%s is not %s %s" % (each, mode, strKey));

            if type(each) == type(strKey) and type(strKey) == type('str'):
                if strKey in each:
                    continue;
                else:
                    raise CheckException("%s is not %s %s" % (strKey, mode, each));
            else:
                raise CheckException("type %s and type %s should be str" % (type(each), type(strKey)));    
    

    if(mode=='eq'):
        for each in listStrs:
            if type(each) == type(strKey) and type(strKey) == type('str'):
                if each == strKey:
                    continue;
                else:
                    raise CheckException("%s is not %s %s" % (each, mode, strKey));
            else:
                raise CheckException("type %s and type %s should be str" % (type(each), type(strKey)));

    if(mode=='pre'):
        for each in listStrs:
            if type(each) == type(strKey) and type(strKey) == type('str'):
                if each.startswith(strKey):
                    continue;
                else:
                    raise CheckException("%s is not %s %s" % (each, mode, strKey));
            else:
                raise CheckException("type %s and type %s should be str" % (type(each), type(strKey)));

    if(mode=='post'):
        for each in listStrs:
            if type(each) == type(strKey) and type(strKey) == type('str'):
                if each.endswith(strKey):
                    continue;
                else:
                    raise CheckException("%s is not %s %s" % (each, mode, strKey));
            else:
                raise CheckException("type %s and type %s should be str" % (type(each), type(strKey)));
if __name__ == "__main__":
	print _CheckSameType(int("1"),long("1"))
	print _CheckSameType(int("1"),str("1"))
	print _CheckSameType(unicode("1"),str("1"))
