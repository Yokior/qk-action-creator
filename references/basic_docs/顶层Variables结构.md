# 顶层 Variables 结构

## 作用

- 这份文档专门回答动作 JSON 顶层 `Variables` 数组怎么写。
- 这不是 Quicker 官方“变量帮助页”的替代，而是给 `qk-action-creator` 直接使用的离线规则，用来防止猜字段。

## 离线最小结构

- 常见最小变量项至少可包含：
  - `Key`
  - `Type`
  - `Desc`
  - `DefaultValue`
- 直接可用模板：

```json
{
  "Key": "var_name",
  "Type": "Text",
  "Desc": "变量说明",
  "DefaultValue": ""
}
```

## 扩展字段

- 只有需求明确涉及对应能力时，才补这些字段：
  - `SaveState`
  - `IsInput`
  - `IsOutput`
  - `ParamName`
  - `TableDef`
  - `CustomType`
  - `Group`

## `Type` 可直接使用的离线取值

- 常用且推荐：
  - `Text`
  - `Integer`
  - `Number`
  - `Boolean`
  - `List`
  - `Dict`
  - `Table`
  - `Any`
- 其他已确认取值：
  - `Image`
  - `DateTime`
  - `Enum`
  - `Form`
- 不建议作为普通顶层变量默认使用：
  - `Keyboard`
  - `Mouse`
  - `Object`

## 默认值写法

- `Text`：通常写空字符串 `""`
- `Integer`：通常写整数字符串，如 `"0"`
- `Number`：通常写数字字符串，如 `"0"`、`"0.5"`
- `Boolean`：通常写 `"false"` 或 `"true"`
- `List`：默认可写空字符串 `""`，表示空列表
- `Dict`：默认可写空字符串 `""`，表示空词典
- `Table`：默认可写空字符串 `""`，表示空表格
- `Any`：只有明确知道运行时会放入任意对象时才用；默认值优先写空字符串 `""`
- `DateTime`：未明确需要初始值时，优先写空字符串 `""`
- `Image`：未明确需要初始图片时，优先写空字符串 `""`

## 对 qk-action-creator 的直接约束

- 默认新增变量时，优先使用上面的最小结构。
- 只有需求明确涉及状态持久化、子程序输入输出、表格定义、自定义类型分组时，才考虑补充其余字段。
- `IsInput`、`IsOutput` 不能为了“让变量显示出来”随意加。
- 普通动作新增变量时，优先在 `Text`、`Integer`、`Number`、`Boolean`、`List`、`Dict`、`Table`、`Any` 中选。
- 如果离线类型表仍无法覆盖当前需求，直接说明“技能内资料未确认此类型”，不要猜字段。
