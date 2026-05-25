---
type: action
source-type: "Remaster"
traits: ["[[Kobold]]", "[[Poison]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Requirements** You are wielding a piercing or slashing weapon

You apply your tail's venom to a piercing or slashing weapon. If your next Strike with that weapon before the end of your next turn hits and deals damage, you deal persistent poison damage equal to your level to the target.

**Source:** `= this.source` (`= this.source-type`)
