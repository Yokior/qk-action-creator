# 跳过后续步骤(continue)

- 模块键: `sys:continue`
- 步骤类型: `Action`
- 说明: 跳过后续步骤（循环内部），开始下一次循环。在循环内部使用。
- 帮助: https://getquicker.net/KC/Help/Doc/continue

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:continue",
  "InputParams": {}
}
```

## 输入参数
无。

## 输出参数
无。

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
