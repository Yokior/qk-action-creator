# 模拟按键A（录入）

- 模块键: `sys:keyInput`
- 步骤类型: `Keyboard`
- 说明: 模拟键盘输入
- 帮助: https://getquicker.net/KC/Help/Doc/keyinput

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:keyInput",
  "InputParams": {
    "keys": {
      "VarKey": "",
      "Value": ""
    },
    "repeat": {
      "VarKey": "",
      "Value": "1"
    },
    "interval": {
      "VarKey": "",
      "Value": "1"
    },
    "holdMs": {
      "VarKey": "",
      "Value": "-1"
    }
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| keys | 按键 | Keyboard | 是 |  |  | 模拟的按键内容 |
| repeat | 重复次数 | Integer | 否 | 1 |  |  |
| interval | 重复间隔(毫秒) | Integer | 否 | 1 |  | 每次重复之间的间隔毫秒数 |
| holdMs | 保持毫秒数 | Integer | 否 | -1 |  | 普通键（非Ctrl/Alt/Shift/Win）在抬起前保持的时间。-1表示使用默认设置。\r\n某些直接模拟按键无法生效的软件中可以尝试增加此值。 |

## 输出参数
无。

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
