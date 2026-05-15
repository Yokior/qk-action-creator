---
name: qk-action-creator
description: Generate or modify Quicker action JSON files from user requirements, using bundled step definition markdown converted from Quicker action docs. Use when Codex needs to create a new action JSON, revise an existing action JSON, explain which Quicker built-in steps fit a requirement, or directly run a Quicker injector action from the current environment to inject the JSON into another action. When requirements are underspecified but code generation is the goal, ask numbered clarification questions one at a time with lettered options and a recommended answer. If local references are insufficient, consult the official Quicker help URL recorded in the relevant document before asking the user.
---

# QK Action Creator

生成或修改 Quicker 动作 JSON，并在当前环境直接执行“注入动作”，把 JSON 写回 Quicker 目标动作。

## 工作流

1. 先判断任务是“解释模块/设计方案”“新建动作 JSON”还是“修改已有 JSON”。
2. 先判断当前信息是否足以直接选模块、定变量、定关键参数。
3. 若只是缺少不会影响实现路径的细枝末节，不要停下来盘问，先继续设计或生成。
4. 若缺少的信息会直接影响模块选择、变量结构、目标动作、动作级元数据或保存/注入链路，先提问再继续。
5. 提问时一次只问一个关键问题，并按“Q 序号 + 选项 + 推荐答案”的格式输出。
6. 若某个问题可以通过读取代码库、现有 JSON、skill 配置或参考文档自行确认，就先查，不要先问用户。
7. 若需求涉及模块语义、变量类型、参数计算、插值或表达式，先读取 `references/basic_docs/` 下与问题直接相关的基础文档。
8. 再读取 `references/step_docs/` 下与需求直接相关的步骤文档。
9. 若本地参考文档未能确认关键字段、参数取值、控制参数行为、线程要求或模块边界，立即访问对应文档里记录的官方帮助 URL。
10. 若官方文档已经明确，按官方文档修正理解与 JSON；若官方文档仍未明确，停止猜测并询问用户。
11. 若需求涉及动作右键菜单、动作自身图标、最小版本、触发后不关闭面板等动作级属性，先读取 `references/basic_docs/动作右键菜单与动作元数据.md`。
12. 若需求涉及 Quicker 内置矢量图、菜单项图标、按钮图标、子程序图标，先读取 `references/basic_docs/Quicker内置矢量图.md`。
13. 先用 Quicker 内置模块拆解需求，优先选最直接的现成步骤，不要一上来写脚本。
14. 若只是简单赋值、简单计算、条件值选择、成员访问，优先用表达式；若只是拼文本，优先用 `$$` 文本插值。
15. 只按技能目录内文档里已经存在且已被本 skill 校正过的模块键、输入参数、输出参数拼装 JSON，不猜字段。
16. 若需求涉及动作级持久化状态数据，默认优先使用 Quicker 提供的 `状态存取` 模块，不要先写脚本自管读写。
17. 只有当内置模块、表达式、文本插值组合后仍然难以实现，或实现会明显过度复杂时，才使用 `运行C#代码`。
18. 若动作开始变长，主动判断是否该拆成步骤组或子程序，不要把所有逻辑堆进主流程。
19. 如需修改已有 JSON，先对目标动作执行一次“同步”，把最新动作定义拉回本地 JSON，再基于该文件修改。
20. 如需新建动作 JSON，先创建空 JSON 文件，再对目标动作执行一次“同步”，把同步后的结果作为工作基底，再基于该文件修改；不要先写业务内容再同步。
21. 同步完成后，先保留原结构，只改与需求直接相关的部分。
22. 把结果写到明确的 JSON 文件。
23. 生成或修改 JSON 后，自动执行一次“注入动作”；执行前先读取 `config.json` 中的“注入器”动作 ID，若缺失再询问用户并保存。
24. 根据注入返回结果判断是否完成；若失败，先回查相关步骤文档和其官方帮助 URL，再按错误内容继续修改 JSON 后重试。

## 澄清提问格式

- 只有在信息缺失会改变实现路径时，才发起澄清提问。
- 一次只问一个问题，不并发抛出多个问题。
- 问题编号格式固定为 `Q1`、`Q2`、`Q3`，按会话内顺序递增。
- 每个问题给出若干互斥选项，格式固定为 `A`、`B`、`C`、`D`、`E`。
- 必须给出单一推荐选项，写成 `推荐：B`。
- 推荐后必须紧跟一句理由，说明为什么这个选项最符合当前需求与本 skill 的实现优先级。
- 若用户的需求明显适合成熟内置模块，推荐项必须优先落在内置模块方案，不要把脚本方案和内置方案并列推荐。
- 若用户选了非推荐项，只要该项可实现，就按其选择继续，不要反复拉回推荐项。
- 若不存在真实可选分支，不要硬造多选题，直接陈述结论或继续执行。
- 若问题本质上是在确认一个具体值，例如动作 ID、变量名、现有 JSON 路径，不要伪装成方案选择题，直接询问该值。
- 问题输出格式如下：

