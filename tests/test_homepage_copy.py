from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOMEPAGE = ROOT / "index.html"


def test_homepage_hero_contains_pm_facing_copy():
    html = HOMEPAGE.read_text()

    required_copy = [
        '<span class="prompt" aria-hidden="true">$</span>fin123',
        "by Reckoning Machines",
        "The operating system for emerging investment firms.",
        "Investment decisions evolve.",
        "Research changes. Estimates change. Markets change.",
        "Your process should keep up.",
        "Track decisions",
        "Preserve context",
        "Move faster",
        "Scale your process",
        "Less chaos",
        "=AI()",
        "built into the investment process.",
        "Not bolted on.",
        "Built for emerging managers and investment teams.",
        "The investment process is the authority.",
    ]

    for copy in required_copy:
        assert copy in html


def test_homepage_hero_removes_ontology_heavy_copy():
    html = HOMEPAGE.read_text()

    forbidden_copy = [
        "integrated into the model as a governed substrate",
        "Model Through Time",
        "canonical substrate",
        "durable object",
        "governed state machine",
    ]

    for copy in forbidden_copy:
        assert copy not in html
