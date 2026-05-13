# 运行C#代码

- 模块键: `sys:csscript`
- 步骤类型: `Action`
- 说明: 执行 C# 代码片段。
- 帮助: https://getquicker.net/KC/Help/Doc/csscript

## 先记结论

- 这是兜底步骤，不是默认步骤。
- 普通模式与低权限模式的 `Exec` 签名不同，不能混写。
- 普通模式读写动作变量，直接用 `Quicker.Public.IStepContext`。
- 低权限模式没有 `stepContext`，只能收一个字符串参数并返回字符串结果。
- 需要 WPF、剪贴板、窗口时，不要依赖 `auto`，显式选线程。
- CodeDOM 模式按旧语法写，避免新语法。

## 最小 JSON

```json
{
  "StepRunnerKey": "sys:csscript",
  "InputParams": {
    "mode": {
      "VarKey": "",
      "Value": "normal"
    },
    "script": {
      "VarKey": "",
      "Value": "//.cs  文件类型，便于外部编辑时使用\\r\\nusing Quicker.Public;\\r\\n\\r\\npublic static string Exec(IStepContext context)\\r\\n{\\r\\n    object oldValue = context.GetVarValue(\"text\");\\r\\n    string value = oldValue == null ? \"\" : oldValue.ToString();\\r\\n    string newValue = \"Hello, \" + value;\\r\\n    context.SetVarValue(\"text\", newValue);\\r\\n    return newValue;\\r\\n}\\r\\n"
    },
    "reference": {
      "VarKey": "",
      "Value": ""
    },
    "runOnUiThread": {
      "VarKey": "",
      "Value": "auto"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "rtn": "out_rtn"
  }
}
```

## 输入参数

| Key | 名称 | 类型 | 必填 | 适用模式 | 说明 |
| --- | --- | --- | --- | --- | --- |
| mode | 运行模式 | Enum | 是 | 全部 | `normal_roslyn` / `normal` / `low_permission_roslyn` / `low_permission` / `generate_assembly` |
| script | 脚本内容 | Text | 是 | `normal` / `normal_roslyn` | 普通模式脚本，签名必须是 `Exec(IStepContext context)` |
| scriptForLp | 脚本内容 | Text | 是 | `low_permission` / `low_permission_roslyn` | 低权限模式脚本，签名必须是 `Exec(string paramValue)` |
| paramValue | 参数值 | Text | 是 | `low_permission` / `low_permission_roslyn` | 传给低权限脚本的字符串 |
| waitResp | 等待返回 | Boolean | 否 | `low_permission` / `low_permission_roslyn` | 是否等待低权限脚本返回 |
| waitMs | 最长等待时间(ms) | Number | 是 | `low_permission` / `low_permission_roslyn` | 超时控制 |
| reference | 引用 DLL 库 | Text | 否 | 全部 | 每行一个 DLL 路径 |
| runOnUiThread | 执行线程 | Enum | 否 | `normal` / `normal_roslyn` | `auto` / `ui` / `background` / `sta` / `staLongRun` |
| stopIfFail | 失败后停止 | Boolean | 否 | 全部 | 失败后是否停止动作 |

## 输出参数

| Key | 名称 | 类型 | 适用模式 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean | 全部 | 操作是否成功 |
| rtn | 返回内容 | Text | `normal` / `normal_roslyn` | `Exec(IStepContext context)` 的返回值 |
| resp | 返回内容 | Text | `low_permission` / `low_permission_roslyn` | 低权限脚本返回的文本 |
| rtnAssembly | 程序集对象 | Object | `generate_assembly` | 生成的程序集对象 |
| assemblyPath | 程序集路径 | Text | `generate_assembly` | 生成的程序集路径 |

## 普通模式

普通模式在 Quicker 进程内运行。脚本入口固定写法：

```csharp
using Quicker.Public;

public static string Exec(IStepContext context)
{
    object oldValue = context.GetVarValue("text");
    string value = oldValue == null ? "" : oldValue.ToString();
    string newValue = "Hello, " + value;
    context.SetVarValue("text", newValue);
    return newValue;
}
```

要点：

- `GetVarValue("变量名")` 读取动作变量。
- `SetVarValue("变量名", 值)` 写回动作变量。
- 返回值走输出参数 `rtn`。
- 如果只需要写变量，不关心返回值，可以把 `Exec` 写成 `void`。

### 常用能力

```csharp
using System.Collections.Generic;
using Quicker.Public;

public static string Exec(IStepContext context)
{
    object title = context.EvalExpression("{标题}");

    IDictionary<string, object> spResult = context.RunSp(
        "子程序名",
        new Dictionary<string, object>
        {
            { "input1", "abc" },
            { "input2", 123 }
        }
    );

    string oldState = context.ReadState("my_key", "");
    context.WriteState("my_key", oldState + "|next");

    context.WriteCache("cache_key", "hello", 600);
    string cacheValue = context.ReadCache<string>("cache_key", "");

    return cacheValue;
}
```

可直接使用的方法：

- `GetVarValue(string varName)`
- `SetVarValue(string varName, object value)`
- `EvalExpression(string expression, bool onUiThread = false)`
- `RunSp(string spName, IDictionary<string, object> inputParams)`
- `RunSp(string spName, object inputParams)`
- `ReadState(string key, string defaultValue)`
- `WriteState(string key, string value)`
- `ReadCache<T>(string key, T defaultValue)`
- `WriteCache(string key, object value, int maxKeepSeconds)`

### 状态存取示例

```csharp
using Quicker.Public;

public static string Exec(IStepContext context)
{
    string oldJson = context.ReadState("items_json", "[]");
    string newJson = oldJson;
    context.WriteState("items_json", newJson);
    context.SetVarValue("items_json", newJson);
    return newJson;
}
```

## 低权限模式

低权限模式在独立进程中运行。脚本入口固定写法：

```csharp
public static string Exec(string paramValue)
{
    return "收到参数:" + paramValue;
}
```

要点：

- 没有 `stepContext`。
- 不能直接读写动作变量。
- 输入只走 `paramValue`。
- 返回只走输出参数 `resp`。
- 适合 COM、隔离执行、避免占用主进程的场景。

## 线程选择

- `ui`：需要 WPF、窗口、部分 UI 对象时使用。
- `sta`：需要 STA 但不想占 UI 线程时使用。
- `staLongRun`：需要独立 STA 线程且运行时间较长时使用。
- `background`：普通后台逻辑。
- `auto`：不作为默认依赖，只有明确知道脚本不碰 UI / STA 时才考虑。

## 什么时候用它

适合：

- 需要访问 Quicker 内部服务或运行时对象。
- 需要 `IStepContext` 提供的状态、缓存、子程序、表达式能力。
- 内置步骤加表达式已经明显失去可维护性。

不适合：

- 变量加减、三元判断、简单拼文本。
- 普通列表、文本、文件处理且已有现成步骤。
- 只是为了把一两句表达式搬进脚本。

## 生成规则

- 普通模式默认优先 `mode = normal`。
- 若明确需要 Roslyn，再改 `normal_roslyn`。
- 若明确需要低权限进程，再改 `low_permission` 或 `low_permission_roslyn`。
- JSON 里普通模式写 `script`。
- JSON 里低权限模式写 `scriptForLp`、`paramValue`、`waitResp`、`waitMs`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
- CodeDOM 环境按旧语法兼容，不要默认使用新语法糖。