```text
Q1 这一步的结果要存到哪里？
A. 只在当前流程里临时使用
B. 写入动作状态，供下次运行继续读取
C. 写入云状态，在多设备之间共享

推荐：B
理由：需求包含“下次运行继续使用”，按本 skill 规则应优先使用本地状态存取，而不是脚本或云状态。
```

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
- 这个 skill 默认按“没有源码、没有真实案例、需要独立完成动作”来工作，不因为缺少案例就猜字段或发明写法。
- 需求如果是“存一份动作自己的状态数据，后面再次运行还要读出来”，默认优先用 `sys:stateStorage`。
- 只有在需求明确要求跨设备、跨账号共享状态时，才考虑 `云状态存取`，不要把普通本地状态默认做成云状态。
- 需求如果是“维护一组可反复复用的配置项”，默认优先用：
  - `sys:form`
  - `sys:stateStorage`
  - `sys:simpleIf` / `sys:if`
  - `sys:stop`
- 需求如果是“步骤里弹出菜单”，优先用 `sys:showmenu` 或相关步骤能力。
- 需求如果是 `sys:custompanel`，默认优先用 `operationData` 的 JSON 形式描述操作项，不默认使用文本简写。
- 只有当 `defaultOperation` 的具体写法已经被本 skill 文档明确覆盖时，才允许使用 `"[图标]标题|data"` 这类简写格式。
- 需求如果是“动作本身右键菜单”，先判定这是 `ActionItem` 元数据，不是 `XAction` 步骤。
- 用户如果要新做动作右键菜单，必须先提示用户在 Quicker 里手工创建右键菜单，再根据用户已创建的右键菜单继续后续开发。
- 在用户尚未手工创建前，不要生成动作右键菜单 JSON，不要设计 `ContextMenuData` 文本，不要假设菜单 DSL。
- 需求如果是“使用 Quicker 内置矢量图”，默认优先用 `fa:` 字符串，不直接生成 WPF 几何对象。
- 当前工作区样例与本 skill 约定都采用 `quicker_in_param` 作为动作入口参数。若同一动作既支持普通点击又支持菜单入口，主流程默认优先先判断 `quicker_in_param`。
- 需求如果是“设置参数”“管理配置”“维护数据”这类入口分支，命中后默认应：
  - 进入专用分支
  - 完成保存或维护动作
  - 视情况给 `sys:notify`
  - 紧接 `sys:stop`
  - 不继续执行主功能
- 多字段表单若只是固定少量变量，优先 `operation=variables` 或 `dict`。
- 多字段表单若字段结构依赖词典、显示条件、动态选项或分组复用，优先 `operation=dict_dynamic`。
- `dict_dynamic` 离线生成时，默认优先写 `dynamicFormForDictDef` 的 JSON `Fields` 结构；只有在当前文档已明确覆盖相关对象模型时，才使用返回 `FormField` 列表的表达式写法。
- 主流程负责编排，重复逻辑、阶段逻辑、分支大块逻辑优先拆到步骤组或子程序。
- 同一段逻辑如果会被调用两次及以上，优先抽成子程序。
- 同一阶段里只是为了可读性分块、批量折叠、整体启停，优先使用步骤组。
- 流程控制优先使用卫语句或提前返回，减少多级嵌套。
- 仅有 `if` 时优先 `sys:simpleIf`；同时存在 `if` 和 `else` 时才使用 `sys:if`。
- 不要生成空的 `ElseSteps`。
- 对复杂动作，关键业务阶段优先加 `sys:comment` 注释模块；不要机械地给每一步都单独加注释。
- 只有涉及 Quicker 内部服务、复杂对象构造、现成模块明显缺失、表达式难以维护时，才用 `sys:csscript`。
- 决定使用 `sys:csscript` 时，必须先能说明“为什么内置模块 + 表达式/插值不适合”。
- 对模块行为、参数格式、控制参数可见性、枚举取值存在疑点时，先查当前文档中的帮助 URL；官方文档未明确时再询问用户。

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
- 配置型动作若需要“下次继续沿用上次参数”，默认优先采用以下主结构：
  - 默认配置初始化
  - 读取动作状态
  - 若状态非空则载入配置
  - 判断入口参数
  - 设置分支保存配置并停止
  - 普通分支继续执行主功能
- 若步骤文档之间存在冲突，优先采用本 skill 中已经人工校正过的样例与规则，不沿用明显失真的自动转存结果。
- 动作一旦出现多个明显阶段，优先用 `sys:group` 分段，并写清楚组的业务语义。
- 动作一旦出现可复用流程，优先在顶层 `SubPrograms` 中定义子程序，再在主流程用 `sys:subprogram` 调用。
- 子程序若需图标，可写其 `Icon` 字段；图标值优先用 `fa:` 字符串。
- 步骤内按钮、菜单项、操作项若支持图标文本，也优先用 `fa:` 字符串。
- 未确认的字段不补，不写兜底值，不发明扩展字段。
- 输出参数名是变量名字符串，不是对象。
- 无 `else` 时，不要为了凑结构生成 `ElseSteps: []`。
- 动作进入复杂阶段后，主流程应更像“调度表”，不要把所有细节都平铺在顶层 `Steps`。

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
- 若需求涉及多字段配置、设置入口、状态持久化、停止返回，优先再读：
  - `references/step_docs/多字段表单.md`
  - `references/step_docs/状态存取.md`
  - `references/step_docs/停止(return).md`
  - `references/step_docs/运行或停止动作.md`
  - `references/example_docs/多字段表单_动态词典配置样例.md`
  - `references/example_docs/右键菜单设置入口样例.md`
