---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Champion]]", "[[Flourish]]"]
prerequisites: "champion's reaction that grants an ally resistance to an enemy's damage (including the grandeur, justice, liberation, and redemption causes)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** An enemy triggered your champion's reaction since the end of your last turn.

You call upon divine power and make a weapon or unarmed Strike against the enemy who triggered your champion's reaction. The Strike deals one extra weapon damage die. If this Strike hits, until the start of your next turn, the target gains weakness equal to half your level to all Strikes made by you and your allies.

> [!danger] Effect: Blessed Counterstrike

**Source:** `= this.source` (`= this.source-type`)
