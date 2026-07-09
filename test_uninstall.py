import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).parent
UNINSTALLER = REPO_ROOT / "uninstall.py"


class UninstallManifestTests(unittest.TestCase):
    def test_manifest_limits_python_uninstall_to_recorded_commands(self):
        with tempfile.TemporaryDirectory() as home:
            home_path = Path(home)
            commands_dir = home_path / ".claude" / "commands"
            commands_dir.mkdir(parents=True)
            manifest_path = home_path / ".claude" / ".ccplugins_manifest.json"
            manifest_path.write_text(json.dumps({"commands": ["refactor.md"]}))

            installed_command = commands_dir / "refactor.md"
            user_command = commands_dir / "docs.md"
            installed_command.write_text("installed by CCPlugins")
            user_command.write_text("owned by the user or another plugin")

            env = os.environ.copy()
            env["HOME"] = home
            env["USERPROFILE"] = home

            result = subprocess.run(
                [sys.executable, str(UNINSTALLER)],
                input="y\nn\n",
                text=True,
                capture_output=True,
                env=env,
                check=False,
            )

            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
            self.assertFalse(installed_command.exists())
            self.assertTrue(user_command.exists())


if __name__ == "__main__":
    unittest.main()
