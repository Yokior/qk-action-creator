# GetClipboardTextStep

- 模块键: `sys:getClipboardText`
- 步骤类型: `Action`
- 帮助: https://getquicker.net/KC/Help/Doc/getClipboardText

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:getClipboardText",
  "InputParams": {
    "format": {
      "VarKey": "",
      "Value": "UnicodeText"
    },
    "customFormat": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "encoding": {
      "VarKey": "",
      "Value": "utf-8"
    },
    "waitMs": {
      "VarKey": "",
      "Value": "400"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "output": "out_output",
    "cleanHtml": "out_cleanHtml",
    "htmlDoc": "out_htmlDoc",
    "url": "out_url",
    "elapsedMs": "out_elapsedMs"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| format | CommonStrings.GetClipboardTextStep_TxtFormatParam_Name | Enum | 否 | UnicodeText | Custom=自定义格式名 | CommonStrings.GetClipboardTextStep_TxtFormatParam_Desc |
| customFormat | 格式名称 | Text | 否 |  | 仅用于 Custom | 自定义的剪贴板格式名，请和实际剪贴板格式名一致。只支持实际为文本类型的内容。 |
| encoding | 文本编码 | Enum | 是 | utf-8 | 仅用于 Custom | 读取自定义格式时候使用的编码类型 |
| waitMs | 重试时间 | Integer | 否 | 400 |  | 每10ms重试一次，直到获取到文本。为0时不重试。 |
| stopIfFail | CommonStrings.GetClipboardTextStep_StopIfEmptyParam_Name | Boolean | 否 | true |  | CommonStrings.GetClipboardTextStep_StopIfEmptyParam_Desc |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | CommonStrings.GetClipboardTextStep_SuccessParam_Name | Boolean |  | CommonStrings.GetClipboardTextStep_SuccessParam_Desc |
| output | 完整结果内容 | Text |  | CommonStrings.GetClipboardTextStep_OutputParam_Desc |
| cleanHtml | 主要HTML片段 | Text | 仅用于 Html | HTML的主要内容。<!--StartFragment-->和<!--EndFragment-->之间的部分 |
| htmlDoc | 完整的HTML文档 | Text | 仅用于 Html | 仅去除剪贴板头部信息的完整HTML文档内容。包含<html>等标签，可直接保存为.html文件。 |
| url | 来源网址 | Text |  | 从网页中复制内容时，可能会携带网址信息。 |
| elapsedMs | 已更新时间 | Integer |  | 剪贴板最后更新是在多少毫秒以前 |

## 要点
- 控制参数: `format`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
