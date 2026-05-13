# Rhino软件控制

- 模块键: `sys:rhinocontrol`
- 步骤类型: `Action`
- 说明: 向Rhino发送命令或脚本
- 帮助: https://getquicker.net/KC/Help/Doc/rhinocontrol

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:rhinocontrol",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "RunScript"
    },
    "command": {
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
| operation | 操作类型 | Enum | 是 | RunScript | RunScript=执行脚本 | 操作类型 |
| command | 命令内容 | Text | 否 |  | 仅用于 RunScript | 命令或脚本内容。 |
| waitResp | 等待命令结束 | Boolean | 否 | true | 仅用于 RunScript |  |
| waitMs | 最长等待时间(ms) | Number | 是 | 10000 |  | 最长的等待返回结果的，毫秒数 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| output | 脚本输出 | Text |  | 仅通过接口执行脚本时支持返回内容。 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
