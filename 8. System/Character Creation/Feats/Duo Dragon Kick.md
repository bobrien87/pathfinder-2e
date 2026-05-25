---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Inventor]]"]
prerequisites: "construct innovation"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your construct innovation is adjacent to you.

You've practiced an impressive spin technique with your construct, automatically attacking in tandem as you launch each other through the air. You Command your construct companion to fight alongside you, after which you both [[Leap]] in the same direction, making an unarmed Strike at the start or end of the Leap; this uses your companion's actions for the turn. If the Strikes both hit the same creature, combine their damage for the purposes of resistances and weaknesses.

**Unstable Function** You spin farther and higher, though the extreme movement risks discombobulating your innovation. Add the unstable trait to Duo Dragon Kick. Increase the distance of your Leaps by 10 feet if horizontal or 5 feet if vertical.

**Source:** `= this.source` (`= this.source-type`)
