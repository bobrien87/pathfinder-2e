---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:3`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Requirements** you are holding your spellbook

**Effect** Spend a Mythic Point, and then Cast a Spell directly from your spellbook. The spell you cast must be one that takes one or two actions to cast, and it's automatically heightened to a rank equal to half your level. Use mythic proficiency to determine any attack rolls or spell DCs.

**Source:** `= this.source` (`= this.source-type`)
