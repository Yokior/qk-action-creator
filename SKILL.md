---
name: qk-action-creator
description: Generate or modify Quicker action JSON files from user requirements, using bundled step definition markdown converted from Quicker action docs. Use when Codex needs to create a new action JSON, revise an existing action JSON, or directly run a Quicker injector action from the current environment to inject the JSON into another action.
---

# QK Action Creator

生成或修改 Quicker 动作 JSON，并在当前环境直接执行“注入动作”，把 JSON 写回 Quicker 目标动作。

## 工作流

1. 先判断任务是“新建动作 JSON”还是“修改已有 JSON”。
2. 先判断需求是在问“步骤模块怎么用”，还是已经进入“拼动作 JSON”阶段。
3. 若需求涉及模块语义、变量类型、参数计算、插值或表达式，先读取 `references/basic_docs/` 下与问题直接相关的基础文档。
4. 再读取 `references/step_docs/` 下与需求直接相关的步骤文档。
5. 若需求涉及动作右键菜单、动作自身图标、最小版本、触发后不关闭面板等动作级属性，先读取 `references/basic_docs/动作右键菜单与动作元数据.md`。
6. 若需求涉及 Quicker 内置矢量图、菜单项图标、按钮图标、子程序图标，先读取 `references/basic_docs/Quicker内置矢量图.md`。
7. 先用 Quicker 内置模块拆解需求，优先选最直接的现成步骤，不要一上来写脚本。
8. 若只是简单赋值、简单计算、条件值选择、成员访问，优先用表达式；若只是拼文本，优先用 `$$` 文本插值。
9. 只按技能目录内文档里已经存在且已被本 skill 校正过的模块键、输入参数、输出参数拼装 JSON，不猜字段。
10. 若需求涉及动作级持久化状态数据，默认优先使用 Quicker 提供的 `状态存取` 模块，不要先写脚本自管读写。
11. 只有当内置模块、表达式、文本插值组合后仍然难以实现，或实现会明显过度复杂时，才使用 `运行C#代码`。
12. 若动作开始变长，主动判断是否该拆成步骤组或子程序，不要把所有逻辑堆进主流程。
13. 如需修改已有 JSON，先保留原结构，只改与需求直接相关的部分。
14. 把结果写到明确的 JSON 文件。
15. 生成或修改 JSON 后，自动执行一次“注入动作”；执行前先读取 `config.json` 中的“注入器”动作 ID，若缺失再询问用户并保存。
16. 根据注入返回结果判断是否完成；若失败，按错误内容继续修改 JSON 后重试。

## 实现优先级

1. Quicker 内置步骤模块。
2. 内置步骤参数中的表达式 `$=`。
3. 文本参数中的 `$$` 插值。
4. 少量步骤组合。
5. 步骤组 / 子程序重组复杂流程。
6. `运行C#代码`。

## 决策规则

- 能用现成模块实现，就不用脚本。
- 能用一个现成步骤加 `$=` 或 `$$` 实现，就不要改成多步脚本。
- 简单计算优先用 `sys:assign` 或其他支持文本输入的内置步骤配合 `$=`。
- 简单拼文本优先在文本参数里直接写 `$$`，不要先上 `sys:csscript`。
- 需求如果是“存一份动作自己的状态数据，后面再次运行还要读出来”，默认优先用 `sys:stateStorage`。
- 只有在需求明确要求跨设备、跨账号共享状态时，才考虑 `云状态存取`，不要把普通本地状态默认做成云状态。
- 需求如果是“步骤里弹出菜单”，优先用 `sys:showmenu` 或相关步骤能力。
- 需求如果是 `sys:custompanel`，默认优先用 `operationData` 的 JSON 形式描述操作项，不默认使用文本简写。
- 只有当 `defaultOperation` 的具体写法已经被本 skill 文档明确覆盖时，才允许使用 `"[图标]标题|data"` 这类简写格式。
- 需求如果是“动作本身右键菜单”，先判定这是 `ActionItem` 元数据，不是 `XAction` 步骤。
- 用户如果要新做动作右键菜单，必须先提示用户在 Quicker 里手工创建右键菜单，再根据用户已创建的右键菜单继续后续开发。
- 在用户尚未手工创建前，不要生成动作右键菜单 JSON，不要设计 `ContextMenuData` 文本，不要假设菜单 DSL。
- 需求如果是“使用 Quicker 内置矢量图”，默认优先用 `fa:` 字符串，不直接生成 WPF 几何对象。
- 主流程负责编排，重复逻辑、阶段逻辑、分支大块逻辑优先拆到步骤组或子程序。
- 同一段逻辑如果会被调用两次及以上，优先抽成子程序。
- 同一阶段里只是为了可读性分块、批量折叠、整体启停，优先使用步骤组。
- 只有涉及 Quicker 内部服务、复杂对象构造、现成模块明显缺失、表达式难以维护时，才用 `sys:csscript`。
- 决定使用 `sys:csscript` 时，必须先能说明“为什么内置模块 + 表达式/插值不适合”。

