# Excel文件读写

- 模块键: `sys:excelreadwrite`
- 步骤类型: `Action`
- 帮助: https://getquicker.net/KC/Help/Doc/excelreadwrite

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:excelreadwrite",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "load"
    },
    "fileType": {
      "VarKey": "",
      "Value": "XSSF"
    },
    "sheetName": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "sourceData": {
      "VarKey": "",
      "Value": ""
    },
    "names": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "writeTitleRow": {
      "VarKey": "",
      "Value": "true"
    },
    "cellIndex": {
      "VarKey": "",
      "Value": "0"
    },
    "dataFormat": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "cellLink": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "replaceDict": {
      "VarKey": "",
      "Value": "{}"
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
| operation | 操作类型 | Enum | 否 |  | load=打开Workbook / newWorkbook=创建Workbook / save=保存Workbook / getSheet=获取Sheet / createSheet=创建Sheet / getRow=获取行 / getCellByValue=查找单元格（根据值） / getCell=读取单元格 / setCell=写入单元格 / writeData=写入多行数据 / mergeCells=合并单元格 / freezePane=冻结窗格 / autoFilter=自动筛选 / setStyle=设置区域单元格样式 / readData=批量提取数据 / batchReplace=批量模板替换 |  |
| fileType | 工作簿类型 | Enum | 否 | XSSF | XSSF=XSSF(.xlsx 2007版Excel) / HSSF=HSSF(.xls 2003版Excel)；仅用于 newWorkbook |  |
| sheetName | 工作表名称 | Text | 否 |  | 仅用于 getSheetByName, createSheet | 要打开的工作表名称 |
| sourceData | 源数据 | Object | 否 |  | 仅用于 writeData | 可以为工作表对象、表格变量或对象列表 |
| names | 名称数据 | Text | 否 |  | 仅用于 addNames | JSON格式的名称数据定义，详细请参考文档。 |
| writeTitleRow | 写入标题行 | Boolean | 否 | true | 仅用于 writeData | 是否输出标题行 |
| cellIndex | 列序号 | Integer | 否 | 0 | 仅用于 getCell, setCell, freezePane | 单元格在所在行里的序号，从0开始 |
| dataFormat | 数据格式 | Text | 否 |  | 仅用于 setCell | 设置单元格的DataFormat |
| cellLink | 链接 | Text | 否 |  | 仅用于 setCell | 可以为网址、邮件地址(mailto:who@domain.com)、工作表名称、文件路径 |
| replaceDict | 替换数据词典 | Dict | 否 |  | 仅用于 batchReplace | 词典格式数据。键为要查找的字段，值为要填充的内容。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- 部分参数偏向变量模式。此类参数实际写入时应优先填写 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
