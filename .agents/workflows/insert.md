---
description: Inserts a new entity (spell, feat, background, class, ancestry, settlement, creature, item, etc.) into the vault using its template and formatting rules.
---

# Insert Workflow

This workflow details the procedures for agents to create, place, and register game entities and rules references within the vault when the `/insert` command is triggered.

---

## Workflow Instructions

When the user triggers the `/insert` command, execute these steps:

### Step 1: Gather Requirements
If the user did not provide enough context (e.g., they just typed `/insert`), ask them for:
1.  **Entity Type:** The type of entity to insert (e.g., spell, creature, feat, item, background, class, ancestry, settlement, map, scene, action, effect, condition, affliction, hazard).
2.  **Name:** The name of the entity.
3.  **Details:** Any specific mechanical descriptions, attributes, traits, or source information.

### Step 2: Determine Source Priority
Verify the source book against the priority matrix in `.agents/rules/sources.md`. Ensure the `source-type` metadata field is set correctly (`Remaster`, `Legacy`, or omitted for campaign homebrew).

### Step 3: Apply the Template and Formatting
1.  Retrieve the corresponding template from the `10. Templates/` subfolder.
2.  Generate the content for the placeholders. **CRUCIAL:** You must follow `.agents/rules/templates.md` and `.agents/rules/formatting.md`.
    *   *Frontmatter Properties:* Placeholders in the frontmatter must be enclosed in double quotes (e.g., `level: "{level}"`).
    *   *Consolidated Dataview Queries:* Optional attributes in the body (e.g., Trigger, Requirements, Range/Area/Targets, Defense/Duration) must be combined into unified single-paragraph queries separated by HTML `<br>` tags to prevent blank line rendering.
    *   *Action Icons:* Wrap action codes in backticks (e.g., `` `pf2:1` ``) in frontmatter properties (like `cast`) to enable icon rendering. Do **NOT** replace action words in description body text.
    *   *Creature Metadata:* Set `type: creature` and provide a list of thematic groups (e.g., `group: ["Dragon"]` or `group: ["Undead", "Spellcaster"]`) in the frontmatter.

### Step 4: Write to Vault
Save the newly populated file in its designated directory:

*   **Spells**: `8. System/Spells/Rank X/` (subdivided by rank, e.g. `Rank 1/`, `Cantrip/`, etc.).
*   **Creatures**: `8. System/Creatures/Level X/` (subdivided by level, e.g. `Level -1/`, `Level 0/`, `Level 1/`, etc.).
*   **Hazards**: `8. System/Hazards/`.
*   **Rules Reference**: `8. System/Rules Reference/` (strictly for short snippet-style rules like alignments).

### Step 5: Notify the User
Provide a clickable wikilink (`[[Name]]`) to the newly created file so the user can easily open it in Obsidian.