## 生成规则

- JSON 顶层优先保持 Quicker 常见结构：
  - `SubPrograms`
  - `Variables`
  - `Steps`
- 生成前先判断本次输出是否只涉及 `XAction` 流程定义。
- 若需求包含动作右键菜单，不直接生成该部分，而是等待用户手工创建后再继续修改相关流程。
- `Variables` 的顶层结构以技能内 `references/basic_docs/顶层Variables结构.md` 为准。
- 变量使用语义看 `references/basic_docs/`
- 单个步骤优先保持文档里的最小结构：
  - `StepRunnerKey`
  - `InputParams`
  - `OutputParams`
  - 如该步骤存在分支，再补 `IfSteps`、`ElseSteps`
- `InputParams` 下每个参数对象默认写：
  - `VarKey`
  - `Value`
- 简单变量改写优先使用 `sys:assign`，不要为了 `+1`、拼提示词、取成员而默认改用 `sys:csscript`。
- 若需求只涉及简单计算、简单判断、简单文本拼接，默认不生成任何脚本步骤。
- 若需求只是在动作内保存或读取少量键值状态，默认不生成任何脚本步骤，直接使用 `sys:stateStorage`。
- 若步骤文档之间存在冲突，优先采用本 skill 中已经人工校正过的样例与规则，不沿用明显失真的自动转存结果。
- 动作一旦出现多个明显阶段，优先用 `sys:group` 分段，并写清楚组的业务语义。
- 动作一旦出现可复用流程，优先在顶层 `SubPrograms` 中定义子程序，再在主流程用 `sys:subprogram` 调用。
- 子程序若需图标，可写其 `Icon` 字段；图标值优先用 `fa:` 字符串。
- 步骤内按钮、菜单项、操作项若支持图标文本，也优先用 `fa:` 字符串。
- 未确认的字段不补，不写兜底值，不发明扩展字段。
- 输出参数名是变量名字符串，不是对象。

## 动作级元数据规则

- 这类需求不属于 `XAction` 顶层：
  - 动作右键菜单
  - 动作最小版本
  - 触发后不关闭面板
  - 停止运行动作时跳过当前动作
  - 启用滚轮触发动作
  - 启用表达式变量求值
- 已确认的动作级字段至少包括：
  - `ContextMenuData`
  - `MinQuickerVersion`
  - `DoNotClosePanel`
  - `SkipWhenStopRunningActions`
  - `AllowScrollTrigger`
  - `EnableEvaluateVariable`
- 不要把 `ContextMenuData` 塞进：
  - `XAction`
  - `Steps`
  - `Variables`
- 如果需求是“新建动作右键菜单”：
  - 先明确告知当前 skill 不能直接独立生成这部分
  - 先让用户手工创建右键菜单
  - 再根据用户已创建的右键菜单做后续流程开发或局部改动
- 如果用户已经手工创建了右键菜单，并能提供当前完整动作导出或现有 `ContextMenuData` 内容：
  - 只根据用户现有内容继续开发
  - 不重写整段菜单定义
  - 仅修改与当前需求直接相关的部分

## 内置矢量图规则

- 默认使用 `fa:` 图标字符串：
  - `fa:风格_图标名:#RRGGBB`
- 颜色段可省略。
- 只在需求明确时写颜色。
- 不确定枚举名时必须询问，不猜。

## 参考资料使用规则

- `references/basic_docs/` 负责回答这些基础问题：
  - 模块与步骤是什么
  - 输入参数如何计算
  - 什么时候用 `$$` 插值
  - 什么时候用 `$=` 表达式
  - 列表、词典、表格、动态对象各自是什么
- 还负责回答：
  - 动作级字段属于 `ActionItem` 还是 `XAction`
  - Quicker 内置矢量图字符串怎么写
- 优先从 `references/step_docs/` 读取与当前需求相关的步骤文档。
- 对以下文档，默认视为本 skill 的人工校正版，优先级高于自动转存痕迹：
  - `references/step_docs/运行C#代码.md`
  - `references/step_docs/运行Javascript代码.md`
  - `references/step_docs/自定义操作窗.md`
- 若需求属于常见基础结构或最小实现，优先再读：
  - `references/example_docs/流程与结构最小样例.md`
  - `references/example_docs/变量与表达式最小样例.md`
  - `references/example_docs/状态存取与脚本最小样例.md`
- 文档通常已经给出：
  - 模块键
  - 最小 JSON
  - 输入参数表
  - 输出参数表
  - 控制参数与可见性
