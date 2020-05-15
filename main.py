'''
README:
本程序用于创建一系列的「索引文件夹」，
其相当于一个索引矩阵（可能是「张量」），其包含的值（本质上是集合，但一般是文件）使用一个特定的序列（等价于一个向量）进行访问；
原理/作用/用途：通过增大其他用户逐一检索文件夹之难度以「隐藏」部分文件夹或文件

待补
'''

import os

#此函数来源于网络
def mkdir(path):
    # 引入模块
    import os
 
    # 去除首尾空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+'目录已存在')
        return False

#此函数用于按字符批量生成文件夹，根目录末尾可以不带「/」
#示例：path='C:\dir\',nums='gbv^4%faw1'
def makeDirsByChar(path,chars):
    root=path.strip().rstrip("\\")
    for i in chars:
        mkdir(root+'\\'+str(i))

#此函数用于按照整数序列生成n个文件夹
#示例：path='C:\',num=9
def makeDirVector(path,num):
    root=path.strip().rstrip("\\")
    for i in range(num):
        mkdir(root+'\\'+str(i))

#此函数用于按照0~9的整数序列生成文件夹「张量」，使用递归以支持任意长度（多起来仍然很恐怖，建议少于5层）
#示例：path='C:\',nums='1321'
def makeDirTenser(path,nums):
    root=path.strip().rstrip("\\")
    #print("正在尝试用%s生成%s"%(nums,root))
    if len(nums)>1:
        for i in range(int(nums[0])):
            makeDirTenser(path+'\\%s\\'%i,nums[1:])
    else:
        makeDirVector(path,int(nums))

#直接打开程序的预设功能（分别对应前面三个函数：字串、向量、张量）
if __name__ == "__main__":
    # 字串
    print("切换到字串模式。。。")
    root=input("输入根路径（默认为chars）：")
    if root=='':root=r"chars"
    value=input("输入字串参数（留空以跳过）：")
    if value!='': makeDirsByChar(root,value)
    # 向量
    print("切换到向量模式。。。")
    root=input("输入根路径（默认为vecter）：")
    if root=='':root=r"vecter"
    value=input("输入文件夹数量（留空以跳过）：")
    if value!='': makeDirVector(root,int(value))
    # 张量
    makeDirTenser(root,value)
    print("切换到张量模式。。。")
    root=input("输入根路径（默认为tenser）：")
    if root=='':root=r"tenser"
    value=input("输入张量阶数序列（留空以跳过）：")
    if value!='': makeDirTenser(root,value)

'''
-并没有什么用的末尾注释-
'''
