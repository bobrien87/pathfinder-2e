---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Primal]]", "[[Sonic]]", "[[Tanuki]]"]
prerequisites: "Ponpoko"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whether it's because you play especially vigorously or are simply off-key, the music of your belly drum can physically wound your foes. You deal @Damage[(ceil(@actor.level/2))d4[sonic]|options:area-damage] damage to all creatures in a @Template[type:cone|distance:30], with a [[Fortitude]] save equal to your spell DC or class DC, whichever is higher. Such vigorous drumming does leave your belly a bit sore, though, preventing you from using this ability again for 1d4 rounds.

At 15th level and every 2 levels thereafter, the damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
