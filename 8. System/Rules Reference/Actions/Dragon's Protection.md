---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Sanctified]]", "[[Spirit]]"]
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An enemy you can see would reduce this spell's target to 0 Hit Points

**Effect** The dragon intercepts, preventing the spell's target from being knocked out; the spell's target remains at 1 Hit Point. As the dragon disappears, it flies over the triggering enemy and releases its retributive breath, dealing 5d4 spirit damage to it with a [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
