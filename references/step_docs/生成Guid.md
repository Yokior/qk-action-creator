# 生成Guid

- 模块键: `sys:newGuid`
- 步骤类型: `Action`
- 说明: 生成一个新的Guid(全局唯一ID标示符)，并转换为文本格式。
- 帮助: https://getquicker.net/KC/Help/Doc/newguid

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:newGuid",
  "InputParams": {
    "format": {
      "VarKey": "",
      "Value": "D"
    },
    "upper": {
      "VarKey": "",
      "Value": "false"
    }
  },
  "OutputParams": {
    "output": "out_output"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| format | 格式 | Enum | 否 | D | D=默认：00000000-0000-0000-0000-000000000000 / N=去除连字符：00000000000000000000000000000000 / B=大括号包围：{00000000-0000-0000-0000-000000000000} / P=小括号包围：(00000000-0000-0000-0000-000000000000) / X=十六进制：{0x00000000,0x0000,0x0000,{0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00}} | 转换为文本时使用的格式 |
| upper | 大写 | Boolean | 否 | false |  | 字母输出为大写格式。 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| output | 内容 | Text |  | 将获得的文本写入到变量 |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
