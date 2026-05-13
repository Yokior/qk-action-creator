# Adobe系列软件控制

- 模块键: `sys:adobesoftscontrol`
- 步骤类型: `Action`
- 帮助: https://getquicker.net/KC/Help/Doc/adobesoftscontrol

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:adobesoftscontrol",
  "InputParams": {
    "software": {
      "VarKey": "",
      "Value": "Photoshop.Application"
    },
    "operation": {
      "VarKey": "",
      "Value": "dojavascript"
    },
    "script": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "scriptFile": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "waitResp": {
      "VarKey": "",
      "Value": "true"
    },
    "waitMs": {
      "VarKey": "",
      "Value": "10000"
    },
    "tryRunScriptUsingExe": {
      "VarKey": "",
      "Value": "false"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "output": "out_output"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| software | 软件名称 | Enum | 是 | Photoshop.Application | Photoshop.Application=Photoshop / Illustrator.Application=Illustrator / afterfx=After Effects | 要执行脚本的软件 |
| operation | 操作类型 | Enum | 是 | dojavascript | dojavascript=执行js脚本 / dojavascriptfile=执行js脚本文件 | 操作类型 |
| script | 脚本内容 | Text | 否 |  | 仅用于 dojavascript | 要执行的js脚本代码。 |
| scriptFile | 脚本文件路径 | Text | 否 |  | 仅用于 dojavascriptfile | js脚本文件的完整路径 |
| waitResp | 等待执行结束 | Boolean | 否 | true |  |  |
| waitMs | 最长等待时间(ms) | Number | 是 | 10000 |  | 最长的等待返回结果的，毫秒数 |
| tryRunScriptUsingExe | 接口失败后，尝试使用程序exe运行脚本文件 | Boolean | 否 | false |  | 使用运行程序并将脚本路径作为参数的方式执行脚本。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| output | 脚本输出 | Text |  | 仅通过接口执行脚本时支持返回内容。 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
