# 使用Everything搜索文件

- 模块键: `sys:everythingsearch`
- 步骤类型: `Action`
- 说明: 调用Everything提供的接口搜索文件
- 帮助: https://getquicker.net/KC/Help/Doc/everythingsearch

## 最小 JSON
```json
{
  "StepRunnerKey": "sys:everythingsearch",
  "InputParams": {
    "search": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "folder": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "ext": {
      "VarKey": "",
      "Value": "示例文本"
    },
    "matchWholeFilename": {
      "VarKey": "",
      "Value": "0"
    },
    "matchWholeWord": {
      "VarKey": "",
      "Value": "1"
    },
    "matchPath": {
      "VarKey": "",
      "Value": "0"
    },
    "matchCase": {
      "VarKey": "",
      "Value": "0"
    },
    "useRegex": {
      "VarKey": "",
      "Value": "0"
    },
    "maxCount": {
      "VarKey": "",
      "Value": "100"
    },
    "sort": {
      "VarKey": "",
      "Value": "1"
    },
    "stopIfFail": {
      "VarKey": "",
      "Value": "true"
    }
  },
  "OutputParams": {
    "isSuccess": "out_isSuccess",
    "pathList": "out_pathList",
    "resultCount": "out_resultCount",
    "rawResult": "out_rawResult"
  }
}
```

## 输入参数
| Key | 名称 | 类型 | 必填 | 默认值 | 取值/可见性 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| search | 搜索内容 | Text | 是 |  |  | 要搜索的内容，格式与直接在everything软件中搜索时相同。 |
| folder | 限定目录 | Text | 否 |  |  | 可选。在指定目录下搜索（包含子目录）。 |
| ext | 扩展名 | Text | 否 |  | bat;cmd;exe;msi;msp;scr;cpl=可执行文件 / c;chm;cpp;csv;cxx;doc;docm;docx;dot;dotm;dotx;h;hpp;htm;html;hxx;ini;java;lua;mht;mhtml;odt;pdf;potx;potm;ppam;ppsm;ppsx;pps;ppt;pptm;pptx;rtf;sldm;sldx;thmx;txt;vsd;wpd;wps;wri;xlam;xls;xlsb;xlsm;xlsx;xltm;xltx;xml=文档 / ani;bmp;gif;ico;jpe;jpeg;jpg;pcx;png;psd;tga;tif;tiff;webp;wmf=图片 / 3g2;3gp;3gp2;3gpp;amr;amv;asf;avi;bdmv;bik;d2v;divx;drc;dsa;dsm;dss;dsv;evo;f4v;flc;fli;flic;flv;hdmov;ifo;ivf;m1v;m2p;m2t;m2ts;m2v;m4b;m4p;m4v;mkv;mp2v;mp4;mp4v;mpe;mpeg;mpg;mpls;mpv2;mpv4;mov;mts;ogm;ogv;pss;pva;qt;ram;ratdvd;rm;rmm;rmvb;roq;rpm;smil;smk;swf;tp;tpr;ts;vob;vp6;webm;wm;wmp;wmv=视频文件 / aac;ac3;aif;aifc;aiff;au;cda;dts;fla;flac;it;m1a;m2a;m3u;m4a;mid;midi;mka;mod;mp2;mp3;mpa;ogg;ra;rmi;spc;rmi;snd;umx;voc;wav;wma;xm=音频文件 | 可选。半角分号分隔的扩展名列表。如“txt;docx;xslx;” |
| matchWholeFilename | 匹配完整文件名 | Boolean | 否 | 0 |  | 匹配整个文件名。0表示否，1表示是。 |
| matchWholeWord | 匹配整个单词 | Boolean | 否 | 1 |  | 匹配整个单词。如 quicker.exe 将会匹配：quicker.exe, quicker.exe.config等。0表示否，1表示是。 |
| matchPath | 匹配路径 | Boolean | 否 | 0 |  | 匹配路径的不同部分，而不仅是文件名。 |
| matchCase | 匹配大小写 | Boolean | 否 | 0 |  | 是否大小写敏感。0表示否，1表示是。 |
| useRegex | 使用正则匹配 | Boolean | 否 | 0 |  | 是否使用正则匹配。0表示否，1表示是。 |
| maxCount | 最大结果数量 | Integer | 是 | 100 |  | -1表示不限制 |
| sort | 排序方式 | Enum | 是 | 1 | 1=名称顺序 NAME_ASCENDING / 2=名称倒序 NAME_DESCENDING / 3=路径顺序 PATH_ASCENDING / 4=路径倒序 PATH_DESCENDING / 5=大小顺序 SIZE_ASCENDING / 6=大小倒序 SIZE_DESCENDING / 7=扩展名顺序 EXTENSION_ASCENDING / 8=扩展名倒序 EXTENSION_DESCENDING / 9=类型名顺序 TYPE_NAME_ASCENDING / 10=类型名倒序 TYPE_NAME_DESCENDING / 11=创建时间顺序 DATE_CREATED_ASCENDING / 12=创建时间倒序 DATE_CREATED_DESCENDING / 13=修改时间顺序 DATE_MODIFIED_ASCENDING / 14=修改时间倒序 DATE_MODIFIED_DESCENDING / 15=属性顺序 ATTRIBUTES_ASCENDING / 16=属性倒序 ATTRIBUTES_DESCENDING / 17=文件列表文件名顺序 FILE_LIST_FILENAME_ASCENDING / 18=文件列表文件名倒序 FILE_LIST_FILENAME_DESCENDING / 19=运行次数顺序 RUN_COUNT_ASCENDING / 20=运行次数倒序 RUN_COUNT_DESCENDING / 21=最后变更时间顺序 DATE_RECENTLY_CHANGED_ASCENDING / 22=最后变更时间倒序 DATE_RECENTLY_CHANGED_DESCENDING / 23=最后访问时间顺序 DATE_ACCESSED_ASCENDING / 24=最后访问时间倒序 DATE_ACCESSED_DESCENDING / 25=最后运行时间顺序 DATE_RUN_ASCENDING / 26=最后运行时间倒序 DATE_RUN_DESCENDING |  |
| stopIfFail | 失败后停止 | Boolean | 否 | true |  | 失败后是否停止动作 |

## 输出参数
| Key | 名称 | 类型 | 可见性 | 说明 |
| --- | --- | --- | --- | --- |
| isSuccess | 是否成功 | Boolean |  | 操作是否成功 |
| pathList | 路径列表 | List |  |  |
| resultCount | 结果个数 | Integer |  |  |
| rawResult | 原始结果 | Object |  |  |

## 要点
- `InputParams.<参数Key>` 值固定为 `{ "VarKey": "", "Value": "..." }`。直接写值用 `Value`，引用变量用 `VarKey`。
- `OutputParams.<输出Key>` 的值是变量名字符串，不是对象。
