---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Spellshape]]"]
cast: "`pf2:r`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** Your hierophant Casts a Spell

**Effect** Interceding directly in your hierophant's affairs, you grant them additional magic. They do not expend the spell slot, usage, or Focus Point.

**Source:** `= this.source` (`= this.source-type`)
