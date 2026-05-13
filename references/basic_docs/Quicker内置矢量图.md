# Quicker 内置矢量图

## 用途

- 这份文档专门说明 Quicker 内置矢量图在离线 JSON 里怎么写。
- 目标是让 `qk-action-creator` 在离线环境中也能稳定生成可用图标字符串。

## 已固化的离线结论

- 内置矢量图最稳定的离线写法是 `fa:` 字符串。
- 该字符串按 `:` 分段。
- 常见可识别前缀包括：
  - `fa:`
  - `url:`
  - `icon:`
  - `http`
  - `previmg:`
- 对于内置矢量图，skill 默认只使用 `fa:`。

## 可离线稳定使用的格式

- 最稳定格式：

```text
fa:风格_图标名:#RRGGBB
```

- 例如：

```text
fa:Solid_TrashAlt:#FFFF4A0D
fa:Light_Search:#6aaded
fa:Brands_Chrome
```

## 分段规则

- 第 1 段固定是：
  - `fa`
- 第 2 段是 FontAwesome 枚举名：
  - 例如 `Solid_TrashAlt`
  - 例如 `Light_Search`
  - 例如 `Brands_Chrome`
- 第 3 段可选，是颜色：
  - 例如 `#4caf50`
  - 例如 `primary`
  - 例如 `danger`

## 颜色规则

- 颜色段可使用：
  - 十六进制颜色，例如 `#4caf50`
  - 命名语义色，例如：
    - `primary`
    - `secondary`
    - `success`
    - `warning`
    - `danger`
    - `info`
    - `link`
    - `text`

## skill 默认策略

- 只要需求是“使用 Quicker 内置矢量图”，默认优先输出 `fa:` 字符串。
- 不默认改用：
  - SVG 路径数据
  - `Geometry`
  - `DrawingImage`
  - `PathGeometry`
- 原因：
  - 这些不是当前 skill 最稳定的离线输入格式。

## 已确认可出现的位置

- 步骤参数文本中
  - 例如 `customButtons`
- 菜单项图标文本中
- 子程序对象的 `Icon`
- 运行时装饰数据中的图标字段

## 已确认的使用方式

- 步骤参数文本中可以直接出现 `fa:` 图标字符串。
- 菜单按钮文本中也可以直接出现 `fa:` 图标字符串。
- 这份 skill 只把它当作字符串输入格式处理，不扩展为动作级图标结构推断。

## 对 qk-action-creator 的直接约束

- 用户只说“内置矢量图”时，默认输出 `fa:` 字符串。
- 用户若要求某个菜单按钮、提示按钮、子程序带图标，可直接生成该字符串。
- 不要把 FontAwesome 枚举名翻译成中文后再写入。
- 不确定图标枚举名时，必须询问，不猜。

## 不要误判的点

- `fa:` 字符串是离线稳定输入格式。
- 真正渲染时内部会转成 `Path` / `Geometry`，但 skill 不需要直接生成这些对象。
- 因此“支持内置矢量图”不等于“直接生成 WPF 几何数据”。
