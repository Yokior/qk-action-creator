# WebView2浏览器窗口

- 模块键: `sys:webview2`
- 步骤类型: `Action`
- 说明: 基于微软Edge浏览器内核的组件，需要安装Edge最新预览版方可使用。
- 帮助: https://getquicker.net/KC/Help/Doc/webview2

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:webview2",
  "InputParams": {
    "type": {
      "VarKey": "",
      "Value": "OpenUrl"
    },
    "url": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "userAgent": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "winLocation": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "virtualHostToFolder": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "defaultBgColor": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "additionalBrowserArguments": {
      "VarKey": "",
      "Value": ""
    },
    "modeForExists": {
      "VarKey": "",
      "Value": "SkipThisStep"
    },
    "script": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "sendMessage": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "winSize": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "defaultDownloadFolderPath": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "profileName": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "topMost": {
      "VarKey": "",
      "Value": "false"
    },
    "showInTaskbar": {
      "VarKey": "",
      "Value": "true"
    },
    "noActivate": {
      "VarKey": "",
      "Value": "false"
    },
    "closeWhenLostFocus": {
      "VarKey": "",
      "Value": "false"
    },
    "escCloseWindow": {
      "VarKey": "",
      "Value": "false"
    },
    "showToolbar": {
      "VarKey": "",
      "Value": "false"
    },
    "windowStyle": {
      "VarKey": "",
      "Value": "normal"
    },
    "clearCookies": {
      "VarKey": "",
      "Value": "false"
    },
    "addDevTool": {
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
    "isInstalled": "out_isInstalled",
    "hWnd": "out_hWnd",
    "webView": "out_webView",
    "lastLocation": "out_lastLocation",
    "currUri": "out_currUri",
    "docTitle": "out_docTitle",
    "sourceCode": "out_sourceCode",
    "cookies": "out_cookies",
    "previewImage": "out_previewImage",
    "isNavCompleted": "out_isNavCompleted",
    "scriptResult": "out_scriptResult"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| type | 操作类型 | Enum | 否 | OpenUrl | OpenUrl=打开网页 / OpenAndWaitLoad=打开网页并等待加载完成 / OpenUrlAndWaitClose=打开网页并等待窗口关闭 / SendMessage=发送消息 / ExecuteScript=执行脚本 / CheckWindowState=获取窗口状态 / Close=关闭窗口(如果尚未关闭) / Reload=重新加载/刷新 / Stop=停止加载 / CheckInstalled=检查是否安装WebView2 / MultiTab_OpenUrl=【多标签】打开网址 / MultiColumn_OpenUrl=【多列】打开网址 |  |
| url | 网址或HTML内容 | Text | 是 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose | 网页地址/文件路径或html代码内容 |
|  |  | List | 是 |  | 仅用于 MultiTab_OpenUrl, MultiColumn_OpenUrl |  |
|  |  | Text | 否 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| userAgent | User Agent | Text | 否 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose, MultiTab_OpenUrl, MultiColumn_OpenUrl | 可选。自定义UserAgent |
| winLocation | 附加的浏览器参数 | Text | 是 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose, MultiTab_OpenUrl, MultiColumn_OpenUrl | 用于设置代理等用途 |
| virtualHostToFolder | 虚拟主机映射 | Text | 是 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose | 将文件夹映射为虚拟主机名。格式：主机名|文件夹路径。多个时，每行一个。\r\n在html中可以使用https://servername/path/to/file.png的格式访问文件。 |
| defaultBgColor | 默认背景色 | Text | 否 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose | 可选。设置窗口的默认背景色。 |
| additionalBrowserArguments |  |  | 否 |  | 不用于 CheckInstalled |  |
| modeForExists | 如果窗口已存在 | Enum | 否 | SkipThisStep | SkipThisStep=跳过此步骤 / UpdateUrl=更新网址 / UpdateUrlAndPosition=更新网址和窗口位置 / RecreateWindow=关闭并重建窗口 / BringToFront=激活窗口；仅用于 OpenUrl, OpenAndWaitLoad |  |
| script | JS脚本 | Text | 是 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose, ExecuteScript | 可选。 |
| sendMessage | 消息内容 | Text | 是 |  | 仅用于 SendMessage | Json格式的消息内容。词典变量会自动转换成json。 |
|  |  | Enum | 否 | ShowWindowLocation.CenterScreen | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose, MultiTab_OpenUrl, MultiColumn_OpenUrl | 在哪里显示选择窗口 |
| winSize | 窗口尺寸/位置 | Text | 否 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose, MultiTab_OpenUrl, MultiColumn_OpenUrl | 设置选择窗口的尺寸，格式为：宽度,高度。支持像素数值或屏幕宽高百分比，详情请参考模块文档。\n“窗口位置” 类型为 “自定义位置” 时用于指定显示位置，格式为：left,top,right,bottom |
| defaultDownloadFolderPath | 默认下载文件夹 | Text | 否 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose, MultiTab_OpenUrl, MultiColumn_OpenUrl | 默认的文件下载存储目录 |
| profileName | Profile | Text | 否 |  | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose | 当需要同时登录一个网站的多个账号时，可以创建独立的Profile |
| topMost | 置顶显示 | Boolean | 否 | false | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose, MultiTab_OpenUrl, MultiColumn_OpenUrl |  |
| showInTaskbar | 显示任务栏图标 | Boolean | 否 | true | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| noActivate | 不占用焦点 | Boolean | 否 | false | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose | 不占用焦点时也无法在窗口中输入文字 |
| closeWhenLostFocus | 失去焦点后 | Enum | 否 | false | false=不执行操作 / true=关闭窗口 / hide=隐藏窗口 / minimize=最小化窗口 / close_if_not_topmost=如果未置顶，关闭窗口 / hide_if_not_topmost=如果未置顶，隐藏窗口 / minimize_if_not_topmost=如果未置顶，最小化窗口；仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| escCloseWindow | 按Esc关闭窗口 | Boolean | 否 | false | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| showToolbar | 显示工具栏 | Boolean | 否 | false | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| windowStyle | 窗口风格 | Enum | 否 | normal | normal=正常 / none=无边框；仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| clearCookies | 关闭窗口时清理Cookie | Boolean | 否 | false | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| addDevTool | 添加DevTools桥 | Boolean | 否 | false | 仅用于 OpenUrl, OpenAndWaitLoad, OpenUrlAndWaitClose |  |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功。获取窗口信息时，窗口是否存在。 |
| isInstalled | 是否安装WebView2 | Boolean | 仅用于 CheckInstalled |  |
| hWnd | 窗口句柄 | Integer | 仅用于 OpenUrl, OpenAndWaitLoad, CheckWindowState |  |
| webView | WebView2对象 | Object | 仅用于 OpenUrl, OpenAndWaitLoad, CheckWindowState | 可用于在C#脚本中使用，需运行在UI线程中。注意避免循环引用。 |
| lastLocation | 窗口位置 | Text | 仅用于 OpenAndWaitLoad, CheckWindowState, OpenUrlAndWaitClose | 返回窗口坐标范围。格式为：left,top,right,bottom |
| currUri | 当前网址 | Text | 仅用于 OpenAndWaitLoad, CheckWindowState | 浏览器当前网址 |
| docTitle | 网页标题 | Text | 仅用于 OpenAndWaitLoad, CheckWindowState |  |
| sourceCode | 网页代码 | Text | 仅用于 OpenAndWaitLoad, CheckWindowState |  |
| cookies | Cookie | Text | 仅用于 OpenAndWaitLoad, CheckWindowState |  |
| previewImage | 预览图 | Image | 仅用于 CheckWindowState |  |
| isNavCompleted | 导航是否已结束 | Boolean | 仅用于 CheckWindowState | 是否已完成网页加载过程 |
| scriptResult | 脚本运行结果 | Text | 仅用于 ExecuteScript | json编码的脚本运行结果内容 |

## 要点
- 控制参数: `type`。先定控制参数，再看其余参数是否生效。
- 带 `TextTools` 的参数在编辑器里通常有选择器辅助，但 JSON 本体仍只写 `VarKey` / `Value`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
