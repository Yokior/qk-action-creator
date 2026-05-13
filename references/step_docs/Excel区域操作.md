# Excel区域操作

- 模块键: `sys:excelRange`
- 步骤类型: `Action`
- 说明: 操作Excel的某个区域或单元格
- 帮助: https://getquicker.net/KC/Help/Doc/excelrange

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:excelRange",
  "InputParams": {
    "range": {
      "VarKey": "",
      "Value": ""
    },
    "subRange": {
      "VarKey": "",
      "Value": "FullArea"
    },
    "operation": {
      "VarKey": "",
      "Value": "SetValue"
    },
    "value": {
      "VarKey": "",
      "Value": ""
    },
    "cellSize": {
      "VarKey": "",
      "Value": ""
    },
    "methods": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "replaceWhat": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "replaceTo": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "replaceEscapeWhat": {
      "VarKey": "",
      "Value": "false"
    },
    "replaceEscapeTo": {
      "VarKey": "",
      "Value": "true"
    },
    "replaceMatchCase": {
      "VarKey": "",
      "Value": "false"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "value": "out_value",
    "text": "out_text",
    "formula": "out_formula",
    "numberFormat": "out_numberFormat",
    "address": "out_address",
    "column": "out_column",
    "row": "out_row",
    "colNum": "out_colNum",
    "rowNum": "out_rowNum",
    "style": "out_style",
    "range": "out_range",
    "sheet": "out_sheet"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| range | 区域 | Object | 否 |  |  | 可以输入区域变量、留空(表示当前选择区域）、used(表示当前工作表的使用区域)或区域范围如A1:E9等，请参考文档。 |
| subRange | 限定子范围 | Enum | 是 | FullArea | FullArea=整个区域 / FirstRow=区域内的第一行 / FirstColumn=区域内的第一列 / LastRow=区域内最后一行 / LastColumn=区域内最后一列 / ActiveCell=活动单元格 / EntireRow=整行(包含区域外) / EntireColumn=整列(包含区域外) / Rows=所有行(区域范围内) / Columns=所有列(区域范围内) | 根据需要，将要操作的目标限定为一个子区域 |
| operation | 操作类型 | Enum | 是 | SetValue | SetValue=设置值 / SetFormula=设置公式 / SetNumberFormat=设置数值格式 / SetCellSize=行高,列宽 / SetStyle=设置格式 / CallMethod=调用方法 / Replace=替换内容 / GetRangeInfo=获取区域信息 | 操作类型 |
| value | 参数 | Any | 否 |  | 仅用于 SetValue, SetFormula, SetNumberFormat | 要设置的内容 |
| cellSize | 行高,列宽 | Any | 否 |  | 仅用于 SetCellSize | -表示不改变，auto表示自动，数字表示具体值。如auto,auto表示自适应高度和宽度 |
| methods | 方法 | Text | 否 |  | 仅用于 CallMethod | 要调用的方法，每行一个。格式请参考文档。 |
| replaceWhat | 查找内容 | Text | 是 |  | 仅用于 Replace | 要替换的内容 |
| replaceTo | 替换为 | Text | 是 |  | 仅用于 Replace | 替换成的内容 |
| replaceEscapeWhat | 转义“查找内容” | Boolean | 否 | false | 仅用于 Replace | 替换“查找内容”中的转义字符（\\r,\\n,\\t） |
| replaceEscapeTo | 转义“替换为” | Boolean | 否 | true | 仅用于 Replace | 替换“替换为”中的转义字符（\\r,\\n,\\t） |
| replaceMatchCase | 区分大小写 | Boolean | 否 | false | 仅用于 Replace |  |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| value | 值 | Any | 仅用于 GetRangeInfo | 单元格的值 |
| text | 文本 | Text | 仅用于 GetRangeInfo | 单元格的显示文本 |
| formula | 公式 | Text | 仅用于 GetRangeInfo | 单元格的公式值 |
| numberFormat | 数值格式 | Text | 仅用于 GetRangeInfo | 单元格数值格式值 |
| address | 位置引用 | Text | 仅用于 GetRangeInfo | 区域位置范围 |
| column | 列号 | Integer | 仅用于 GetRangeInfo | 左上角单元格从1开始的列数 |
| row | 行号 | Integer | 仅用于 GetRangeInfo | 左上角单元格从1开始的行数 |
| colNum | 列数 | Integer | 仅用于 GetRangeInfo | 区域包含的列数 |
| rowNum | 行数 | Integer | 仅用于 GetRangeInfo | 区域包含的行数 |
| style | 格式信息 | Text | 仅用于 GetRangeInfo | 单元格的格式 |
| range | 区域对象 | Object | 仅用于 GetRangeInfo | Range对象 |
| sheet | 工作表对象 | Object | 仅用于 GetRangeInfo | WorkSheet对象 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
