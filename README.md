# Knowledge Animation Studio (Manim) 🎬

> **基于 Manim Community 的数学/知识可视化动画工作台**

这份文档用于记录如何在新电脑上**从零开始**复活这个项目，以及如何配置开发环境。

## 🛠️ 第一步：下载项目 (Clone)

打开你想要存放项目的文件夹，右键打开终端 (CMD/PowerShell/Git Bash)：

```
# 1. 克隆代码库 (换成你的仓库地址)
git clone [https://github.com/你的用户名/Knowledge-Animation-Studio.git](https://github.com/你的用户名/Knowledge-Animation-Studio.git)

# 2. 进入目录
cd Knowledge-Animation-Studio
```

## 📦 第二步：安装系统级依赖 (必做!)

Manim 极其依赖两个外部软件，缺一不可。

### 1. FFmpeg (视频处理引擎)

- **验证：** 在终端输入 `ffmpeg -version`。如果看到版本号，说明已安装。
- **安装：** 如果没装，去 [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) 下载 `release-full.7z`，解压并把 `bin` 文件夹路径添加到系统环境变量 Path 中。

### 2. LaTeX (公式渲染引擎)

- **作用：** 如果你想用 `MathTex` 写漂亮的数学公式，必须装这个。
- **推荐：** 下载并安装 [MiKTeX](https://miktex.org/download) (Windows) 或 TeX Live。
- **验证：** 安装完后重启终端，输入 `latex --version`。

## 🐍 第三步：配置 Python 环境

不要直接用系统 Python，建立一个干净的虚拟环境。

```
# 1. 创建虚拟环境 (文件夹名 venv)
python -m venv venv

# 2. 激活环境 (Windows)
# CMD:
venv\Scripts\activate
# PowerShell:
venv\Scripts\Activate.ps1

# 3. 安装 Python 依赖库
# (Manim 本体和相关库都在这里)
pip install -r requirements.txt
```

## ⚙️ 第四步：VS Code 最佳配置 (推荐)

为了获得“点击播放”的丝滑体验，建议配置 VS Code。

1. **打开项目：** 在 VS Code 中点击 `File -> Open Folder`，选择本项目根目录。
2. **安装插件：** 搜索并安装 **Manim Sideview**。
3. **选择解释器：** 点击右下角的 Python 版本号，选择 `('venv': venv)`。
4. **确认工作目录：** 确保 `.vscode/settings.json` (如果项目里有) 指向了正确的路径。通常默认即可。

## ▶️ 第五步：运行动画

### 方式 A：命令行运行 (最稳)

在项目根目录的终端中 (确保有 `(venv)` 前缀)：

```
# 格式: manim -pql [脚本文件路径] [类名]
# -p: 预览 (preview)
# -ql: 低画质 (quality low)

manim -pql scenes/demo_scene.py HelloManim
```

### 方式 B：VS Code 侧边栏运行

1. 打开 `.py` 脚本文件。
2. 点击右上角的 **Manim** 图标。
3. 选择你要渲染的 `Scene` 类名。
4. 视频会在右侧窗口预览。

## 📂 产出物在哪里？

根据配置文件 `manim.cfg`，生成的文件通常位于：

- **`./media/videos/`**

*(注意：media 文件夹已被 .gitignore 忽略，不会上传到 GitHub)*