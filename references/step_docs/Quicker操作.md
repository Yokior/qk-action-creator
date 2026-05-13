# Quicker操作

- 模块键: `sys:quickeroperations`
- 步骤类型: `Action`
- 说明: 调用Quicker的某个功能
- 帮助: https://getquicker.net/KC/Help/Doc/quickeroperations

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:quickeroperations",
  "InputParams": {
    "type": {
      "VarKey": "",
      "Value": "showPanel"
    },
    "profileId": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "actionId": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "position": {
      "VarKey": "",
      "Value": "200,200"
    },
    "exe": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "activatePointWindow": {
      "VarKey": "",
      "Value": "0"
    },
    "followMousePosition": {
      "VarKey": "",
      "Value": "true"
    },
    "searchText": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "skinId": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "theme": {
      "VarKey": "",
      "Value": ""
    },
    "viewMode": {
      "VarKey": "",
      "Value": "ViewMode.ByProcess"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "actionList": "out_actionList",
    "actionTitle": "out_actionTitle",
    "actionIcon": "out_actionIcon",
    "windowHandle": "out_windowHandle"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| type | 类型 | Enum | 是 | showPanel | showPanel=显示面板 / showSearch=显示搜索框 / closeSearch=关闭搜索框 / showCircleMenu=显示轮盘菜单 (点击) / togglePause=禁用/启用 / runLastAction=运行最后使用的动作 / startAppVoiceInput=启动App语音输入 / stopAllActions=停止运行中的动作 / reinstallMouseHook=重新加载键鼠挂钩 / ResetKeyboard=重置键盘状态 / showDashboardWindow=显示仪表盘窗口 / toggleTextFloatWindow=开启/关闭文本悬浮窗功能 / showConfigWindow=显示设置窗口 / showExeSettingWindow=显示场景与动作管理窗口 / closeAllFloatWindow=关闭所有悬浮按钮 / loadProfile=加载动作页 / loadExeProfiles=加载指定应用程序的所有动作页（锁定切换） / loadExeProfilesNoLock=加载指定应用程序的所有动作页（不锁定切换） / ToggleLockPanel=锁定/解锁 动作页自动切换 / editAction=编辑动作 / RestartQuicker=重启Quicker / SetPushActiveClient=推送服务：设置为活动客户端 / StartSearchWithAction=使用当前动作进行实时搜索 / SearchWithCertainAction=使用指定动作进行实时搜索 / operation_show_context_menu=显示剪贴板上下文菜单 / LoadSkin=加载外观/切换主题(专业版功能) / ExitQuicker=退出Quicker / FloatAction=悬浮动作(专业版功能) / ToggleFloatButtons=切换所有悬浮按钮显示 / ShowHideImageWindows=显示或隐藏所有图片窗口 / RemoveAction=删除当前动作 / GetActionInfo=根据ID获取动作信息 | 操作类型 |
| profileId | 动作页ID | Text | 是 |  | 仅用于 loadProfile | 请在场景与动作管理中，查看动作页信息获取ID。 |
| actionId | 动作ID或名称 | Text | 是 |  | 仅用于 editAction, SearchWithCertainAction, FloatAction, GetActionInfo | 在动作上点右键->信息可以查看动作信息。使用名称时不能有重名动作。获取动作信息时仅可填写动作Id。编辑动作时，使用%%id或%%name格式，可用于编辑公共子程序。 |
| position | 位置 | Text | 是 | 200,200 | 仅用于 FloatAction | 坐标，格式为：left,top |
| exe | 场景标识 | Text | 是 |  | 仅用于 loadExeProfiles, loadExeProfilesNoLock, showCircleMenu, GetActionList, showExeSettingWindow, showDashboardWindow | 场景关联的exe文件名。请参考场景与动作管理窗口左侧应用列表。 |
| activatePointWindow | 自动激活鼠标位置窗口 | Boolean | 否 | 0 | 仅用于 showPanel |  |
| followMousePosition | 跟随鼠标位置 | Boolean | 否 | true | 仅用于 showPanel |  |
| searchText | 预置的搜索内容 | Text | 否 |  | 仅用于 StartSearchWithAction, showSearch, SearchWithCertainAction | 预先放入搜索框的内容 |
| skinId | 外观ID | Text | 是 |  | 仅用于 LoadSkin | 请在外观网页中复制外观ID |
| theme | 主题模式 | Enum | 否 |  | =不改变 / auto=跟随Windows / light=浅色 / dark=暗色 / toggle=切换浅色和暗色；仅用于 LoadSkin | 可选切换为浅色或暗色模式 |
| viewMode | 显示状态 | Enum | 否 | ViewMode.ByProcess | ToggleHideAndAuto=切换隐藏和自动；仅用于 ToggleFloatButtons |  |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 步骤是否成功 | Boolean |  | 步骤是否成功完成 |
| actionList | 动作列表 | List | 仅用于 GetActionList |  |
| actionTitle | 动作标题 | Text | 仅用于 GetActionInfo |  |
| actionIcon | 动作图标 | Text | 仅用于 GetActionInfo |  |
| windowHandle | 窗口句柄 | Integer | 仅用于 FloatAction |  |

## 要点
- 控制参数: `type`。先定控制参数，再看其余参数是否生效。
- 带 `TextTools` 的参数在编辑器里通常有选择器辅助，但 JSON 本体仍只写 `VarKey` / `Value`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
