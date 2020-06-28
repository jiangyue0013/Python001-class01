学习笔记
Selector 使用 XPath

XPath 的路径匹配

* '/' 从最上层的路径开始匹配（系统自动生成的匹配多使用）
* '//' 前面可以是任意长的路径，比较灵活
* '.' 当前匹配位置向下找
* '..' 查找平级的位置（一般用于有同名的情况）

标签中的内容使用 @text() 获取，标签的属性使用 @标签名 获取。

XPath 性能相比 BeautifulSoup 提升不止十倍。

调试:

1. 使用浏览器
2. 直接输出

XPath 匹配到的数据，列表的形式存储。

释放数据使用：

* extract() 释放所有
* extract_first() 释放第一个

还可以使用内部函数如 strip() 进行处理。

Request 中设置 dont_filter = Frue

不受 domin 限制