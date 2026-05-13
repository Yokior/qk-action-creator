# 跳出循环(break)

- 模块键: `sys:break`
- 步骤类型: `Action`
- 说明: 跳出循环（“每个” 或 “重复” 模块）
- 帮助: https://getquicker.net/KC/Help/Doc/break

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:break",
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
