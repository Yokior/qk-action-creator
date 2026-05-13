# 读取Excel文件内容或写入Excel文件

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
    "filePath": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "styleData": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "cellRange": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "sheetName": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "sourceData": {
      "VarKey": "",
      "Value": ""
    },
    "cellAddress": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "names": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "createSheetIfNotExist": {
      "VarKey": "",
      "Value": ""
    },
    "writeTitleRow": {
      "VarKey": "",
      "Value": "true"
    },
    "cellIndex": {
      "VarKey": "",
      "Value": "0"
    },
    "readDataMap": {
      "VarKey": "",
      "Value": ""
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
    "replacePrefixSuffix": {
      "VarKey": "",
      "Value": "{{\\r\\n}}"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "workbook": "out_workbook",
    "worksheetNameList": "out_worksheetNameList",
    "sheet": "out_sheet",
    "firstRow": "out_firstRow",
    "lastRow": "out_lastRow",
    "firstCellNum": "out_firstCellNum",
    "lastCellNum": "out_lastCellNum",
    "dictData": "out_dictData",
    "cellValue": "out_cellValue",
    "cellType": "out_cellType",
    "cellFormula": "out_cellFormula",
    "cellDataFormatString": "out_cellDataFormatString",
    "names": "out_names",
    "cellAddress": "out_cellAddress"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| operation | 操作类型 | Enum | 否 |  | load=打开Workbook / newWorkbook=创建Workbook / save=保存Workbook / getSheet=获取Sheet / createSheet=创建Sheet / getRow=获取行 / getCellByValue=查找单元格（根据值） / getCell=读取单元格 / setCell=写入单元格 / writeData=写入多行数据 / mergeCells=合并单元格 / freezePane=冻结窗格 / autoFilter=自动筛选 / setStyle=设置区域单元格样式 / readData=批量提取数据 / batchReplace=批量模板替换 |  |
| fileType | 工作簿类型 | Enum | 否 | XSSF | XSSF=XSSF(.xlsx 2007版Excel) / HSSF=HSSF(.xls 2003版Excel)；仅用于 newWorkbook |  |
| filePath | 文件路径 | Text | 否 |  | 仅用于 load, save | 要打开或写入的Excel文件路径 |
|  |  | Integer | 否 | 0 | 仅用于 getSheetByIndex, getSheetByName, getSheet, createSheet, save, readData, addNames | 以0开始计算的序号 |
| styleData | 样式设置 | Text | 否 |  | 仅用于 readData | 请参考模块文档。 |
| cellRange | 提取数据定义 | Text | 否 |  | 仅用于 getSheetByIndex, getSheet | 每行一条规则：“字段:[工作表序号或名称]单元格地址”，详情请参考模块文档。 |
| sheetName | 工作表名称 | Text | 否 |  | 仅用于 getSheetByName, createSheet | 要打开的工作表名称 |
| sourceData | 源数据 | Object | 否 |  | 仅用于 writeData | 可以为工作表对象、表格变量或对象列表 |
| cellAddress | 单元格地址 | Text | 否 |  | 仅用于 writeData | 类似于“D5”这样的单元格位置名称。或在下方使用行序号和单元格序号指定（两种二选一）。 |
| names | 名称数据 | Text | 否 |  | 仅用于 addNames | JSON格式的名称数据定义，详细请参考文档。 |
| createSheetIfNotExist |  |  | 否 |  | 仅用于 getRow, getCell, batchReplace, setCell, writeData, mergeCells, setStyle, freezePane, autoFilter, getCellByValue |  |
|  | 工作簿对象 | Object | 否 |  | =自动（根据值的类型判断） | 需要操作的工作簿对象 |
| writeTitleRow | 写入标题行 | Boolean | 否 | true | 仅用于 writeData | 是否输出标题行 |
| cellIndex | 列序号 | Integer | 否 | 0 | 仅用于 getCell, setCell, freezePane | 单元格在所在行里的序号，从0开始 |
| readDataMap |  |  | 否 |  | 仅用于 setCell, getCellByValue |  |
| dataFormat | 数据格式 | Text | 否 |  | 仅用于 setCell | 设置单元格的DataFormat |
| cellLink | 链接 | Text | 否 |  | 仅用于 setCell | 可以为网址、邮件地址(mailto:who@domain.com)、工作表名称、文件路径 |
| replaceDict | 替换数据词典 | Dict | 否 |  | 仅用于 batchReplace | 词典格式数据。键为要查找的字段，值为要填充的内容。 |
| replacePrefixSuffix | 占位符前后缀 | Text | 否 | {{\r\n}} | 仅用于 batchReplace | 第一行写前缀，第二行写后缀。“前缀+字段名+后缀”组成要查找和替换的目标，如“{{姓名}}”。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| workbook | 工作簿对象 | Object | 仅用于 load, newWorkbook | 用于在后续步骤中继续操作工作簿。 |
|  |  | Integer | 仅用于 load |  |
| worksheetNameList | 工作表名称列表 | List | 仅用于 load | 工作簿中的工作表名列表。 |
| sheet | 工作表对象 | Object | 仅用于 load, getSheetByIndex, getSheetByName, getSheet, createSheet | 返回指定的工作表。加载文件时返回工作簿中的第一个工作表对象 |
| firstRow | 首行序号 | Integer | 仅用于 load, getSheetByIndex, getSheetByName, getSheet, getCellByValue | 工作表首行序号（从0开始）。 |
| lastRow | 末行序号 | Integer | 仅用于 load, getSheetByIndex, getSheetByName, getSheet | 工作表有内容的最后一行序号（从0开始）。 |
| firstCellNum | 首个单元格的列序号 | Integer | 仅用于 getRow, getCellByValue | 一行的首列序号（从0开始）。获取工作表信息时， |
| lastCellNum | 末个单元格的列序号 | Integer | 仅用于 getRow | 一行的最后一个单元格的序号（从0开始）。 |
| dictData | 数据词典 |  |  | 从工作簿加载的数据 |
| cellValue | 值 | Any | 仅用于 getCell | 单元格的值 |
|  | 文本值 | Text | 仅用于 getCell | 文本格式的单元格内容 |
| cellType | 类型 | Text | 仅用于 getCell | 单元格的类型 |
| cellFormula | 公式 | Text | 仅用于 getCell | 单元格的公式值 |
| cellDataFormatString | 数据格式字符串 | Text | 仅用于 getCell | 数据格式的字符串表示 |
| names | 名称数据 | Dict | 仅用于 readData | 工作簿中定义的名称数据，返回json格式 |
| cellAddress | 单元格地址 | Object | 仅用于 getCellByValue | 查找到的单元格地址 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- 部分参数偏向变量模式。此类参数实际写入时应优先填写 `VarKey`。
- 带 `TextTools` 的参数在编辑器里通常有选择器辅助，但 JSON 本体仍只写 `VarKey` / `Value`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
