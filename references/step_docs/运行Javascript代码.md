# 运行Javascript代码

- 模块键: `sys:jsscript`
- 步骤类型: `Action`
- 说明: 执行 Javascript 代码片段。代码中应包含主函数 `exec()`。
- 帮助: https://getquicker.net/KC/Help/Doc/jsscript

## 先记结论

- 脚本入口固定写 `function exec(){ ... }`。
- 读取变量用 `quickerGetVar("变量名")`。
- 写回变量用 `quickerSetVar("变量名", 值)`。
- 返回值必须是数字。
- 生成 JSON 时，脚本内容统一写成单个字符串，换行用 `\\r\\n` 转义。
- 不要把“真实换行的多行字符串”直接塞进 JSON 的 `Value`。

## 最小 JSON

```json
{
  "StepRunnerKey": "sys:jsscript",
  "InputParams": {
    "script": {
      "VarKey": "",
      "Value": "//.js 主函数 exec()\\r\\nfunction exec(){\\r\\n    var name = quickerGetVar('text');\\r\\n    quickerSetVar('text', 'Hello, ' + name);\\r\\n    return 0;\\r\\n}\\r\\n"
    },
    "allClr": {
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
    "return": "out_return"
  }
}
```

## 输入参数

| Key | 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| script | 脚本内容 | Text | 是 | 要运行的脚本内容 |
| allClr | 允许访问 .Net 程序集 | Boolean | 否 | 是否允许在 JS 中访问 .Net |
| stopIfFail | 失败后停止 | Boolean | 否 | 失败后是否停止动作 |

## 输出参数

| Key | 名称 | 类型 | 说明 |
| --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean | 操作是否成功 |
| return | 返回值 | Integer | `exec()` 返回的数字 |

## 多行脚本标准写法

JSON 里应写成这样：

```json
{
  "script": {
    "VarKey": "",
    "Value": "//.js 主函数 exec()\\r\\nfunction exec(){\\r\\n    var text = quickerGetVar('text');\\r\\n    quickerSetVar('text', text + '_done');\\r\\n    return 0;\\r\\n}\\r\\n"
  }
}
```

要点：

- 每一行都折成 `\\r\\n`。
- 引号仍按 JSON 规则转义。
- 最后一行也建议保留 `\\r\\n`。

## 变量读写示例

```javascript
//.js 主函数 exec()
function exec(){
    var localName = quickerGetVar("text");
    quickerSetVar("text", "Hello, " + localName);
    return 0;
}
```

## 状态读改写完整示例

下面示例假设动作里已有变量：

- `items_json`：当前状态字符串

思路：

1. 先用别的步骤把动作状态读入 `items_json`。
2. JS 里修改这个 JSON 字符串。
3. 再用别的步骤把修改后的 `items_json` 写回动作状态。

对应 JS 步骤内容：

```javascript
//.js 主函数 exec()
function exec(){
    var raw = quickerGetVar("items_json");
    if(!raw){
        raw = "[]";
    }

    var list = JSON.parse(raw);
    list.push({
        title: "新项",
        time: "2026-05-13"
    });

    quickerSetVar("items_json", JSON.stringify(list));
    return 0;
}
```

对应 JSON 片段：

```json
{
  "StepRunnerKey": "sys:jsscript",
  "InputParams": {
    "script": {
      "VarKey": "",
      "Value": "//.js 主函数 exec()\\r\\nfunction exec(){\\r\\n    var raw = quickerGetVar('items_json');\\r\\n    if(!raw){\\r\\n        raw = '[]';\\r\\n    }\\r\\n    var list = JSON.parse(raw);\\r\\n    list.push({ title: '新项', time: '2026-05-13' });\\r\\n    quickerSetVar('items_json', JSON.stringify(list));\\r\\n    return 0;\\r\\n}\\r\\n"
    },
    "allClr": {
      "VarKey": "",
      "Value": "false"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "return": "脚本返回值"
  }
}
```

## 什么时候用 JS

适合：

- 只是轻量字符串处理。
- 已知 `quickerGetVar` / `quickerSetVar` 就够用。
- 只改变量，不访问 Quicker 内部服务。

不适合：

- 需要 `ReadState` / `WriteState` / `RunSp` 这类内部上下文能力。
- 需要直接操纵 Quicker 内部运行时对象。
- 需要复杂对象构造且内置步骤难以覆盖。

## 生成规则

- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。
- 直接写脚本正文时用 `Value`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
