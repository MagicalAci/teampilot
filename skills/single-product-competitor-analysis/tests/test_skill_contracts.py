import json
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from spca.cli import file_marks_ready, final_delivery_gate_status  # noqa: E402


class SkillContractsTest(unittest.TestCase):
    def test_task_card_template_exists_and_has_minimum_fields(self):
        template_path = SKILL_ROOT / "task-card.template.json"
        self.assertTrue(template_path.exists(), "缺少 task-card.template.json")

        payload = json.loads(template_path.read_text(encoding="utf-8"))
        self.assertIn("product_name", payload)
        self.assertIn("analysis_goal", payload)
        self.assertIn("output_root", payload)
        self.assertIn("imports_root", payload)
        self.assertIn("manual_root", payload)

    def test_benchmark_passes_current_final_delivery_gate(self):
        benchmark_root = SKILL_ROOT / "examples" / "doubao-aixue-benchmark"
        ok, blockers = final_delivery_gate_status(
            {
                "synthesis_root": benchmark_root / "05-synthesis",
                "experience_root": benchmark_root / "04-experience",
                "writing_root": benchmark_root / "06-writing",
                "factcheck_root": benchmark_root / "07-factcheck",
                "visuals_root": benchmark_root / "08-visuals",
            }
        )
        self.assertTrue(ok, "\n".join(blockers))

    def test_file_marks_ready_rejects_chinese_pending_markers(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "status.md"
            path.write_text("已按新骨架重排，待补关键原话\n", encoding="utf-8")
            self.assertFalse(file_marks_ready(path))


if __name__ == "__main__":
    unittest.main()
