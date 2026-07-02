# Contributing

**We share the recipe, not the black box.** Everything here is plain, readable Markdown you can open, audit and fork. The enemy is never the format, it is the black box: an opaque artifact that hides its logic or runs a canned process on you. Keep that line in mind for anything you submit.

This cookbook grows from real work. Three ways to contribute.

## Add a recipe

A recipe is a **prompt or pattern** you have actually used for financial work with an AI agent.

State the **kind** at the top of the recipe:
- **Prompt**: it does the task in-session.
- **Custom-skill**: it forges or hardens a skill, script or `FINANCE.md` the user owns.

## Add a skill

A skill is a small **listen-first consultant** that lives in `skills/your-skill-name/SKILL.md`. The bar that keeps it out of black-box territory: it must **ask before it acts** and adapt to the case in front of it, never unroll a fixed template. It must be readable Markdown a user can audit and fork, name the wall it cannot cross (structure, persistence), and be field-tested like everything else. If your contribution only unrolls a rigid process, it is not a skill we want, rewrite it as a prompt recipe or make it listen first.

1. Copy [`TEMPLATE.md`](./TEMPLATE.md) into `recipes/your-recipe-name.md`.
2. Fill the sections: the kind, the problem, the prompt, where it breaks, notes.
3. Be honest about the wall. Every recipe names the point where the prompt alone stops being enough. A recipe that claims a prompt replaces a model will not be merged.
4. Add a one-line note on where it was field-tested. Untested recipes do not belong here.
5. Add a row to the recipes table in the [README](./README.md).

Open a pull request. Keep it to one recipe per PR.

## Suggest a library entry

The library in the README points to good external resources (other people's prompts, skills, posts, repos). Curation, not authorship.

The bar: it has to earn its place. We would rather link 10 vetted resources than 200 unsorted ones. Add a row to the library table with the resource, the author, what it is genuinely good for, and the link. Say in your PR why it earns a spot.

## Style

- English, plain and direct. No filler.
- No em dash. Use a comma, a colon, or parentheses.
- Show the prompt verbatim in a code block so people can copy it.
- If a recipe leans on a Layerz feature, link it, but the recipe must be useful to someone who never opens Layerz.
