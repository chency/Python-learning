# 学些类_class
    类首先得从作用域开始谈起
## 作用域与命名空间_scope and namespace

* 不同作用域中的访问顺序
    - the innermost scope, which is searched first, contains the local names 
    - the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope,
      contains non-local, but also non-global names 
    - the next-to-last scope contains the current module’s global names 
    - the outermost scope (searched last) is the namespace containing built-in names
    简单地说访问顺序是从最内层作用域开始查找的
    如果里层作用域想要使用外层作用域的变量等，可以使用 _nonlocal id_
     _global id_ 声明该变量属于最外层的全局作用域代码为例
     
'''

    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"
    
        def do_global():
            global spam
            spam = "global spam"
    
        spam = "test spam"
        do_local()
        print("After local assignment:", spam)  # After local assignment: test spam
        do_nonlocal()
        print("After nonlocal assignment:", spam)   # After nonlocal assignment: nonlocal spam
        do_global()
        print("After global assignment:", spam) # After global assignment: nonlocal spam，该变量可以在scope_test作用域中找到
    
    scope_test()
    print("In global scope:", spam) # In global scope: global spam，该变量只能在全局作用域中找到

'''
* 类的结构

'''

    class ClassName:
        <statement-1>
        .
        .
        .
        <statement-N>

'''

    - 看文档貌似statement可以是if语句呀
    - class的构造函数为 def __init__(self):
    - 并不会重载，而是以最后一个有效
    - ClassName.func 与 Instancel.func差别是蛮大的，前者只是一个通用方法，类似于JAVA中的静态函数，而后者则是
    - 类的静态变量与对象的成员变量有本质的区别，这个区别可以用作用域来解释。已经初始化后的对象对于它指向的变量本身在对变量进行
      左值操作之前，变量指向的是类作用域的静态变量，左值操作之后，就为对象的成员变量，可以通过vars(instance).items()查看
      而在del 对象的成员变量之后，该变量指向的是类作用域的静态变量。例子参见learnclass.py的test_normal_classval部分
    - 注意上面一条中左值操作针对的是指向的变量，如果修改的是指向变量指向的对象，并不是左值操作。例如官方文档中提到的类的静态变量
      指向的是一个链表，实例对象在对链表成员是并不会实例化静态变量
    - 对象的成员是可以动态添加的，同时也是可以删除的

* 类的继承

'''

    class DerivedClassName(BaseClassName):
        <statement-1>
        .
        .
        .
        <statement-N>
'''
  
   - 继承的基类可以为module.baseclass类型的结构
   - 类的方法支持重写
   - 调用父类的方法为BaseClassName.methodname(self, arguments).
   - isinstance() 判断实例的类型
   - issubclass 判断是否是xx的子类
   
* 类的多重继承，没有多大的意义吧

* 私有成员变量

    - 以双下划线开头的变量为私有变量
    

    
