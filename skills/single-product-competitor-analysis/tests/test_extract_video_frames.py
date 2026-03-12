import importlib.util
import unittest
from pathlib import Path

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "extract_video_frames.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("extract_video_frames", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ExtractVideoFramesTest(unittest.TestCase):
    def test_build_command_supports_every_n_frames(self):
        module = load_module()
        command = module.build_ffmpeg_command(
            ffmpeg_bin="ffmpeg",
            input_path=Path("/tmp/demo.mp4"),
            output_pattern=Path("/tmp/frames/frame-%05d.png"),
            fps=None,
            every_n_frames=10,
        )

        self.assertEqual(command[:3], ["ffmpeg", "-i", "/tmp/demo.mp4"])
        self.assertIn("select=not(mod(n\\,10))", command)
        self.assertIn("-vsync", command)
        self.assertIn("vfr", command)


if __name__ == "__main__":
    unittest.main()
