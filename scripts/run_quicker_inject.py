import argparse
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_QUICKER_STARTER = Path(r"C:\Program Files\Quicker\QuickerStarter.exe")
SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = SKILL_DIR / "config.json"


def decode_output(data: bytes) -> str:
    if not data:
        return ""
    for encoding in ("utf-8", "gbk"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def load_injector_action_id(config_path: Path) -> str:
    if not config_path.exists():
        raise FileNotFoundError(f"未找到配置文件：{config_path}")
    with config_path.open("r", encoding="utf-8") as f:
        config = json.load(f)
    injector_action_id = str(config.get("InjectorActionId", "")).strip()
    if not injector_action_id:
        raise ValueError(f"配置文件中缺少可用的 InjectorActionId：{config_path}")
    return injector_action_id


def build_command(quicker_starter: Path, injector_action_id: str, json_path: Path) -> list[str]:
    return [
        str(quicker_starter),
        "-c",
        f"runaction:{injector_action_id}?{json_path}",
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="调用 QuickerStarter 执行注入器动作，并获取控制台返回值。"
    )
    parser.add_argument("json_path", help="要注入的动作 JSON 文件路径")
    parser.add_argument(
        "--injector-id",
        dest="injector_id",
        help="注入器动作 ID；不传时从 config.json 读取",
    )
    parser.add_argument(
        "--config",
        dest="config_path",
        default=str(DEFAULT_CONFIG_PATH),
        help="配置文件路径，默认使用技能目录下的 config.json",
    )
    parser.add_argument(
        "--quicker-starter",
        dest="quicker_starter",
        default=str(DEFAULT_QUICKER_STARTER),
        help="QuickerStarter.exe 路径",
    )
    parser.add_argument(
        "--timeout",
        dest="timeout",
        type=int,
        default=30,
        help="等待返回的秒数，默认 30",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    json_path = Path(args.json_path).resolve()
    if not json_path.exists():
        print(f"JSON 文件不存在：{json_path}", file=sys.stderr)
        return 2

    quicker_starter = Path(args.quicker_starter)
    if not quicker_starter.exists():
        print(f"QuickerStarter 不存在：{quicker_starter}", file=sys.stderr)
        return 2

    try:
        injector_action_id = args.injector_id or load_injector_action_id(Path(args.config_path))
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        return 2

    cmd = build_command(quicker_starter, injector_action_id, json_path)

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )
        out, err = proc.communicate(timeout=args.timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        out, err = proc.communicate()
        timeout_stdout = decode_output(out)
        timeout_stderr = decode_output(err)
        if timeout_stdout:
            print(timeout_stdout)
        if timeout_stderr:
            print(timeout_stderr, file=sys.stderr)
        print(f"等待 Quicker 返回超时：{args.timeout} 秒", file=sys.stderr)
        return 124

    stdout_text = decode_output(out).strip()
    stderr_text = decode_output(err).strip()

    if stdout_text:
        print(stdout_text)
    if stderr_text:
        print(stderr_text, file=sys.stderr)

    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
