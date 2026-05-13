# WriteClipboardStep

- 模块键: `sys:writeClipboard`
- 步骤类型: `Action`
- 帮助: https://getquicker.net/KC/Help/Doc/writeClipboard

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:writeClipboard",
  "InputParams": {
    "type": {
      "VarKey": "",
      "Value": "auto"
    },
    "customFormat": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "input": {
      "VarKey": "",
      "Value": ""
    },
    "html": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "fastMode": {
      "VarKey": "",
      "Value": "false"
    },
    "text": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "imageVar": {
      "VarKey": "",
      "Value": false
    },
    "successMsg": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| type | CommonStrings.WriteClipboardStep_TypeParam_Name | Enum | 是 | auto | custom=自定义格式 / clearHistory=清空剪贴板历史(Win10+) | CommonStrings.WriteClipboardStep_TypeParam_Desc |
| customFormat | 格式名 | Text | 是 |  | 仅用于 custom | 自定义的剪贴板格式名 |
| input | CommonStrings.WriteClipboardStep__inputParam_Name | Any | 是 |  | 仅用于 auto | CommonStrings.WriteClipboardStep__inputParam_Desc |
| html | CommonStrings.WriteClipboardStep__htmlParam_Name | Text | 是 |  | 仅用于 html | CommonStrings.WriteClipboardStep__htmlParam_Desc |
| fastMode | 快速模式 |  | 否 | false |  | 不需要处理图片中的透明通道时选择 |
| text | CommonStrings.WriteClipboardStep__textParam_Name | Text | 是 |  | 仅用于 html, text, rtf, csv, custom | CommonStrings.WriteClipboardStep__textParam_Desc |
| imageVar | CommonStrings.WriteClipboardStep__imgVarParam_Name | Boolean | 否 |  | 仅用于 image | CommonStrings.WriteClipboardStep__imgVarParam_Desc |
| successMsg | 成功后提示 | Text | 是 |  |  | 可选。写入成功后提示消息，如“XXX已写入剪贴板”。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |

## 要点
- 控制参数: `type`。先定控制参数，再看其余参数是否生效。
- 部分参数偏向变量模式。此类参数实际写入时应优先填写 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
