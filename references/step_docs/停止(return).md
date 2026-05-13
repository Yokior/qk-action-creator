# 停止(return)

- 模块键: `sys:stop`
- 步骤类型: `Action`
- 说明: 停止动作或从子程序中返回
- 帮助: https://getquicker.net/KC/Help/Doc/stop

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:stop",
  "InputParams": {
    "method": {
      "VarKey": "",
      "Value": "default"
    },
    "isError": {
      "VarKey": "",
      "Value": "false"
    },
    "return": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "showMessage": {
      "VarKey": "",
      "Value": "示例文本"
    }
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| method | 操作类型 | Enum | 否 | default | default=默认：停止动作或从子程序返回 / forcestop=停止动作：停止整个动作(即使在子程序中) |  |
| isError | 标记为出错 | Boolean | 否 | false |  | 用作子程序或被其他动作调用时，返回出错状态。 |
| return | 返回值 | Text | 否 |  |  | 被其他动作调用时，返回的动作结果。 |
| showMessage | 提示消息 | Text | 否 |  |  | 显示的提示信息。 |

## 输出参数
无。

## 要点
- 控制参数: `method`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
