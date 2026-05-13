# 窗口界面控制(FlaUI)

- 模块键: `sys:flauiautomation`
- 步骤类型: `Action`
- 说明: 触发Windows窗口的菜单/按钮等控件(通过FlaUI库实现)。
- 帮助: https://getquicker.net/KC/Help/Doc/uiautomation

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:flauiautomation",
  "InputParams": {
    "type": {
      "VarKey": "",
      "Value": "TriggerMenu"
    },
    "window": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "expandDelay": {
      "VarKey": "",
      "Value": "200"
    },
    "controlType": {
      "VarKey": "",
      "Value": "0"
    },
    "controlOperation": {
      "VarKey": "",
      "Value": "Auto"
    },
    "value": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "pointLocation": {
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
    "value": "out_value",
    "controlText": "out_controlText",
    "rect": "out_rect",
    "controlName": "out_controlName",
    "controlType": "out_controlType",
    "controlXPath": "out_controlXPath",
    "controlTypeId": "out_controlTypeId",
    "controlInfo": "out_controlInfo",
    "controlIsEnabled": "out_controlIsEnabled",
    "controlIsVisible": "out_controlIsVisible",
    "element": "out_element"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| type | 操作类型 | Enum | 否 | TriggerMenu | TriggerMenu=触发窗口菜单 / TriggerControl=触发窗口控件 / GetControlInfo=获取窗口控件信息 / GetCursorPointControlInfo=获取鼠标指针位置控件信息 / GetControlInfoByPosition=获取指定位置控件信息 / GetFocusedControlInfo=获取焦点控件信息 | 操作类型。按下和抬起需要配对使用。 |
| window | 窗口句柄 | Text | 否 |  | 仅用于 TriggerMenu, TriggerControl, GetControlInfo | 要操作哪个窗口的控件。不填写=使用前台窗口；或窗口句柄数字。 |
| expandDelay | 展开延时 | Integer | 否 | 200 | 仅用于 TriggerMenu | 等待下级菜单展开的时间(ms) |
|  |  | Text | 否 |  | 仅用于 TriggerControl, GetControlInfo | 控件的XPath或Name。XPath以/开始。 |
| controlType | 控件类型 | Enum | 否 | 0 | 0=*任意类型*；仅用于 TriggerControl, GetControlInfo | 可选。当有多个名称相同但类型不同的控件时区分。 |
| controlOperation | 动作 | Enum | 否 | Auto | Auto=自动 / Invoke=调用（按钮、菜单项等） / LeftClick=鼠标左键单击 / MiddleClick=鼠标中键单击 / RightClick=鼠标右键单击 / LeftDoubleClick=鼠标左键双击 / Select=单选：选择（单选框、标签页等） / AddToSelection=多选：添加到多选（多选列表等） / RemoveFromSelection=多选：从多选中移除（多选列表） / ToggleItemSelection=多选：切换选中状态 / Expand=展开折叠：展开（菜单等） / Collapse=展开折叠：折叠（菜单等） / ToggleExpandCollapse=展开折叠：切换展开折叠（菜单等） / Toggle=切换：切换（检查框等） / ToggleOn=切换：开（检查框等） / ToggleOff=切换：关（检查框等） / SetValue=设置值；仅用于 TriggerControl | 对控件执行的操作。 |
| value | 值 | Text | 否 |  | 仅用于 TriggerControl | 仅用于 “设置值” 操作。 |
| pointLocation | 坐标位置 | Text | 否 |  | 仅用于 GetControlInfoByPosition | 指定要检查的控件的屏幕坐标位置，格式为“x,y” |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| value | 值 | Text | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition | 控件的值 |
| controlText | 文本 | Text | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition | 获取控件上的文本。根据控件不同，可能从Value、Text、Name等信息获取。 |
| rect | 位置 | Text | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition | 控件坐标位置 |
| controlName | 控件名称 | Text | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition |  |
| controlType | 控件类型 | Text | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition |  |
| controlXPath | 控件XPath | Text | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition |  |
| controlTypeId | 控件类型ID | Integer | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition |  |
| controlInfo | 其他信息 | Dict | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition |  |
| controlIsEnabled | 是否启用 | Boolean | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition | 控件未处于禁用状态 |
| controlIsVisible | 是否可见 | Boolean | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition | 控件是否在屏幕上。 |
| element | 原始对象 | Object | 仅用于 GetControlInfo, GetCursorPointControlInfo, GetFocusedControlInfo, GetControlInfoByPosition | 返回控件的AutomationElement对象 |

## 要点
- 控制参数: `type`。先定控制参数，再看其余参数是否生效。
- 带 `TextTools` 的参数在编辑器里通常有选择器辅助，但 JSON 本体仍只写 `VarKey` / `Value`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
