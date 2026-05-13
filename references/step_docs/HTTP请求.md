# HTTP请求

- 模块键: `sys:http`
- 步骤类型: `Action`
- 说明: 发送HTTP请求，并获取返回结果
- 帮助: https://getquicker.net/KC/Help/Doc/http

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:http",
  "InputParams": {
    "url": {
      "VarKey": "",
      "Value": "https://"
    },
    "method": {
      "VarKey": "",
      "Value": "GET"
    },
    "header": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "cookie": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "body": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "contentType": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "resultType": {
      "VarKey": "",
      "Value": "Text"
    },
    "ua": {
      "VarKey": "",
      "Value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    },
    "expireSeconds": {
      "VarKey": "",
      "Value": "100"
    },
    "noAutoRedirect": {
      "VarKey": "",
      "Value": "false"
    },
    "showProgress": {
      "VarKey": "",
      "Value": "false"
    },
    "skipCertVerify": {
      "VarKey": "",
      "Value": "false"
    },
    "forceProxy": {
      "VarKey": "",
      "Value": "false"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    },
    "useSSE": {
      "VarKey": "",
      "Value": "false"
    },
    "sseSpName": {
      "VarKey": "",
      "Value": "示例文本"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "statusCode": "out_statusCode",
    "respHeaders": "out_respHeaders",
    "respCookies": "out_respCookies",
    "content": "out_content",
    "imgResult": "out_imgResult"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| url | 网址 | Text | 是 | https:// |  | 要打开的网页地址 |
| method | 方法 | Enum | 是 | GET |  | Http请求的类型 |
| header | 请求头 | Text | 否 |  |  | 发送的HttpHeader。每行一个header，格式为Name:Value |
| cookie | Cookie | Text | 否 |  |  | 请求的cookie内容 |
| body | 请求体 | Text | 否 |  | 不用于 GET, HEAD, OPTIONS | Http 请求 BODY。格式要求详见模块帮助。 |
| contentType | 内容类型 | Text | 否 |  | 不用于 GET, HEAD, OPTIONS | 选填。上传内容的ContentType，适用于“单个文件或图片变量（二进制）”或“纯文本” 请求体类型。 |
| resultType | 结果类型 | Enum | 是 | Text | Text=文本 / Image=图片 / File=文件 | Http请求的结果类型 |
| ua | UserAgent | Text | 否 | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 |  |  |
| expireSeconds | 超时时间 | Number | 否 | 100 |  | 请求超时时间（秒数） |
| noAutoRedirect | 禁止重定向 | Boolean | 否 | false |  | 是否禁止自动跳转 |
| showProgress | 显示进度条 | Boolean | 否 | false |  | 是否显示上传下载进度条 |
| skipCertVerify | 忽略HTTPS证书验证 | Boolean | 否 | false |  |  |
| forceProxy | 强制使用代理 | Boolean | 否 | false |  | 即使系统设置中未启用代理，本步骤仍然使用代理访问。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |
| useSSE | 启用SSE流式响应 | Boolean | 否 | false |  | 调用AI接口时使用，通过子程序处理接收到的流式响应内容 |
| sseSpName | SSE流式响应处理子程序 | Text | 否 |  |  | 用于处理接收到的流式响应消息，每次收到调用一次，通过data输入变量接收内容。 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 是否操作成功 |
| statusCode | 状态码 | Integer |  | 返回的http请求状态码 |
| respHeaders | 响应头 | Dict |  | 返回的HTTP响应Headers |
| respCookies | 响应Cookies | Dict |  | 返回的Cookies |
| content | 文本结果 | Text |  | 返回的文本内容 |
| imgResult | 图片结果 | Image |  | 返回的图片内容 |

## 要点
- 控制参数: `method`。先定控制参数，再看其余参数是否生效。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
