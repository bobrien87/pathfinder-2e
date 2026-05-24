# Pathfinder 2e Formatting Rules

This rule document defines formatting standards for notes, rules references, spells, abilities, and campaign data in this Obsidian vault.

---

## 1. PF2e Action Icons

Always use inline PF2e action icons instead of writing out action numbers or types in body text, headings, tables, list items, or note properties.

### Icon Syntax Mapping

Use the following syntax (enclosed in backticks) to represent actions:

| Action Icon Syntax | Action Type |
| :--- | :--- |
| `` `pf2:1` `` | Single Action (1 Action) |
| `` `pf2:2` `` | Two Actions (2 Actions) |
| `` `pf2:3` `` | Three Actions (3 Actions) |
| `` `pf2:0` `` | Free Action |
| `` `pf2:r` `` | Reaction |

### Rules of Engagement

1. **Body Text & Descriptions**:
   * Replace references to action requirements in descriptions with their icon representation.
   * *Example*: "For each additional action you spend..." becomes "For each additional `pf2:1` you spend..."
   * *Example*: "As a reaction, you can..." becomes "As a `pf2:r`, you can..."

2. **Note Properties (Frontmatter)**:
   * When setting properties like `cast` or `actions`, use the icon syntax where supported or appropriate.
   * *Example*: `cast: "pf2:1"` or `cast: "pf2:2"` or `cast: "pf2:1 to pf2:3"`

3. **Tables & Checklists**:
   * Use icons in summary tables and combat logs to keep entries compact and scannable.
