# Windows服务和注册表

- 模块键: `sys:winservice`
- 步骤类型: `Action`
- 说明: 获取Windows服务的状态、注册表项信息
- 帮助: https://getquicker.net/KC/Help/Doc/winservice

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:winservice",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "getServiceInfo"
    },
    "name": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "regKeyPath": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "regValueName": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isExists": "out_isExists",
    "displayName": "out_displayName",
    "serviceList": "out_serviceList",
    "regValue": "out_regValue"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| operation | 操作类型 | Enum | 否 | getServiceInfo | getServiceInfo=获取某个服务的信息 / getServiceList=获取Windows服务列表 / getRegValue=获取注册表项值 |  |
| name | 服务名 | Text | 否 |  | 仅用于 getServiceInfo | 服务名称（不是显示名称），大小写敏感。 |
| regKeyPath | 注册表项路径 | Text | 否 |  | 仅用于 getRegValue | 如：HKEY_CURRENT_USER\\Software\\Quicker |
| regValueName | 值名称 | Text | 否 |  | 仅用于 getRegValue | 留空表示“默认”项 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isExists | 是否存在 | Boolean | 仅用于 getServiceInfo, getRegValue | 服务或注册表项是否存在 |
| displayName | 显示名 | Text | 仅用于 getServiceInfo | 服务的显示名 |
| serviceList | 服务名列表 | List | 仅用于 getServiceList |  |
| regValue | 值 | Text | 仅用于 getRegValue | 注册表项的值 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
