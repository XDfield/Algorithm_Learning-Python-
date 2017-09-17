'''各种排序算法实现'''
import random
import time


def find_max_in_list(lists):
    '''求列表中的最大值'''
    max_e = 0
    for i in range(len(lists)):
        if lists[i] > max_e:
            max_e = lists[i]
    return max_e

class Sort:
    '''一个调用各排序算法的类'''
    def __init__(self):
        self.time = 0

    def BUB(self, arr=None, timing=False, pattern='<'):
        '''冒泡排序'''
        # 排序思想: 相邻两个数依次比对将最大的数往后"冒出"
        arr = list(arr)
        # 未排序的元素个数
        UnsortedElement = len(arr)
        if timing:
            start = time.time()
        while UnsortedElement:  # 若都排序好则退出
            for i in range(UnsortedElement-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            UnsortedElement -= 1
        if timing:
            self.time = time.time() - start
        return arr if pattern == '<' else arr[::-1]
    
    def SEL(self, arr=None, timing=False, pattern='<'):
        '''选择排序'''
        # 排序思想: 选出未排序的元素里最小的数放到前边已排序里
        arr = list(arr)
        # 第一个未排序的元素位置
        UnsortedE_i = 0
        if timing:
            start = time.time()
        # 重复(元素个数-1)次:
        for i in range(len(arr)-1):
            # 将第一个未排序的元素记录为最小值
            min_i = UnsortedE_i
            for j in range(UnsortedE_i+1, len(arr)):
                if arr[min_i] > arr[j]:
                    min_i = j 
            arr[UnsortedE_i], arr[min_i] = arr[min_i], arr[UnsortedE_i]
            UnsortedE_i += 1
        if timing:
            self.time = time.time() - start
        return arr if pattern == '<' else arr[::-1]
        
    def INS(self, arr=None, timing=False, pattern='<'):
        '''插入排序'''
        # 排序思想: 取出待排序的元素从左往右遍历插入刚好比对方大的位置
        arr = list(arr)
        # 设定最后一个已排序的元素位置
        LSortedElement = 0
        if timing:
            start = time.time()
        for i in range(len(arr)-1):
            # 待插入元素
            Extrect_e = arr[LSortedElement+1]
            for j in range(LSortedElement+1)[::-1]:
                if Extrect_e <= arr[j]:
                    # 移位
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                else:
                    # 插入(实际因为原先移位了相当于插入了)
                    break
            LSortedElement += 1
        if timing:
            self.time = time.time() - start
        return arr if pattern == '<' else arr[::-1]

    def MER(self, arr=None, timing=False, pattern='<'):
        '''归并排序'''
        # 排序思想: 想分后治.先拆散各自与相邻的比对再相邻得组合.多采用递归的思路.
        arr = list(arr)
        
        def merge(left, right):
            '''用于两个序列的有序合并'''
            i, j = 0, 0
            result = []
            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            # 若有一方尚有剩余则将剩余的都添加进去
            result += left[i:]
            result += right[j:]
            return result

        def merge_sort(lists):
            '''用于递归拆分'''
            # 若数组长度小于或等于1则不用细分了
            if len(lists) <= 1:
                return lists
            num = len(lists)//2
            # 数组拆分        
            left = merge_sort(lists[:num])
            right = merge_sort(lists[num:])
            # 数组合并
            return merge(left, right)

        if timing:
            start = time.time()
        result = merge_sort(arr)
        if timing:
            self.time = time.time() - start
        return result if pattern == '<' else result[::-1]

    def QUI(self, arr=None, timing=False, pattern='<', RQ=False):
        '''快速排序'''
        # 若RQ=True则为随机化快速排序
        # 排序思想: 取基准数将数组化为(比它小的数 基准数 比它大的数),再递归
        arr = list(arr)
        
        def quick(lists, left, right, RQ=False):
            '''快速排序主逻辑'''
            if left >= right:
                return lists
            # 基准点位置默认为最左端位置,随机化时随机抽取一个数与最左端互换
            if RQ:
                r = random.randint(left, right)
                lists[r], lists[left] = lists[left], lists[r]
            Base = left
            low = left
            high = right
            while left < right:
                while lists[right] >= lists[Base] and left < right:
                    right -= 1
                while lists[left] <= lists[Base] and left < right:
                    left += 1
                # 将左探测点遇到的比基准点小的数与右探测点遇到的比基准点大的数互换
                lists[left], lists[right] = lists[right], lists[left]
            # 左右探测点相遇后将基准点与相遇点互换
            lists[Base], lists[right] = lists[right], lists[Base]
            # 对基准点左右两边也进行排序
            quick(lists, low, right-1, RQ=RQ)
            quick(lists, right+1, high, RQ=RQ)
            return lists
        if timing:
            start = time.time()
        result = quick(arr, 0, len(arr)-1, RQ=RQ)
        if timing:
            self.time = time.time() - start
        return result if pattern == '<' else result[::-1]

    def COU(self, arr=None, timing=False, pattern='<'):
        '''计数排序'''
        # 排序思想: 统计各个数各出现多少次再输出
        arr = list(arr)
        if timing:
            start = time.time()
        # 找出数组里的最大值
        max_e = find_max_in_list(arr)
        # 初始化统计数组(长度为待排序数组里最大值+1)(因为还有个0)
        count_list = [0]*(max_e+1)
        for j in range(len(arr)):
            count_list[arr[j]] += 1
        
        result = []
        for k in range(len(count_list)):
            if count_list[k] == 0:
                continue
            for p in range(count_list[k]):
                result.append(k)
        if timing:
            self.time = time.time() - start
        return result if pattern == '<' else result[::-1]

    def RAD(self, arr=None, timing=False, pattern='<'):
        '''基数排序'''
        # 排序思想: 按各个数的数位排列入桶
        result = list(arr)
        if timing:
            start = time.time()
        # 先求出最大值的位数
        max_e = find_max_in_list(arr)
        k = 0
        while max_e > 0:
            k += 1
            max_e = max_e // 10
        # 构造十个桶序列(存放0~9)
        bucket = [[] for n in range(10)]
        # 遍历k(位数)次:
        for i in range(k):
            for j in range(len(result)):
                # 将数字转化为字符串来取对应位数的数字,取不到则为0
                c = str(result[j])[::-1]
                try:
                    num = int(c[i])
                except IndexError:
                    num = 0
                bucket[num].append(result[j])
            result = []
            for p in range(10):
                result += bucket[p]
            bucket = [[] for n in range(10)]
        if timing:
            self.time = time.time() - start
        return result if pattern == '<' else result[::-1]

def RandomList(start=0, stop=50, length=15):
    '''
    生成随机数组
    默认生成长度15,各元素为0~50的随机数
    '''
    if int(start) < int(stop):
        start, stop = int(start), int(stop)
    else:
        start, stop = int(stop), int(start)

    if length:
        length = int(length)

    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

if __name__ == "__main__":
    sort = Sort()
    # 待排序数组
    random_list = RandomList(length=30)
    # print('待排序数组:\t'+str(random_list)+'\n')

    answer = sorted(random_list)

    print('-'*5+'测试'+'-'*5)
    tasks = [sort.BUB, sort.SEL, sort.INS, sort.MER, sort.QUI, sort.RAD, sort.COU]
    for fn in tasks:
        sorted_list = fn(random_list)
        sorted_result = '通过' if sorted_list==answer else '未通过'
        print(fn.__doc__+': '+sorted_result)
