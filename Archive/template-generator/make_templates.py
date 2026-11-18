#!/usr/bin/env python3

from pathlib import Path
import yaml


def make_placeholder(key_path, index=None):
    """
    Build a meaningful placeholder from the key path.
    Example:
      campaign.title -> {campaign_title}
      theme[0] -> {theme_1}
    """

    name = "_".join(
        str(k)
        for k in key_path
        if isinstance(k, str)
    )

    if index is not None:
        return f"{{{name}_{index + 1}}}"

    return f"{{{name}}}"


def template_value(value, key_path=None):
    if key_path is None:
        key_path = []

    # Dictionaries
    if isinstance(value, dict):
        return {
            key: template_value(
                val,
                key_path + [key]
            )
            for key, val in value.items()
        }

    # Lists
    elif isinstance(value, list):
        result = []

        for i, item in enumerate(value):

            if isinstance(item, (dict, list)):
                result.append(
                    template_value(
                        item,
                        key_path + [str(i)]
                    )
                )
            else:
                result.append(
                    make_placeholder(
                        key_path,
                        i
                    )
                )

        return result

    # Boolean
    elif isinstance(value, bool):
        return False

    # Integer
    elif isinstance(value, int):
        return 0

    # Float
    elif isinstance(value, float):
        return 0.0

    # Null
    elif value is None:
        return None

    # Strings and everything else
    return make_placeholder(key_path)


def create_template(input_file, output_file):

    with open(input_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        data = {}

    template = template_value(data)

    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(
            template,
            f,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            width=120
        )


def process_directory(source_dir, output_dir):

    source_dir = Path(source_dir)
    output_dir = Path(output_dir)

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    yaml_files = list(source_dir.rglob("*.yaml"))
    yaml_files.extend(source_dir.rglob("*.yml"))

    if not yaml_files:
        print("No YAML files found.")
        return

    for yaml_file in yaml_files:

        relative_path = yaml_file.relative_to(source_dir)

        output_file = (
            output_dir /
            relative_path.parent /
            f"{yaml_file.stem}_template.yaml"
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        try:
            create_template(
                yaml_file,
                output_file
            )

            print(
                f"Created: {output_file}"
            )

        except Exception as e:
            print(
                f"Failed: {yaml_file} -> {e}"
            )


if __name__ == "__main__":

    process_directory(
        source_dir="./vanished-century",
        output_dir="./templates"
    )