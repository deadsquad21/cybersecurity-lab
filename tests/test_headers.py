import importlib.util
import sys
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "tools" / "headers-analyzer" / "analyze_headers.py"
spec = importlib.util.spec_from_file_location("analyze_headers", MODULE)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)

class HeaderTests(unittest.TestCase):
    def test_good_headers(self):
        headers = {
            "Content-Security-Policy": "default-src 'self'; frame-ancestors 'none'",
            "Strict-Transport-Security": "max-age=31536000",
            "X-Content-Type-Options": "nosniff",
            "Referrer-Policy": "strict-origin",
            "Permissions-Policy": "camera=()",
        }
        result = mod.assess(headers)
        self.assertEqual(result["summary"]["missing"], 0)

    def test_empty_headers(self):
        result = mod.assess({})
        self.assertGreaterEqual(result["summary"]["missing"], 5)

if __name__ == "__main__":
    unittest.main()
