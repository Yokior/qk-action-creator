# 图片/Base64 转换

- 模块键: `sys:imgToBase64`
- 步骤类型: `Action`
- 说明: 图片和Base64转换
- 帮助: https://getquicker.net/KC/Help/Doc/imgtobase64

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:imgToBase64",
  "InputParams": {
    "type": {
      "VarKey": "",
      "Value": "imgToBase64"
    },
    "img": {
      "VarKey": "",
      "Value": ""
    },
    "addHeader": {
      "VarKey": "",
      "Value": "false"
    },
    "base64": {
      "VarKey": "",
      "Value": "示例文本"
    }
  },
  "OutputParams": {
    "code": "out_code",
    "img": "out_img"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| type | 操作类型 | Enum | 否 | imgToBase64 | imgToBase64=图片或文件转Base64文本 / base64ToImg=Base64文本转图片 | 转换操作类型 |
| img | 图片 | Image | 是 |  | 仅用于 imgToBase64 | 要转换的图片（图片变量或文件路径） |
| addHeader | 添加data头 | Boolean | 否 | false | 仅用于 imgToBase64 | 是否添加“data:image/png;base64,”头 |
| base64 | Base64编码 | Text | 是 |  | 仅用于 base64ToImg | 要转换的编码文本 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| code | Base64编码 | Text | 仅用于 imgToBase64 | Base64编码结果 |
| img | 图片 | Image | 仅用于 base64ToImg | 转换输出的图片 |

## 要点
- 控制参数: `type`。先定控制参数，再看其余参数是否生效。
- 部分参数偏向变量模式。此类参数实际写入时应优先填写 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
