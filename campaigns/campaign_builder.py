from pathlib import Path
import re

# Folder containing your campaign text files
SOURCE_ROOT = Path(
    r"C:\Users\e_yac\OneDrive\Documents\Projects\hermes-dm\campaigns"
)

# Where generated files will go
OUTPUT_ROOT = Path(
    r"C:\Users\e_yac\OneDrive\Documents\Projects\hermes-dm\generated"
)

# Matches:
# vanished-century/campaign.yaml
# vanished-century/factions/foo.yaml
# data/campaigns/vanished-century/session-state.json
FILE_PATTERN = re.compile(
    r"^(?:[A-Za-z0-9_-]+|data)"
    r"(?:/[A-Za-z0-9_.-]+)+"
    r"\.(yaml|json|md)$"
)

SKIP_LINES = {
    "yaml",
    "json",
    "markdown",
    "<br>",
}


def normalize_line(line: str) -> str:
    """
    Remove formatting artifacts from copied documents.
    """
    return line.rstrip("\n").replace("\ufeff", "")


def write_file(relative_path: str, content_lines: list[str]):
    target = OUTPUT_ROOT / relative_path

    target.parent.mkdir(parents=True, exist_ok=True)

    content = "".join(content_lines).strip()

    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.write("\n")

    print(f"[CREATED] {target}")


def process_source_file(source_file: Path):
    print(f"\nProcessing: {source_file.name}")

    current_file = None
    buffer = []

    def flush():
        nonlocal current_file, buffer

        if current_file is None:
            return

        write_file(current_file, buffer)
        buffer = []

    with open(source_file, "r", encoding="utf-8") as f:
        for raw_line in f:

            line = normalize_line(raw_line)
            stripped = line.strip()

            # New file marker?
            if FILE_PATTERN.match(stripped):
                flush()
                current_file = stripped
                continue

            # Ignore helper markers
            if stripped in SKIP_LINES:
                continue

            # Ignore HTML artifacts
            if stripped == "":
                buffer.append("\n")
                continue

            buffer.append(raw_line)

    flush()


def main():
    if not SOURCE_ROOT.exists():
        print(f"Source path not found:\n{SOURCE_ROOT}")
        return

    txt_files = sorted(SOURCE_ROOT.rglob("*.txt"))

    if not txt_files:
        print("No .txt campaign files found.")
        return

    print(f"Found {len(txt_files)} source files.\n")

    for txt_file in txt_files:
        process_source_file(txt_file)

    print("\nDone.")
    print(f"Output written to:\n{OUTPUT_ROOT}")


if __name__ == "__main__":
    main()