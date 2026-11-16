from pathlib import Path
import zipfile, json
root = Path(__file__).resolve().parents[1]
skill = (root / "skills/instructions/SKILL.md").read_text(encoding="utf-8")
body = skill.split("---", 2)[2].lstrip()
(root / "gemini").mkdir(exist_ok=True)
(root / "gemini/instrucoes.md").write_text(body, encoding="utf-8")
claude = root / "claude/prontuario-upa"
claude.mkdir(parents=True, exist_ok=True)
(claude / "SKILL.md").write_text("---\nname: prontuario-upa\ndescription: Organiza admissão, evolução e discussão clínica em português no modelo UPA quando o médico solicita esses registros.\n---\n\n" + body, encoding="utf-8")
json.loads((root / "plugin.json").read_text())
(root / "dist").mkdir(exist_ok=True)
with zipfile.ZipFile(root / "dist/prontuario-upa-chatgpt.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for item in [root / "LICENSE", root / "plugin.json", *(root / "skills").rglob("*"), *(root / "assets").rglob("*")]:
        if item.is_file(): z.write(item, item.relative_to(root))
with zipfile.ZipFile(root / "dist/prontuario-upa-claude.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write(claude / "SKILL.md", "prontuario-upa/SKILL.md")
    z.write(root / "LICENSE", "prontuario-upa/LICENSE")
for name in ["prontuario-upa-chatgpt.zip", "prontuario-upa-claude.zip"]:
    with zipfile.ZipFile(root / "dist" / name) as z:
        assert z.testzip() is None
        print(name, z.namelist())
