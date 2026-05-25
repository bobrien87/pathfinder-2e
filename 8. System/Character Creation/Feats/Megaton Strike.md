---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Inventor]]"]
prerequisites: "armor, construct, or weapon innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You activate gears, explosives, and other hidden mechanisms in your innovation to make a powerful attack. You make a Strike, dealing an extra die of weapon damage. If you're at least 10th level, increase this to two extra dice, and if you're at least 18th level, increase it to three extra dice. The type of Strike you can make depends on your innovation.

- **Armor** You Strike with a melee unarmed attack or a melee weapon. To use a melee weapon for this, you must have prepared it in advance with special contraptions when you make your daily preparations.
- **Construct** Your minion innovation Strikes.
- **Weapon** You Strike with your weapon innovation.

**Unstable Function** You put even more force into the Strike, though you risk stress fractures to your innovation. Add the unstable trait to Megaton Strike. The Strike deals another extra damage die, for a total of two extra dice at 4th level, three at 10th level, and four at 18th level.

**Special** If your innovation is a minion, it can take this action rather than you.

**Source:** `= this.source` (`= this.source-type`)
