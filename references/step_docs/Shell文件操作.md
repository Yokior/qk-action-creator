# Shell文件操作

- 模块键: `sys:shelloperation`
- 步骤类型: `Action`
- 说明: 针对文件的Windows Shell相关操作
- 帮助: https://getquicker.net/KC/Help/Doc/shelloperation

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:shelloperation",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "getverb"
    },
    "pathOrExt": {
      "VarKey": "",
      "Value": ".txt"
    },
    "pathList": {
      "VarKey": "",
      "Value": "item1\\nitem2"
    },
    "verb": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "title": {
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
    "verbs": "out_verbs",
    "titles": "out_titles"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| operation | 操作类型 | Enum | 否 | getverb | getverb=获取文件的可用动词列表(verb) / execverb=对文件执行动词(verb) / gettitles=获取文件的可用菜单标题列表 / execbytitle=对文件执行菜单(指定菜单标题) / showmenu=显示系统上下文菜单 |  |
| pathOrExt | 文件路径或扩展名 | Text | 否 | .txt | 仅用于 getverb, gettitles | 需要获取可用动词的文件类型，可使用扩展名如.txt或提供完整文件名。 |
| pathList | 文件路径列表 | List | 否 |  | 仅用于 execverb, showmenu, execbytitle | 要操作文件的完整路径的列表。每个文件将会被依次调用。 |
| verb | 动词 | Text | 否 |  | open=打开 / edit=编辑 / print=打印 / link=创建快捷方式 / openas=选择打开方式 / copy=复制 / cut=剪切 / delete=删除 / setdesktopwallpaper=设置为桌面背景 / ShellEdit=使用照片编辑 / VSCode=通过VisualStudioCode打开 / 通过QQ发送到我的手机，打开QQ手机版接收。=通过QQ发送到手机；仅用于 execverb | Shell操作动词，需要在当前电脑上支持才能正常运行。 |
| title | 菜单标题 | Text | 否 |  | 仅用于 execbytitle | 菜单上的标题文字，需要准确匹配。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| verbs | 动词列表 | List | 仅用于 getverb | 每项格式为：描述文字|动词 |
| titles | 菜单标题列表 | List | 仅用于 gettitles |  |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- 带 `TextTools` 的参数在编辑器里通常有选择器辅助，但 JSON 本体仍只写 `VarKey` / `Value`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