- 需要跨文件组合动作时，只读取必要文档，不要整批加载全部文档。
- 如果只是要解释某个基础概念，不要急着生成 JSON。
- 如果能从已有步骤文档直接选出模块，就先选模块，再决定参数里是否用 `$=` 或 `$$`。
- 若一个需求只是简单计算或简单文本拼接，不要跳到 `运行C#代码.md`。
- 若某个步骤文档中出现类型、默认值、控制参数、可见性互相冲突，先以该文档里的“要点”“样例”“人工补充说明”为准。
- 如果要新增顶层变量，而步骤文档没有说明变量类型，就读取 `references/basic_docs/顶层Variables结构.md` 中已经固化的离线类型表和最小变量结构；文档未覆盖时再明确告知无法确认，不猜字段。
- 如果需求涉及动作右键菜单或动作自身图标，先读：
  - `references/basic_docs/动作右键菜单与动作元数据.md`
  - `references/basic_docs/Quicker内置矢量图.md`
- 若用户需求涉及 Quicker 运行链路、命令行注入、保存行为，再读 `references/quicker_runtime_notes.md`。

## 基础文档索引

- `references/basic_docs/模块和步骤.md`
- `references/basic_docs/参数传递.md`
- `references/basic_docs/文本插值.md`
- `references/basic_docs/表达式.md`
- `references/basic_docs/动态对象变量.md`
- `references/basic_docs/词典类型.md`
- `references/basic_docs/列表类型.md`
- `references/basic_docs/表格变量类型.md`
- `references/basic_docs/顶层Variables结构.md`
- `references/basic_docs/动作结构组织.md`
- `references/basic_docs/动作右键菜单与动作元数据.md`
- `references/basic_docs/Quicker内置矢量图.md`

## 人工样例索引

- `references/example_docs/流程与结构最小样例.md`
- `references/example_docs/变量与表达式最小样例.md`
- `references/example_docs/状态存取与脚本最小样例.md`

## 注入规则

- 这里的“注入动作”就是“注入器”动作。
- 注入依赖一个用户事先准备好的 Quicker 动作。该动作负责：
  - 从 `quicker_in_param` 读取 JSON 文件路径
  - 读取 JSON
  - 反序列化为 `XAction`
  - 把流程定义写回目标动作
  - 保存所属 `ActionProfile`
- 优先读取 `该skill目录下的config.json`。
- 配置文件格式：

```json
{
  "InjectorActionId": "c2b4ebf9-1a50-4e7c-ac20-acef79fb0cdb"
}
```

- 若 `config.json` 不存在，或其中没有可用的 `InjectorActionId`，就必须询问用户“注入器”动作 ID。
- 用户提供后，写回 `config.json`，供后续对话优先读取。
- 若当前对话上下文里已经明确给出了“注入器”动作 ID，也可以直接使用，并同步保存到 `config.json`。
- 执行注入时，优先使用技能目录下的 `scripts/run_quicker_inject.py`。
- 调用方式：

```bat
python .codex\skills\qk-action-creator\scripts\run_quicker_inject.py "JSON文件路径"
```

- 该脚本会：
  - 优先从技能目录下的 `config.json` 读取 `InjectorActionId`
  - 用 `subprocess.Popen(..., stdout=PIPE, stderr=PIPE, shell=False)` 调用 `QuickerStarter.exe`
  - 输出解码后的控制台返回文本
  - 以进程返回码作为脚本退出码
- 该脚本本身只负责把 JSON 文件路径传给注入器。
- 底层仍然调用：

```bat
cmd.exe /c 'C:\Program Files\Quicker\QuickerStarter.exe' -c runaction:注入器动作ID?'JSON文件路径'
```

- `-c` 表示从控制台等待返回结果，默认最长 20 秒。
- 成功返回通常是 `ok`。
- 失败返回通常是注入动作内部输出的错误文本。
- 如果脚本标准输出为空，不能直接判成功，需要继续结合退出码和目标动作实际状态判断。

## 修改已有 JSON

- 先读取原 JSON。
- 仅修改与当前需求直接相关的步骤、参数、变量或输出。
- 不顺手改命名、不重排数组、不重写整份结构，除非原文件明显无效且修复必需。

## 结果判断

- 返回 `ok`：视为注入成功。
- 返回空文本：不能直接判成功，需要提醒用户确认注入动作是否有输出。
- 返回错误文本：按原文保留关键信息，定位是：
  - JSON 结构错误
  - 步骤参数错误
  - 注入动作内部逻辑错误
  - 目标动作 ID 或保存链路错误

## 输出要求

- 生成 JSON 时，优先输出到用户当前工作区。
- 执行注入前，确认目标 JSON 文件路径明确可用。
- 若当前需求是“新建”或“修改”动作 JSON，完成 JSON 后默认继续执行注入，不额外等待用户再次确认。
- 注入失败时，先依据错误调整 JSON 或命令，再重试；不要无依据反复重试。
