# Websocket

- 模块键: `sys:websocket`
- 步骤类型: `Action`
- 说明: Websocket相关操作
- 帮助: https://getquicker.net/KC/Help/Doc/websocket

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:websocket",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "CreateClient"
    },
    "content": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "clientId": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "spName": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "account": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "origin": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "callbackOnClose": {
      "VarKey": "",
      "Value": "true"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "isConnected": "out_isConnected"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| operation | 操作类型 | Enum | 否 | CreateClient | CreateClient=客户端：连接到Websocket服务 / SendMsgToServer=客户端：向Websocket服务发送消息 / GetClientState=客户端：获取连接状态 / CloseClient=客户端：关闭连接 / SendTextToClient=服务器：向连接的客户端发送文本 / SendFileToClient=服务器：向连接的客户端发送文件(二进制方式) / SendFileToClientBase64=服务器：向连接的客户端发送文件(Base64方式) |  |
| content | 消息内容 | Text | 否 |  | 仅用于 CreateClient |  |
| clientId | 连接ID | Text | 否 |  | 仅用于 CreateClient, SendMsgToServer, GetClientState, CloseClient | 用于区分不同的客户端连接。连接相同id的客户端时，前一个连接会被自动关闭。 |
| spName | 消息处理子程序 | Text | 否 |  | 仅用于 CreateClient | 使用子程序处理从websocket服务接收到的消息。详情请参考文档。 |
| account | 账号密码 | Text | 否 |  | 仅用于 CreateClient | 支持Basic和Digest认证方式。多行填写。第一行写账号，第二行写密码。 |
| origin | Origin | Text | 否 |  | 仅用于 CreateClient | 仅需要时填写 |
| callbackOnClose | 服务断开时通知动作(调用动作并传入参数:websocket__closed) | Boolean | 否 | true | 仅用于 CreateClient | 是否等待服务器响应 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| isConnected | 是否连接 | Boolean | 仅用于 GetClientState | 指定客户端是否连接到远程服务器 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