- 文档通常已经给出：
  - 模块键
  - 最小 JSON
  - 输入参数表
  - 输出参数表
  - 控制参数与可见性
- 本 skill 默认假定当前任务拿不到源码，也拿不到真实动作案例，因此参考资料链路必须稳定：
  - 先查本 skill 自带 `references/`
  - 再查对应文档中的官方帮助 URL
  - 官方文档仍未明确时，再询问用户
- 需要跨文件组合动作时，只读取必要文档，不要整批加载全部文档。
- 如果只是要解释某个基础概念，不要急着生成 JSON。
- 如果能从已有步骤文档直接选出模块，就先选模块，再决定参数里是否用 `$=` 或 `$$`。
- 若一个需求只是简单计算或简单文本拼接，不要跳到 `运行C#代码.md`。
- 若某个步骤文档中出现类型、默认值、控制参数、可见性互相冲突，先以该文档里的“要点”“样例”“人工补充说明”为准。
- 不同步骤的脚本文本参数不能互相套用规则。
- `sys:jsscript` 的脚本换行规则只适用于 `references/step_docs/运行Javascript代码.md` 对应模块。
- `sys:chromecontrol` 的 `InputParams.script.Value` 若要写多行脚本，JSON 中应写 `\r\n`，不要写成字面量 `\\r\\n`。
- 若本地文档缺少某个关键字段、关键参数、默认值、枚举取值或行为说明，必须访问该文档顶部 `帮助` 一行里的官方 URL。
- 若官方文档与本地人工校正规则冲突，先以本 skill 已人工校正且已验证可用的规则为准；若仍无法判断，再询问用户。
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
- `references/example_docs/多字段表单_动态词典配置样例.md`
- `references/example_docs/右键菜单设置入口样例.md`

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
- 该脚本支持两种模式：
  - 默认模式：把 JSON 文件路径传给注入器，执行“本地文件 -> 目标动作”。
  - `--sync-only`：把 `同步+JSON 文件路径` 传给注入器，执行“目标动作 -> 本地文件”。
- 底层仍然调用：

```bat
cmd.exe /c 'C:\Program Files\Quicker\QuickerStarter.exe' -c runaction:注入器动作ID?'JSON文件路径'
```

- 同步模式底层等价于：

```bat
cmd.exe /c 'C:\Program Files\Quicker\QuickerStarter.exe' -c runaction:注入器动作ID?'同步D:\path\action.json'
```

- `-c` 表示从控制台等待返回结果，默认最长 20 秒。
- 成功返回通常是 `ok`。
- 同步成功返回通常是 `sync ok`。
- 失败返回通常是注入动作内部输出的错误文本。
- 如果脚本标准输出为空，不能直接判成功，需要继续结合退出码和目标动作实际状态判断。

## 修改已有 JSON

- 第一步不是直接读本地文件，而是先执行：

```bat
python .codex\skills\qk-action-creator\scripts\run_quicker_inject.py --sync-only "JSON文件路径"
```

- 只有同步返回 `sync ok` 后，才继续读取该本地 JSON。
- 同步失败时，先处理同步错误，不要基于旧文件继续修改。
- 仅修改与当前需求直接相关的步骤、参数、变量或输出。
- 不顺手改命名、不重排数组、不重写整份结构，除非原文件明显无效且修复必需。

## 新建动作 JSON

- 先创建空 JSON 文件，作为后续同步和修改的工作文件。
- 再执行同步，把目标动作当前定义写回该空文件。
- 只有同步完成后，才开始补步骤、变量和元数据。
- 不要先在本地文件里写完整内容再同步，避免被同步结果覆盖。

## 结果判断

- 返回 `ok`：视为注入成功。
- 返回空文本：不能直接判成功，需要提醒用户确认注入动作是否有输出。
- 返回错误文本：按原文保留关键信息，定位是：
  - JSON 结构错误
  - 步骤参数错误
  - 注入动作内部逻辑错误
  - 目标动作 ID 或保存链路错误
- 若错误指向某个具体步骤或参数，而本地文档不足以解释，必须回查该步骤文档的官方帮助 URL，再决定如何修改。
- 若回查官方文档后仍无法确认问题根因，不继续猜测，直接询问用户。

## 输出要求

- 生成 JSON 时，优先输出到用户当前工作区。
- 执行注入前，确认目标 JSON 文件路径明确可用。
- 若当前需求是“修改”动作 JSON，必须先同步，再修改，再注入。
- 若当前需求是“新建”动作 JSON，完成 JSON 后默认继续执行注入，不额外等待用户再次确认。
- 注入失败时，先依据错误调整 JSON 或命令，再重试；不要无依据反复重试。
