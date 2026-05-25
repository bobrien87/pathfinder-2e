---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Aura]]", "[[Dragonet]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You call nearby wild dragonets to swarm to your side. The flock grants you 25 temporary Hit Points that last up to 1 minute. The flock disperses and the effect ends when the temporary Hit Points are gone, the minute elapses, or you Dismiss Form a Flock. As long as you're surrounded by your flock, you gain weakness 5 to area and splash damage and have a flock aura in a @Template[type:emanation|distance:10]. Enemies in this aura are [[Dazzled]].

When you use Form a Flock and while it lasts, you can take the Acrid Barrage action.

**Source:** `= this.source` (`= this.source-type`)
