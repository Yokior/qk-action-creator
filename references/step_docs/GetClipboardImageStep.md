# GetClipboardImageStep

- 模块键: `sys:getClipboardImage`
- 步骤类型: `Action`
- 帮助: https://getquicker.net/KC/Help/Doc/getclipboardimage

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:getClipboardImage",
  "InputParams": {
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "output": "out_output",
    "elapsedMs": "out_elapsedMs"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| stopIfFail | CommonStrings.GetClipboardImageStep__stopIfEmptyParam | Boolean | 否 | true |  | CommonStrings.GetClipboardImageStep__stopIfEmptyParam_Desc |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | CommonStrings.GetClipboardImageStep__successParam | Boolean |  | CommonStrings.GetClipboardImageStep__successParam_desc |
| output | CommonStrings.GetClipboardImageStep__outputParam_img | Image |  | CommonStrings.GetClipboardImageStep__outputParam_img_desc |
| elapsedMs | 已更新时间 | Integer |  | 剪贴板最后更新是在多少毫秒以前 |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
