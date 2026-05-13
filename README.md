# qk-action-creator

用于让 AI 根据需求生成或修改 Quicker 动作 JSON，并通过“注入器”动作把流程定义写回 Quicker 目标动作。

## 项目用途

这个仓库本质上是一个面向 Quicker 动作开发的 skill 仓库，包含三类内容：

- `SKILL.md`：skill 的行为规则、生成规则、注入规则。
- `references/`：离线步骤文档、基础文档、最小样例，用来约束 AI 不猜字段、不乱写结构。
- `scripts/run_quicker_inject.py`：把生成好的 JSON 文件路径传给 Quicker“注入器”动作，并获取控制台返回结果。

适用场景：

- 新建一个 Quicker 动作 JSON。
- 在已有 JSON 上做局部修改。
- 生成完成后，直接把 JSON 注入到 Quicker 目标动作。

## 仓库结构

```text
qk-action-creator/
├─ SKILL.md
├─ config.json
├─ scripts/
│  └─ run_quicker_inject.py
├─ references/
│  ├─ basic_docs/
│  ├─ step_docs/
│  ├─ example_docs/
│  └─ quicker_runtime_notes.md
└─ agents/
```

## 依赖环境

- Windows
- 已安装 Quicker
- 可用的 `QuickerStarter.exe`
- Python 3
- 一个由你自己准备好的 Quicker“注入器”动作

默认情况下，脚本会使用这个路径：

```text
C:\Program Files\Quicker\QuickerStarter.exe
```

如果你的安装路径不同，执行脚本时需要显式传入 `--quicker-starter`。

## config.json 配置

仓库根目录下的 `config.json` 用于保存“注入器”动作 ID，格式如下：

```json
{
  "InjectorActionId": "c2b4ebf9-1a50-4e7c-ac20-acef79fb0cdb"
}
```

`InjectorActionId` 的含义：

- 它不是目标动作 ID。
- 它是“注入器”动作本身的动作 ID。
- AI 生成完 JSON 后，会调用这个动作，把 JSON 写回真正的目标动作。

推荐两种配置方式：

1. 直接手工编辑 `config.json`，写入 `InjectorActionId`。
2. 初次使用时，把“注入器”动作 ID 告诉 AI，由 AI 按 `SKILL.md` 里的约定回填到 `config.json`。

## 典型使用流程

1. 准备好一个 Quicker“注入器”动作。
2. 把该动作 ID 写入 `config.json`，或在首次对话时直接告诉 AI。
3. 让 AI 根据需求生成新的动作 JSON，或修改已有 JSON。
4. AI 参考 `references/` 下的离线文档拼装结构。
5. 生成完成后，调用 `scripts/run_quicker_inject.py` 执行注入。
6. 根据返回值判断成功或失败：
   - 返回 `ok`：通常表示注入成功。
   - 返回空文本：不能直接判定成功，需要检查注入器动作是否有输出。
   - 返回错误文本：按错误内容继续修正 JSON 或注入器逻辑。
