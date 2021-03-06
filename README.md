# makeFolderTenser 文件夹张量制作

本程序用于快速创建一系列的「简单文件夹」，即一系列名称简单到只有一个字符的文件夹；而创建这些文件夹的参数只需要一个字符串就能轻松设定

# 文件夹矩阵/文件夹张量

* 定义：文件夹的一个规则嵌套结构
* 特征：每个同一「层级」的文件夹都包含一定数量（可能名称也一样）的「子文件夹」
* 其相当于一个索引矩阵（可能是「张量」），其包含的值（本质上是集合，但一般是文件）使用一个特定的序列（等价于一个向量）进行访问；
* 原理/作用/用途：通过增大其他用户逐一检索文件夹之难度以「隐藏」部分文件夹或文件
* 示例：4235表示这个文件夹的第一层包含四个文件夹，每个「第一层文件夹」包含两个「子文件夹」，每个「第二层文件夹」包含三个「子文件夹」，每个「第三层文件夹」包含五个「子文件夹」
* 注意：这种文件夹矩阵随着其字符串长度的增长而成指数增长，所以创建「文件夹张量」时字符串长度最好不要超过5

# 示例

* 字串模式，参数：「这是一个序列」
* 向量模式，参数：20
* 张量模式，参数：4235
* 注：张量模式中演示了「如何通过索引寻找特定文件」
