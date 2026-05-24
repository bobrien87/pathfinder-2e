# Template Design and Formatting Rules

This rule document defines structural and syntactic standards for note templates in this vault to ensure high-fidelity rendering and prevent Dataview parsing errors.

---

## 1. Frontmatter Variable Quoting

All template placeholders enclosed in curly braces `{}` in the frontmatter must be enclosed in double quotes. This prevents the YAML parser from interpreting bare braces as inline dictionary maps, which corrupts the Obsidian Properties UI.

*   **Correct**:
    ```yaml
    level: "{level}"
    traits: "{traits}"
    ```
*   **Incorrect**:
    ```yaml
    level: {level}
    traits: [{traits}]
    ```

---

## 2. Spacing and Dataview Inline Query Consolidation

To prevent the markdown renderer from producing empty rows and large blank spaces when optional fields (e.g., `Trigger`, `Requirements`, `Defense`, `Duration`) are null, all optional property lines must be consolidated into a single paragraph/query block.

Use string concatenation with conditional HTML `<br>` line breaks inside the query. Do not place separate queries on consecutive lines.

### Standard Pattern for Optional Attributes
```markdown
`= choice(this.field1 != null, "**Field 1** " + this.field1, "") + choice(this.field2 != null, choice(this.field1 != null, "<br>", "") + "**Field 2** " + this.field2, "")`
```

### Standard Separators
When multiple inline attributes or metadata fields are rendered on the same line, do **NOT** use pipe characters (`|`) or bullet points (`•`) as separators. Always use a semi-colon followed by a space (`; `).

---

## 3. Action Icon Application

Pathfinder 2e action icons are rendered via custom CSS snippets targeting inline code blocks. Follow these rules for action syntax:

1.  **Metadata Fields (Frontmatter)**:
    *   To allow the consolidated Dataview header to output action symbols, wrap them in backticks inside the frontmatter string.
    *   *Example*: `cast: "\`pf2:1\` to \`pf2:3\`"` or `cast: "\`pf2:r\`"`
2.  **Body Descriptions and Heightened Wording**:
    *   Do **NOT** replace plain-text mentions of numbers of actions in spell/feat descriptions or heightened sections (e.g., do not replace "For each additional action you use..." or "with each action you spend"). Leave these as plain text.

---

## 4. Creature Frontmatter Formatting (Fantasy Statblocks)

To ensure the **Fantasy Statblocks** plugin can parse and index creature notes properly, always use YAML frontmatter properties rather than inline `statblock` codeblocks containing metadata:

1.  **Identifier & Layout**:
    *   `statblock: true` must be specified to trigger the bestiary parser.
    *   `layout: Basic Pathfinder 2e Layout` must be specified to select the correct PF2e block configuration.

2.  **Modifiers Array**:
    *   `abilityMods` must be defined as a list of strings: `["+4", "+1", "+3", "+0", "+0", "+0"]`. Do not use bare numbers or unquoted signs (like `+4` without quotes) which can trigger YAML parsing errors.

3.  **Trait List Properties**:
    *   Optional properties mapped to `traits` blocks (e.g., `abilities_top`, `abilities_mid`, `abilities_bot`, `attacks`, `spellcasting`) expect a list of objects containing `name` and `desc`.
    *   If a creature does not possess any items for these lists, configure them as empty lists `[]` in the frontmatter, or omit the keys entirely. Do not leave them containing empty-string attributes as that will cause the statblock to render empty lines.

4.  **Sourcebook Field**:
    *   Define `sourcebook` in the frontmatter (e.g. `sourcebook: "{source}"`). This satisfies the Dataview query at the bottom of the note (referencing `this.sourcebook`) and the Statblocks plugin layout. The duplicate `source` property is not needed for creatures.

5.  **Metadata Classification**:
    *   Set `type: creature` to categorize the entity type.
    *   Set `group` as a YAML list of strings defining the creature's mechanical/thematic families (e.g. `group: ["Undead", "Spellcaster"]` or `group: ["Dragon"]`).
