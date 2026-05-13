# HTTP服务器

- 模块键: `sys:httpserver`
- 步骤类型: `Action`
- 说明: 创建临时的本地HTTP服务器，从而可以从移动端或其它设备访问。
- 帮助: https://getquicker.net/KC/Help/Doc/httpserver

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:httpserver",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "CreateFileServer"
    },
    "headCode": {
      "VarKey": "",
      "Value": ""
    },
    "enableHttps": {
      "VarKey": "",
      "Value": "1"
    },
    "port": {
      "VarKey": "",
      "Value": "8080"
    },
    "showNotifyWhenAutoClose": {
      "VarKey": "",
      "Value": ""
    },
    "password": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "serviceId": {
      "VarKey": "",
      "Value": "default"
    },
    "docPath": {
      "VarKey": "",
      "Value": "false"
    },
    "defaultDoc": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "bodyCode": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "customRequest": {
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
    "serverUrl": "out_serverUrl",
    "serverUrlWithAccount": "out_serverUrlWithAccount",
    "isRunning": "out_isRunning",
    "serverList": "out_serverList"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| operation | 操作类型 | Enum | 否 | CreateFileServer | CreateFileServer=创建文件服务器 / CloseServer=关闭服务 / GetServerState=获取服务状态 |  |
| headCode |  |  | 否 |  | 仅用于 CreateFileServer |  |
| enableHttps | 启用HTTPS | Boolean | 否 | 1 | 仅用于 CreateFileServer |  |
| port | 端口号 | Boolean | 否 | 8080 | 仅用于 CreateFileServer | 服务端口号。值为0时自动生成端口号。 |
| showNotifyWhenAutoClose | 自动关闭时显示通知 |  | 否 |  |  |  |
| password | 基础验证密码 | Text | 否 |  | 仅用于 CreateFileServer | Basic验证的密码，账号固定为quicker |
| serviceId | 服务ID | Text | 否 | default |  | 通过服务ID启动或关闭服务 |
| docPath | 文件夹路径 | Number | 否 | false | 仅用于 CreateFileServer | 闲置超时关闭时，是否显示通知。 |
| defaultDoc | 默认文档 | Text | 否 |  |  | 可选，如index.html。 |
| bodyCode | BODY插入代码 | Text | 否 |  | 仅用于 CreateFileServer | 向目录HTML文档的BODY中插入代码，可用于自定义脚本。 |
| customRequest | 自定义请求处理 | Text | 否 |  | 仅用于 CreateFileServer | 每行一条规则，格式为：“路径:HTTP方法:子程序名”。详细信息请参考模块文档。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| serverUrl | 服务地址 | Text | 仅用于 CreateFileServer | 服务网址 |
| serverUrlWithAccount | 带账号的地址 | Text | 仅用于 CreateFileServer | 带有账号密码的地址。可用于扫码后自动登录。 |
| isRunning | 是否在运行 | Boolean | 仅用于 GetServerState | 指定ID的web服务是否在运行中 |
| serverList | 运行中的服务列表 | List | 仅用于 GetServerState | 所有运行中的服务的列表 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
