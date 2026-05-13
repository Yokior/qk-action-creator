# 提取HTML内容

- 模块键: `sys:htmlExtract`
- 步骤类型: `Action`
- 说明: 从HTML代码中提取内容
- 帮助: https://getquicker.net/KC/Help/Doc/htmlextract

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:htmlExtract",
  "InputParams": {
    "source": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "encoding": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "xpath": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "selectTarget": {
      "VarKey": "",
      "Value": "single"
    },
    "returnType": {
      "VarKey": "",
      "Value": "InnerHtml"
    },
    "attribute": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "writeToSheet": {
      "VarKey": "",
      "Value": ""
    }
  },
  "OutputParams": {
    "value": "out_value",
    "rootNode": "out_rootNode"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| source | 源HTML | Text | 是 |  |  | 原始HTML内容，或网址，或根节点对象 |
| encoding | 网页编码类型 | Text | 否 |  | auto=自动检测 (加载两次) / gb2312=GB2312编码 / utf-8=UTF8编码 | 通过网址加载内容时，使用指定的编码。留空时默认为UTF8。 |
| xpath | 节点XPath | Text | 是 |  |  | 内容的XPath，详细说明请参考文档 |
| selectTarget | 提取方式 | Enum | 否 | single | single=第一个符合条件的节点 / all=所有符合条件的节点 | 提取单个节点还是符合条件的所有节点。 |
| returnType | 提取内容类型 | Enum | 否 | InnerHtml | InnerHtml=innerHtml 内部HTML / InnerText=innerText 内部文本 / OuterHtml=outerHTML 节点全部HTML / Attribute=Attribute 节点的某个属性 / Node=节点对象 | 要提取的节点信息。 |
| attribute | 属性名称 | Text | 否 |  |  | 仅在提取节点属性时有效。指定属性的名称。 |
| writeToSheet | 写入工作表对象 | Object | 否 |  |  | 将提取到的表格内容写入工作表对象中。 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| value | 提取值 | Any |  | 提取的内容。请确保结果类型和变量类型匹配。 |
| rootNode | 根节点 | Any |  | 整个HTML源内容对应的HtmlNode节点对象，可用于后续处理使用。 |

## 要点
- 部分参数偏向变量模式。此类参数实际写入时应优先填写 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
