---
type: action
source-type: "Remaster"
traits: ["[[Arcane]]", "[[Wizard]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Requirements** Your bonded item is on your person.

You expend the magical power stored in your bonded item. During the current turn, you can cast one spell you prepared today and already cast, without spending a spell slot. You must still Cast the Spell and meet the spell's other requirements.

**Source:** `= this.source` (`= this.source-type`)
