"""Render game data to printable HTML files using Jinja2 templates."""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from . import data

TEMPLATE_DIR = Path(__file__).parent / "templates"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def render_all(output_dir: Path | None = None) -> None:
    out = output_dir or OUTPUT_DIR
    out.mkdir(parents=True, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,
        keep_trailing_newline=True,
    )

    templates = {
        "karten.html.j2": ("karten.html", {"cards": data.ACTION_CARDS}),
        "krisen.html.j2": (
            "krisen.html",
            {
                "dynamic": data.DYNAMIC_CRISES,
                "region": data.REGION_CRISES,
                "sev": {1: "🟡 Gering", 2: "🟠 Mittel", 3: "🔴 Schwer"},
            },
        ),
        "tableaus.html.j2": (
            "tableaus.html",
            {"regions": data.REGIONS, "players": data.KINGDOMS},
        ),
        "tokens.html.j2": ("tokens.html", {"symbols": data.TOKEN_TYPES}),
        "regelwerk.html.j2": ("regelwerk.html", {}),
    }

    for tpl_name, (out_name, ctx) in templates.items():
        tpl = env.get_template(tpl_name)
        (out / out_name).write_text(tpl.render(**ctx), encoding="utf-8")
        print(f"  {out / out_name}")


def main() -> None:
    print("Rendering cards …")
    render_all()
    print("Done.")


if __name__ == "__main__":
    main()
