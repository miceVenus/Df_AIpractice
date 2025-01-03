# Text Processing Application

这是一个简单的文本处理应用程序，使用 socket API 与后端模型进行通信。该应用程序使用 PyQt5 构建图形用户界面（GUI），并使用 MVC（Model-View-Controller）模式组织代码。

## 目录结构

```
Df_AIpractice/
    ├── client
            ├── asset
            ├── config.ini
            ├── controller.py
            ├── feg.bat
            ├── feg.py
            ├── main.py
            ├── model.py
            ├── page.py
            ├── page.ui
    ├── server
            ├── server.py
    ├── test
            ├── fixture.py
            ├── test_mulThread.py
    ├── requirement.txt
    └── README.md
```

## 文件说明

- `controller.py`：控制器模块，负责处理用户输入、与模型交互并更新视图。
- `main.py`：主程序入口，负责初始化应用程序并启动主事件循环。
- `model.py`：模型模块，包含文本处理的业务逻辑。
- `page.py`：视图模块，包含由 PyQt5 生成的用户界面代码。
- `server.py`：服务器模块，负责接收客户端请求并与后端模型进行对接。

## 安装和运行

### 先决条件

- Python 3.10.10
- PyQt5

### 安装依赖

使用以下命令安装所需的依赖：

```bash
pip install -r requirements.txt
```

### 运行应用程序

在终端中导航到项目目录并运行以下命令：

```bash
python main.py
```
或者使用终端方式(当前仅限于在当前目录使用 无法在全局调用feg命令)
```bash
feg [your files] [输出文件位置]
```

### 运行服务器

在终端中导航到项目目录并运行以下命令：

```bash
python server.py
```

## 修改说明

在 model.py中的 ProcessTextIn和 ProcessUploadFile方法中实现具体的文本处理逻辑。你需要调用后端 API 来处理文本，并返回处理后的字符串。
修改server文件的DataProcess函数，使其能够正确调用模型的方法，并返回处理后的文本。

客户端直接修改config.ini文件中的server段中的服务器配置即可

## 配置环境

使用 Python 3.10.10 环境，并安装所需的依赖：

```bash
pip install -r requirements.txt
```

### TO DO:
    - [] 完成feg命令的安全全局调用
    - [] 继续美化界面原型
    - [] 还有什么没完成呢
## 贡献

上述readme部分由copilot生成，后续会根据实际情况进行修改。
