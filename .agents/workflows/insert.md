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
1.  **Entity Type:** The type of entity to insert (e.g., spell, creature, feat, item, background, class, ancestry, heritage, deity, archetype, settlement, map, scene, action, effect, condition, affliction, hazard, faction, pc, npc, discovery, session).
2.  **Name:** The name of the entity.
3.  **Details:** Any specific mechanical descriptions, attributes, traits, or source information.
    *   *Factions / Sub-factions:* Determine if the faction is a nested sub-faction (i.e. has a parent faction). Ask the user for the parent faction if it is not specified.

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
*   **Character Creation (Ancestry, Heritage, Class, Background, Feat, Archetype)**: `8. System/Character Creation/[Category]/` (e.g. `8. System/Character Creation/Ancestries/`, `8. System/Character Creation/Heritages/`, etc.).
*   **Rules Reference**:
    *   *Short rule snippets (like Alignment)*: `8. System/Rules Reference/`
    *   *Actions, Afflictions, Conditions, Effects, Traits*: `8. System/Rules Reference/[Category]/` (e.g. `8. System/Rules Reference/Actions/`, `8. System/Rules Reference/Conditions/`, etc.).
    *   *Deities*: `8. System/Rules Reference/Deities/`.
*   **Items**: `8. System/Items/`.
*   **Factions**: `4. NPCs and Factions/[Faction Name]/[Faction Name].md`
*   **Sub-factions**: `4. NPCs and Factions/[Parent Faction Name]/.../[Sub-faction Name]/[Sub-faction Name].md` (recursively nested folder structure matching parentage).
*   **NPCs**: `4. NPCs and Factions/[Faction Name]/[NPC Name].md` (placed inside the corresponding faction or sub-faction folder if they belong to one, otherwise directly in `4. NPCs and Factions/`).
*   **Locations / Settlements**: `5. Locations/[Parent Location Name]/[Location Name].md` (nested in parent location folders where applicable, otherwise directly in `5. Locations/`).
*   **Player Characters**: `2. Player Characters/`.
*   **Discoveries**: `1. Campaign/Discoveries/`.
*   **Scenes**: `1. Campaign/Scenes/`.
*   **Sessions**: `3. Sessions/`.
*   **Maps**: `6. Maps/`.

### Step 5: Notify the User
Provide a clickable wikilink (`[[Name]]`) to the newly created file so the user can easily open it in Obsidian.
