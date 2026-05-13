# 基础OCR

- 模块键: `sys:basic-ocr`
- 步骤类型: `Action`
- 说明: 获取图片中的文字
- 帮助: https://getquicker.net/KC/Help/Doc/basic-ocr

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:basic-ocr",
  "InputParams": {
    "operation": {
      "VarKey": "",
      "Value": "QuickerServerOcr"
    },
    "apiKey": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "secretKey": {
      "VarKey": "",
      "Value": ""
    },
    "imgVar": {
      "VarKey": "",
      "Value": ""
    },
    "punctuationType": {
      "VarKey": "",
      "Value": "no"
    },
    "mergeChapter": {
      "VarKey": "",
      "Value": "no"
    },
    "interface": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "options": {
      "VarKey": "",
      "Value": "{}"
    },
    "lang": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "offlineMode": {
      "VarKey": "",
      "Value": "Auto"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "content": "out_content",
    "textList": "out_textList",
    "rawData": "out_rawData",
    "rawObject": "out_rawObject"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| operation | 接口/引擎 | Enum | 是 | QuickerServerOcr | QuickerServerOcr=Quicker OCR引擎 / WindowsOcr=Windows10/11 内置OCR引擎 / baidu-basic=百度通用文字识别（自定义帐号） / baidu-quicker=百度通用文字识别（Quicker帐号） / baidu-custom=百度自定义接口识别（自定义帐号） / table_quicker=表格识别（Quicker服务） | OCR接口或引擎。离线引擎安装方式请参考模块文档。 |
| apiKey | ApiKey | Text | 是 |  | 仅用于 baidu-basic, baidu-custom | 请填写OCR帐号的ApiKey |
| secretKey | SecretKey |  | 否 |  | 仅用于 baidu-basic, baidu-custom |  |
| imgVar | 图片变量 | Image | 是 |  |  | 从指定变量中加载图片 |
| punctuationType | 转换标点符号 | Enum | 是 | no | no=不转换 / sbc=全角符号 / dbc=半角符号；仅用于 baidu-basic, baidu-quicker, QuickerServerOcr | 合并文本时，是否转换标点符号 |
| mergeChapter | 合并段落 | Enum | 是 | no | no=不合并 / merge=合并；仅用于 baidu-basic, baidu-quicker, QuickerServerOcr | 是否智能合并段落。 |
| interface | 接口名称或网址 | Text | 否 |  | general_basic=通用文字识别（标准版） / general=通用文字识别（标准含位置版） / accurate_basic=通用文字识别（高精度版） / accurate=通用文字识别（高精度含位置版） / handwriting=手写文字识别 / numbers=数字识别 / doc_analysis_office=办公文档识别 / form=表格文字识别(同步接口) / qrcode=二维码识别；仅用于 baidu-custom | 接口的完整网址，或 https://aip.baidubce.com/rest/2.0/ocr/v1/ 后面的部分 |
| options | 附加参数 | Dict | 否 |  | 仅用于 baidu-custom | 请参考百度官方/Quicker服务接口说明。每行一个参数，使用option:value的格式。 |
| lang | 语言 | Text | 否 |  | CHN_ENG=中英混合 / ENG=英语 / KOR=韩语 / JAP=日语 / CHT=繁体中文 / LAT=拉丁语 / ARA=阿拉伯语；仅用于 QuickerServerOcr, table_quicker | 待识别内容的语言。表格识别仅支持中英混合和英文。 |
| offlineMode | 离线模式 | Enum | 否 | Auto | Auto=自动 / OnlineOnly=仅使用在线服务 / OfflineOnly=仅使用离线引擎；仅用于 QuickerServerOcr | 是否使用离线引擎。自动：安装离线引擎时使用离线，否则使用在线。 |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| content | 合并后结果 | Text | 仅用于 baidu-basic, baidu-quicker, QuickerServerOcr, WindowsOcr, table_quicker | 合并在一起的的文本内容 |
| textList | 行列表 | List | 仅用于 baidu-basic, baidu-quicker, QuickerServerOcr, WindowsOcr | OCR识别结果，列表格式，每行一项。 |
| rawData | 原始结果 | Text |  | API接口返回的完整内容 |
| rawObject | 原始结果JObject对象 | Object | 仅用于 baidu-basic, baidu-quicker, baidu-custom | 返回结果的JObject对象 |

## 要点
- 控制参数: `operation`。先定控制参数，再看其余参数是否生效。
- 部分参数偏向变量模式。此类参数实际写入时应优先填写 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
