from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOMEPAGE = ROOT / "index.html"


def test_homepage_contains_iris_brand_refresh_copy():
    html = HOMEPAGE.read_text()

    required_copy = [
        '<span class="prompt" aria-hidden="true">$</span><a class="brand-link" href="./index.html"\n                        aria-label="IRIS home">IRIS</a>',
        "by Reckoning Machines",
        "Work the way you think.",
        "The investment research operating system.",
        "Built for investment analysts. Engineered for institutional memory.",
        "IRIS answers questions about your firm's investment work.",
        "IRIS adds the operating system around the model.",
        "Open IRIS runtime",
        "IRIS by Reckoning Machines",
        "./search%20screen.png",
        "./screen.png",
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


def test_homepage_removes_legacy_fin123_visible_branding():
    html = HOMEPAGE.read_text()

    forbidden_copy = [
        ">fin123<",
        "fin123 answers questions",
        "fin123 adds the operating system",
        "full fin123 product",
        "fin123 search surface",
        "fin123 Analyze surface",
    ]

    for copy in forbidden_copy:
        assert copy not in html
