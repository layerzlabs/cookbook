# Installing a skill

Every skill here is a single readable `SKILL.md`. **Read it before you install it.** That is the whole point: you are installing a set of instructions you can check, not a black box you trust.

## In Claude (Cowork or claude.ai)

1. Open the skill's `SKILL.md` on GitHub and download it (the download button in the file toolbar).
2. In Claude: **+** > **Skills** > **Manage skills** > **Add** > **Upload skill**, then drop the `.md` file in.

That is it. No terminal, no zip. The skill loads itself when the moment fits.

If Claude never picks the skill up, check that **code execution** is enabled in your settings. Skills need it.

## In Claude Code

If you already have the repo:

```bash
cp -r skills/<skill-name> ~/.claude/skills/   # personal, every project
cp -r skills/<skill-name> .claude/skills/     # or project-scoped
```

Or ask your agent to do it for you:

```
Install the "<skill-name>" skill from
https://github.com/layerzlabs/cookbook (folder skills/<skill-name>).
Read its SKILL.md, then copy the whole folder into my skills directory:
~/.claude/skills/ for personal use, or .claude/skills/ in this project.
Keep SKILL.md unchanged.
```

## In any other agent

The `SKILL.md` body is a plain system prompt. Paste it into a project, a custom instruction or a system prompt, and it works the same way.

## Then make it yours

You own the file. These skills are written from real practice, but not from *your* practice. Open the `SKILL.md`, cut what does not apply, add the conventions and the vocabulary of your business. A forked skill that fits beats a pristine one that does not.
