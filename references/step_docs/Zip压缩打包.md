# Zip压缩打包

- 模块键: `sys:zip`
- 步骤类型: `Action`
- 说明: Zip压缩或解压缩
- 帮助: https://getquicker.net/KC/Help/Doc/zip

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:zip",
  "InputParams": {
    "type": {
      "VarKey": "",
      "Value": "Zip"
    },
    "sourcePath": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "targetZipFile": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "sourceZipFile": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "keepBaseFolder": {
      "VarKey": "",
      "Value": "false"
    },
    "outputPath": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "password": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "comment": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "level": {
      "VarKey": "",
      "Value": "1"
    },
    "overwrite": {
      "VarKey": "",
      "Value": "false"
    },
    "skipOverwriteError": {
      "VarKey": "",
      "Value": "false"
    },
    "showProgress": {
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
    "resultPath": "out_resultPath"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| type | 操作类型 | Enum | 否 | Zip | Zip=创建Zip文件 / Unzip=解压缩Zip文件 |  |
| sourcePath | 源路径 | Text | 是 |  | 仅用于 Zip | 待压缩的文件夹或文件路径。多个文件时每个文件一行。 |
| targetZipFile | Zip文件路径 | Text | 是 |  | 仅用于 Zip | 压缩时：目标文件的路径。留空时自动生成临时文件。点(.)表示待压缩的文件夹或文件所在位置。 |
| sourceZipFile | Zip文件路径 | Text | 是 |  | 仅用于 Unzip | 待解压的文件路径。 |
| keepBaseFolder | 源路径为单个文件夹时，压缩整个文件夹（保留文件夹名称） | Boolean | 否 | false | 仅用于 Zip |  |
| outputPath | 目标路径 | Text | 是 |  | 仅用于 Unzip | 解压缩的目标路径, 点(.)表示zip文件所在的文件夹, 星(*)表示以zip文件名创建的子文件夹。 |
| password | 密码 | Text | 否 |  |  | 压缩文件密码 |
| comment | 备注 | Text | 否 |  | 仅用于 Zip | 压缩文件注释内容 |
| level | 级别 | Integer | 否 | 1 | 仅用于 Zip | 压缩级别，0-9。0表示不压缩（速度快），9表示压缩到最小（速度慢） |
| overwrite | 自动覆盖文件 | Boolean | 否 | false | 仅用于 Unzip |  |
| skipOverwriteError | 覆盖失败时忽略 | Boolean | 否 | false | 仅用于 Unzip | 忽略掉无法覆盖的情况 |
| showProgress | 显示进度条 | Boolean | 否 | false | 仅用于 Unzip, Zip | 仅支持解压缩或压缩单个文件夹。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| resultPath | 结果路径 | Text |  | 生成的zip文件完整路径，或解压缩后的完整路径 |

## 要点
- 控制参数: `type`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
