# WriteFileToClipboardStep

- 模块键: `sys:fileToClipboard`
- 步骤类型: `Action`
- 帮助: https://getquicker.net/KC/Help/Doc/filetoclipboard

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:fileToClipboard",
  "InputParams": {
    "file": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "list": {
      "VarKey": "",
      "Value": "item1\\nitem2"
    },
    "useCut": {
      "VarKey": "",
      "Value": "false"
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
| file | CommonStrings.WriteFileToClipboardStep_FileParam_Name | Text | 否 |  |  | CommonStrings.WriteFileToClipboardStep_FileParam_Desc |
| list | CommonStrings.WriteFileToClipboardStep_FileListParam_Name | List | 否 |  |  | CommonStrings.WriteFileToClipboardStep_FileListParam_Desc |
| useCut | 剪切文件 | Boolean | 否 | false |  | 是否剪切文件 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
