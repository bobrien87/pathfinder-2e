---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Fighter]]", "[[Press]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a single one-handed melee weapon and hold nothing else in your hands.

Using your weapon as a lever, you force your opponent to end up right where you want them. Make a Strike with a one-handed melee weapon. If the Strike hits, you can [[Reposition]] the target up to 10 feet. You can move the target through your space during this movement. Your Strike gains the following failure effect.
- **Failure** You can force the creature to move as you would on a success, but you can move the target only 5 feet.

**Source:** `= this.source` (`= this.source-type`)
