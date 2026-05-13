# SMTP发送邮件

- 模块键: `sys:smtp`
- 步骤类型: `Action`
- 说明: 使用SMTP协议发送邮件
- 帮助: https://getquicker.net/KC/Help/Doc/smtp

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:smtp",
  "InputParams": {
    "server": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "port": {
      "VarKey": "",
      "Value": "25"
    },
    "useSsl": {
      "VarKey": "",
      "Value": "false"
    },
    "account": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "password": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "sender": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "senderName": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "to": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "cc": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "bcc": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "subject": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "content": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "attachList": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "isHtml": {
      "VarKey": "",
      "Value": "false"
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
| server | 邮件服务器 | Text | 是 |  |  | 邮件服务器的域名或IP |
| port | 端口 | Integer | 是 | 25 |  | Smtp端口号 |
| useSsl | 使用加密连接 | Boolean | 否 | false |  | 是否使用TLS连接（通常为587端口）。 |
| account | 帐号 | Text | 是 |  |  | 发信帐号 |
| password | 密码 | Text | 是 |  |  | 发信帐号的密码 |
| sender | 发信邮箱 | Text | 是 |  |  | 发信帐号所对应的Email地址 |
| senderName | 发件人名称 | Text | 是 |  |  | 发件人的显示名称（可选） |
| to | 收件人 | Text | 是 |  |  | 收件人Email地址，多个的话使用小写逗号分隔。 |
| cc | 抄送 | Text | 是 |  |  | 抄送给的Email地址列表，多个的话使用小写逗号分隔。 |
| bcc | 密送 | Text | 是 |  |  | 密送给的Email地址列表，多个的话使用小写逗号分隔。 |
| subject | 邮件主题 | Text | 是 |  |  | 邮件的主题 |
| content | 邮件正文 | Text | 否 |  |  | 邮件正文内容 |
| attachList | 附件 | Text | 否 |  |  | 附件文件列表。多个时每行一个。 |
| isHtml | 内容为html | Boolean | 否 | false |  | 邮件内容是否为HTML格式 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
