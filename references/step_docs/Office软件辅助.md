# Office软件辅助

- 模块键: `sys:officehelper`
- 步骤类型: `Action`
- 说明: 辅助控制Office软件
- 帮助: https://getquicker.net/KC/Help/Doc/officehelper

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:officehelper",
  "InputParams": {
    "appType": {
      "VarKey": "",
      "Value": "word_wps"
    },
    "code": {
      "VarKey": "",
      "Value": "Sub Hello()\\r\\nMsgBox \\\"Hello World\\\"\\r\\nEnd Sub\\r\\n"
    },
    "command": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "formats": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "waitResp": {
      "VarKey": "",
      "Value": "1"
    },
    "waitMs": {
      "VarKey": "",
      "Value": "10000"
    }
  },
  "OutputParams": {
    "resp": "out_resp",
    "progId": "out_progId"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| appType | 应用程序 | Enum | 否 | word_wps | word_wps=Word 或 WPS文字（根据前台进程自动识别） / word=Word / wps=WPS文字 / excel_et=Excel 或 WPS表格（根据前台进程自动识别） / excel=Excel / et=WPS表格 / powerpoint_wpp=PowerPoint 或 WPS幻灯片（根据前台进程自动识别） / powerpoint=PowerPoint / wpp=WPS幻灯片 / outlook=Outlook (支持界面命令) / project=Project (支持界面命令) / visio=Visio (支持界面命令、VBA) |  |
| code | 宏名称或VBA代码 | Text | 否 | Sub Hello()\r\nMsgBox \"Hello World\"\r\nEnd Sub\r\n |  | 宏的名称，或VBA代码（将执行第一个找到的Sub或Function） |
| command | 命令ID | Text | 否 |  |  | 界面按钮所对应的命令ID，请参考模块文档了解如何获取。 |
| formats | 格式设置/属性赋值代码 | Text | 否 |  |  | 请参考文档说明 |
| waitResp | 等待执行结束 | Boolean | 否 | 1 |  | 不等待将立即继续后续步骤的执行，如果遇到异常情况无法获知。 |
| waitMs | 最长等待时间(ms) | Number | 是 | 10000 |  | 最长的等待返回结果的，毫秒数 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| resp | 返回内容 | Text |  |  |
| progId | ProgId | Text |  | 获取程序的ProgId，可用于在C#里得到对应的Application对象。 |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
