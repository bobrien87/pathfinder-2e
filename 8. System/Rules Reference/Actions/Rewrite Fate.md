---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]", "[[Mythic]]"]
cast: "`pf2:0`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You roll a skill check or saving throw and don't like the result.

Destiny, fate, or some other force bends around you as your mythic power swells, manifesting in a flash of light or visible surge of energy emanating from your body as you cast aside the chains of fate. You expend a Mythic Point and reroll the check or save with mythic proficiency, taking the new result.

**Source:** `= this.source` (`= this.source-type`)
