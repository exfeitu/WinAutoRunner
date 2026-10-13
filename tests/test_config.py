import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from runner import load_config

class ConfigTests(unittest.TestCase):
    def test_accepts_valid_config(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "config.json"
            f.write_text(json.dumps({"url": "https://example.com", "interval_seconds": 60, "timeout_ms": 1000}))
            self.assertEqual(load_config(f)["interval_seconds"], 60)

    def test_rejects_invalid_interval(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "config.json"
            f.write_text(json.dumps({"url": "https://example.com", "interval_seconds": 0, "timeout_ms": 1000}))
            with self.assertRaises(ValueError):
                load_config(f)

    def test_rejects_invalid_scheme(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "config.json"
            f.write_text(json.dumps({"url": "file:///secret", "interval_seconds": 60, "timeout_ms": 1000}))
            with self.assertRaises(ValueError):
                load_config(f)

if __name__ == "__main__":
    unittest.main()
