# AI 调用

- 模块键: `sys:ai`
- 步骤类型: `Action`
- 说明: 调用第三方AI服务
- 帮助: https://getquicker.net/KC/Help/Doc/ai

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:ai",
  "InputParams": {
    "endpoint": {
      "VarKey": "",
      "Value": "chat"
    },
    "model": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "systemPrompt": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "suffix": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "topP": {
      "VarKey": "",
      "Value": "1"
    },
    "apiKey": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "apiOrg": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "maxTokens": {
      "VarKey": "",
      "Value": "0"
    },
    "temperature": {
      "VarKey": "",
      "Value": "0.2"
    },
    "prompt": {
      "VarKey": "",
      "Value": ""
    },
    "n": {
      "VarKey": "",
      "Value": "1"
    },
    "stream": {
      "VarKey": "",
      "Value": "false"
    },
    "streamTo": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "stop": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "apiUrlFormat": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "expireSeconds": {
      "VarKey": "",
      "Value": "120"
    },
    "respFormat": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "sessionId": {
      "VarKey": "",
      "Value": ""
    },
    "forceProxy": {
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
    "result": "out_result",
    "rawResponse": "out_rawResponse",
    "reasoningContent": "out_reasoningContent",
    "promptTokens": "out_promptTokens",
    "completionTokens": "out_completionTokens",
    "totalTokens": "out_totalTokens",
    "finishReason": "out_finishReason",
    "historyMessages": "out_historyMessages"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| endpoint | 接口端点 | Enum | 是 | chat | chat=Chat / completions=Completions |  |
| model | 模型 | Text | 否 |  |  | 适用于可能适用于不同的端点，请参考官方文档使用。 |
| systemPrompt | 系统提示 | Text | 否 |  | 仅用于 chat | 告知AI所需要扮演的角色和要求。如“你是一个专业的翻译助手”。 |
| suffix | 会话ID | Text | 否 |  | 仅用于 chat | 可选。每次会话请生成新的GUID格式会话ID，设置后将自动保存会话历史。 |
| topP | top_p | Dict | 否 | 1 |  | 用于添加额外的请求参数。请参考文档 |
|  |  |  | 否 |  | 仅用于 chat, completions |  |
| apiKey | APIKey | Text | 否 |  |  |  |
| apiOrg | Orgnization | Text | 否 |  |  | 可选 |
| maxTokens | 最大响应Token数 | Integer | 否 | 0 |  | 提示token数+最大响应token数不能超过模型限制。 |
| temperature | 温度 | Number | 否 | 0.2 |  | 像0.8这样的较高值会使输出更随机（发散/创造性），而像0.2这样的较低值会使其更加专注和确定性。 |
| prompt | 提示 |  | 否 |  | 仅用于 chat, completions |  |
| n | n | Integer | 否 | 1 |  | 对每个问题生成几个结果，将会耗费更多token。 |
| stream | 使用流式输出 | Boolean | 否 | false |  | 即时输出结果，将结果输出到文本窗口，详见文档。此时将无法获得完整响应和token用量等信息。 |
| streamTo | 流式输出窗口标识 | Text | 否 |  |  | 一个预先使用非等待模式显示的文本窗口的标识，流式输出时将结果显示在该窗口中。 |
| stop | 停止符stop | Text | 否 |  |  | 遇到指定的内容时自动停止生成。可使用\\r,\\n,\\t等表示特殊字符。输入多行时，表示多个停止符。 |
| apiUrlFormat | API网址 | Text | 否 |  |  | 可选，使用自定义的API服务器时使用。请参考模块文档了解如何设置。 |
| expireSeconds | 超时秒数 | Number | 否 | 120 |  | 最长等待秒数 |
| respFormat | 响应格式 | Text | 否 |  | =文本 / json_object=JSON对象；仅用于 chat | 留空，或使用“json_object”表示json格式响应，或json格式的完整的response_format内容。 |
| sessionId |  |  | 否 |  | 仅用于 chat |  |
| forceProxy | 强制使用代理 | Boolean | 否 | false |  | 即使系统设置中未启用代理，本步骤仍然使用代理访问。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| result | 生成结果 | Text |  | 生成的结果文本 |
| rawResponse | 原始响应内容 | Text |  | 接口返回的原始响应内容 |
| reasoningContent | 推理内容 | Text |  | 推理模型的reasoning_content |
| promptTokens | 提示Token数 | Integer |  | Prompt耗费的token数量 |
| completionTokens | 响应Token数 | Integer |  | 响应耗费的token数量 |
| totalTokens | 总Token数 | Integer |  | 总耗费的token数量 |
| finishReason | 结束原因 | Text |  |  |
| historyMessages | 历史消息 | Object | 仅用于 chat | 消息类型列表对象 |

## 要点
- 控制参数: `endpoint`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
