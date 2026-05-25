---
type: action
source-type: "Remaster"
traits: ["[[Arcane]]", "[[Concentrate]]"]
cast: "`pf2:r`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A creature deals damage to you with a spell

**Effect** You gain a measure of revenge immediately by twisting the magic used by the triggering creature. Spend a Mythic Point. The triggering creature takes 6d8 force damage, with a [[Will]] save saving throw against either your class DC or spell DC using mythic proficiency, whichever is higher. At 14th level, and every 2 levels thereafter, this damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
