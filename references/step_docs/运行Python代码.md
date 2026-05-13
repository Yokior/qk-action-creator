# 运行Python代码

- 模块键: `sys:pythonscript`
- 步骤类型: `Action`
- 说明: 执行Python代码片段。
- 帮助: https://getquicker.net/KC/Help/Doc/pythonscript

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:pythonscript",
  "InputParams": {
    "script": {
      "VarKey": "",
      "Value": "##.py \\r\\nquicker.context.SetVarValue('text', 'hello world')\\r\\n"
    },
    "pythonPath": {
      "VarKey": "",
      "Value": "示例文本"
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
| script | 脚本内容 | Text | 是 | ##.py \r\nquicker.context.SetVarValue('text', 'hello world')\r\n |  | 要运行的脚本内容 |
| pythonPath | Python环境路径 | Text | 否 |  |  | 可选。Python环境(PythonXXX.dll)所在目录，留空时使用全局设置 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
