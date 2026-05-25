---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Concentrate]]", "[[Fortune]]", "[[Monk]]"]
prerequisites: "Monastic Archer Stance, Stunning Blows"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Monastic Archer Stance]] and wielding a bow usable with that stance.

You string three arrows to your bow and fire them all at once. Make three ranged Strikes against a single target with the required weapon, each using your current multiple attack penalty, and you take an additional –2 penalty. This counts as two attacks when calculating your multiple attack penalty, and you combine the attacks' damage for the purpose of resistances and weaknesses. Your Stunning Blows benefit applies to Triangle Shot, even though it isn't a Flurry of Blows. If all three Strikes hit, the target takes 3d6 persistent,bleed damage.

**Source:** `= this.source` (`= this.source-type`)
