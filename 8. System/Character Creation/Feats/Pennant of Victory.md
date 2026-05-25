---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Brandish]]", "[[Commander]]", "[[Visual]]"]
frequency: "once per PT10M"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You wave your banner in victory, signaling to your allies that the fight is won. You and all allies within the aura of your commander's banner gain a +4 status bonus to attack and damage rolls, a +10-foot status bonus to all your Speeds, and 40 temporary Hit Points. These benefits last until the start of your next turn.

> [!danger] Effect: Pennant of Victory

**Source:** `= this.source` (`= this.source-type`)
