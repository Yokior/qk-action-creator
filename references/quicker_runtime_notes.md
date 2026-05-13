# Quicker 运行备注

## 外部执行动作并传入 JSON 文件路径

目标：在 Quicker 外部通过命令行启动一个动作，把“动作定义 JSON 文件路径”作为动作参数传入，再由动作内部的运行 C# 脚本读取文件并改写目标动作。

1. 基本格式
- `cmd.exe /c "C:\\Program Files\\Quicker\\QuickerStarter.exe" -c runaction:注入器动作ID?"json文件路径"`

2. 样例

```bat
cmd.exe /c 'C:\Program Files\Quicker\QuickerStarter.exe' -c runaction:c2b4ebf9-1a50-4e7c-ac20-acef79fb0cdb?'D:\Downloads\codex_test\quicker\测试生成_提示框.json'
```

3. 参数含义
- `-c`
  - 让 Quicker 通过控制台输出动作返回结果，默认最长等待 20 秒。
- `runaction:注入器动作ID?...`
  - 表示启动指定注入器动作，并把问号后面的内容写入目标动作的 `quicker_in_param`。
- `"json文件路径"`
  - 当前约定这里传入的是 JSON 文件路径，不直接传 JSON 文本。

4. 动作内配套约定
- `actionId`
  - 目标被改写动作的 ID。（由用户提前手动设置，未设置会报错 targetActionId 为空）
- `quicker_in_param`
  - JSON 文件路径。（只需要关注这个）

5. 返回结果
- 成功时返回：`ok`
- 失败时返回：运行 C# 脚本中的错误文本

6. 在当前环境里获取返回值的推荐方式
- 优先使用技能目录下的 `scripts/run_quicker_inject.py`
- 原因：
  - `QuickerStarter.exe -c` 的返回值在不同控制台宿主里表现不完全一致
  - 直接用交互式终端手输 `cmd.exe /c ...` 往往能看到 `ok`
  - 但某些工具宿主下，直接执行 `cmd` 命令可能拿不到标准输出
- 已验证可稳定获取返回值的调用方式：

```python
from subprocess import Popen, PIPE

proc = Popen(
    [
        r"C:\Program Files\Quicker\QuickerStarter.exe",
        "-c",
        r"runaction:动作标识?D:\path\action.json",
    ],
    stdout=PIPE,
    stderr=PIPE,
)
out, err = proc.communicate()
```

- 要点：
  - 不使用 `shell=True`
  - 必须传 `stdout=PIPE`
  - 如需读取错误文本，同时传 `stderr=PIPE`
  - `runaction:动作标识?参数` 这一整段应作为单独一个参数传入
  - 不要再手动给 JSON 路径额外包一层双引号，否则 Quicker 会把引号视为路径内容
