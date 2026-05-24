# Pathfinder 2e Source Priority & Types Rule

This rule defines the sources to reference for **Rules** and **Lore**, their relative priorities, confirmation guidelines, and metadata tagging rules.

---

## 1. Source Types and Priorities

Sources in this vault are split into two distinct domains: **Rules** (how things work mechanically) and **Lore** (what is true in the setting/campaign).

### Rules Sources
When referencing game mechanics, rules, character options, spells, or items:

| Priority | Source | Confirmation Required? |
| :--- | :--- | :--- |
| **1** | **Remaster Core Books** (*Player Core*, *GM Core*, *Monster Core*, *Player Core 2*) | **No** (Directly use) |
| **2** | **Archives of Nethys** (Official Online Reference) | **No** (Directly use) |
| **3** | **Legacy Rulebooks** (*Core Rulebook*, *Advanced Player's Guide*, *Bestiaries 1-3*, *Gamemastery Guide*) | **⚠️ YES** - Always ask the user for confirmation before referencing legacy rules. |

---

### Lore Sources
When referencing the setting, campaign history, NPC backgrounds, locations, or plots:

| Priority | Source | Confirmation Required? |
| :--- | :--- | :--- |
| **1** | **Played Vault Data**<br>- Sessions where `played = true`<br>- PC Notes & NPC Notes<br>- Discoveries where `discovered = true`<br>- Scenes where `played = true` | **No** (Directly use) |
| **2** | **Unplayed Vault Data** | **No** (Directly use) |
| **3** | **Notes in `9. Sources` folder** where `priority = Primary` | **No** (Directly use) |
| **4** | **Notes in `9. Sources` folder** where `priority = Secondary` | **⚠️ YES** - Always ask the user for confirmation before using. |
| **5** | **Remaster Core Books** (setting lore and world info) | **⚠️ YES** - Always ask the user for confirmation before using. |

---

## 2. Metadata Tagging: `source-type` Property

For files in this vault containing rules, items, spells, monsters, or lore, the `source-type` frontmatter property must be set as follows:

* **`source-type: Remaster`**: If the content is taken from or based on a Pathfinder 2e Remaster source.
* **`source-type: Legacy`**: If the content is taken from or based on a Pathfinder 2e Legacy source.
* **No `source-type` property**: If the content is specific to the campaign and created by you (the Agent) or the user (e.g. session notes, custom NPCs, campaign-specific items, homebrew).

### Frontmatter Examples:

**Remaster Note:**
```yaml
---
type: spell
source-type: Remaster
---
```

**Legacy Note:**
```yaml
---
type: creature
source-type: Legacy
---
```

**Campaign Specific / Homebrew / Session Note:**
```yaml
---
type: session
played: true
---
```
