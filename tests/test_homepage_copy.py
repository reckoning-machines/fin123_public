from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOMEPAGE = ROOT / "index.html"


def test_homepage_contains_iris_brand_refresh_copy():
    html = HOMEPAGE.read_text()

    required_copy = [
        '<a class="brand-link" href="./index.html" aria-label="IRIS home">IRIS</a>',
        "by Reckoning Machines",
        "Work the way you think.",
        "The investment research operating system.",
        "Built for investment analysts. Engineered for institutional memory.",
        "Figure 1",
        "The Research Velocity Flywheel",
        "The operating model behind IRIS.",
        "You start with context instead of rebuilding it.",
        "Less time navigating. More time thinking.",
        "Research is one click away, not another search.",
        "Today's work becomes tomorrow's context.",
        "./flywheel.png",
        "Research Shell is the analyst interface to the repository.",
        "Every decision becomes part of the model's history.",
        "Everything stays connected.",
        "Open IRIS runtime",
        "IRIS by Reckoning Machines",
        "./desktop%20iris.png",
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
