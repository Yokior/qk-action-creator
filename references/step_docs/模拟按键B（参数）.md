# 模拟按键B（参数）

- 模块键: `sys:sendKeys`
- 步骤类型: `Action`
- 说明: 发送按键和文本
- 帮助: https://getquicker.net/KC/Help/Doc/sendKeys

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:sendKeys",
  "InputParams": {
    "keys": {
      "VarKey": "",
      "Value": "示例文本"
    }
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| keys | 按键序列 | Text | 否 |  |  | 要发送的按键序列，使用C#语言SendKeys.Send()语法，具体请参考教程文档。 |

## 输出参数
无。

## 要点
- 带 `TextTools` 的参数在编辑器里通常有选择器辅助，但 JSON 本体仍只写 `VarKey` / `Value`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
