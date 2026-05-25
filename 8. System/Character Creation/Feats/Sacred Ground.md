---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Consecration]]", "[[Divine]]", "[[Exploration]]"]
prerequisites: "harmful font or healing font"
frequency: "once per PT10M"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You pray continuously for 1 minute to call a subtle shadow of your deity's realm over a @Template[burst|distance:30] centered on you. It lasts for 10 minutes, and a creature that remains in the area for the entire 10 minutes regains Hit Points equal to your level. If you have a healing font, this activity has the healing and vitality traits and heals living creatures. If you have a harmful font, this activity has the healing and void traits and heals undead creatures (or other creatures with void healing). Clerics with Versatile Font can choose either or both. It can't damage creatures in any case.

**Source:** `= this.source` (`= this.source-type`)
