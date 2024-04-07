# codex2

**变量赋值**

    !cbl 变量名 = 值;
    cbl hello = "hello world";
    cprint(hello);

**打印语句**

cprint(str|int|variable)

str:
    cprint("hello world");

int:
    cprint(114514);

variable:
    cbl hello = "hello world";
    cprint(hello);
  
**文件后缀名**

.p 是示例文件或是模块, .codex 是程序代码文件

**模块**

编写好的模块需要放到Lib文件夹中,编写语句如下:

//modules.p
    !modules.p
    !用于实现一个简单的打印函数

    cbk print = "cprint(text)";
        ^^^^^    ^^^^^^  ^^^^
    !   函数名   执行语句|希望参数名

//code.codex

    import <modules.p>
    !导入modules.p 模块

    !满足模块中print函数期望的变量值
    cbl text = "Hello,world";
    !执行print函数
    run(cbl['print']);

