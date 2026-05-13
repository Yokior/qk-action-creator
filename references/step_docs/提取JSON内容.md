# 提取JSON内容

- 模块键: `sys:jsonExtract`
- 步骤类型: `Action`
- 说明: 提取Json文本中的信息
- 帮助: https://getquicker.net/KC/Help/Doc/jsonExtract

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:jsonExtract",
  "InputParams": {
    "data": {
      "VarKey": "",
      "Value": "示例文本"
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
| data | 输入 | Text | 是 |  |  | 要从中提取内容的Json文本或JToken对象 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否没有异常 |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
