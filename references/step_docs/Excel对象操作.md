# Excel对象操作

- 模块键: `sys:excelObjects`
- 步骤类型: `Action`
- 说明: 操作Excel的某个对象
- 帮助: https://getquicker.net/KC/Help/Doc/excelobjects

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:excelObjects",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "ApplicationInfo"
    },
    "path": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "workbook": {
      "VarKey": "",
      "Value": ""
    },
    "params": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "activeWorkbook": "out_activeWorkbook",
    "activeSheet": "out_activeSheet",
    "worksheetNames": "out_worksheetNames",
    "worksheets": "out_worksheets",
    "workbookPath": "out_workbookPath",
    "application": "out_application"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| operation | 操作类型 | Enum | 是 |  | ApplicationInfo=获取当前Excel应用信息 / OpenFile=工作簿: 打开工作簿 / SaveWorkbook=工作簿: 保存工作簿 / CloseWorkbook=工作簿: 关闭工作簿 / CreateWorkbook=工作簿: 创建工作簿 / SelectWorksheet=工作表：选择工作表 | 操作类型 |
| path | 文件/模板路径 | Text | 否 |  | 仅用于 OpenFile, SaveWorkbook, CreateWorkbook | 完整路径。创建工作簿时，用于指定模板文件。 |
| workbook | 工作簿对象 | Object | 否 |  | 仅用于 SaveWorkbook, CloseWorkbook, SelectWorksheet | 根据具体操作，可用参数不同。请参考文档。 |
| params | 参数 | Text | 否 |  |  | 根据具体操作，可用参数不同。请参考文档。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| activeWorkbook | 活动工作簿 | Object | 仅用于 ApplicationInfo, OpenFile, CreateWorkbook | ActiveWorkbook |
| activeSheet | 活动工作表 | Object | 仅用于 ApplicationInfo, OpenFile, CreateWorkbook | ActiveSheet |
| worksheetNames | 工作表名称的列表 | List | 仅用于 ApplicationInfo, OpenFile | Worksheets |
| worksheets | 工作表对象列表 | Object | 仅用于 ApplicationInfo, OpenFile, CreateWorkbook | Worksheets |
| workbookPath | 工作簿路径 | Text | 仅用于 ApplicationInfo | Worksheets |
| application | Application对象 | Object | 仅用于 ApplicationInfo, OpenFile, CreateWorkbook | Application对象的引用 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
