from pathlib import Path

def test_required_files_exist():
    """Verify that the main application files exist."""
    project_root = Path(__file__).resolve().parents[1]

    required_files = [
        "backend.py",
        "frontend.py",
        "mcp_client.py",
        "pdf_generator.py",
        "requirements.txt",
        "Dockerfile",
    ]

    for filename in required_files:
        assert (project_root / filename).is_file(), (
            f"Required file is missing: {filename}"
        )

