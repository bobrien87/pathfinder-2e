---
type: action
source-type: "Remaster"
traits: ["[[Magical]]", "[[Spellshot]]"]
cast: "`pf2:2`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You imprint a bullet with a field of disruptive energy built upon your magical signature, disrupting the magic of whatever it hits. Make a firearm or crossbow Strike against a foe you can see. If you hit, you attempt to counteract a spell effect active on the target (your choice, or the highest-level effect if you don't choose). Your counteract rank is equal to half your level (rounded up), and your counteract check modifier is equal to your class DC – 10.

**Source:** `= this.source` (`= this.source-type`)
