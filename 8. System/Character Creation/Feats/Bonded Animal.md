---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Downtime]]", "[[General]]", "[[Skill]]"]
prerequisites: "expert in Nature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You forge strong connections with animals. You can spend 7 days of downtime regularly interacting with a normal animal (not a companion or other special animal) that is friendly or helpful to you. After this duration, attempt a [[Nature]] check against the animal's Will DC. If successful, you bond with the animal. The animal is permanently bonded to you until you form a bond with a different animal or do something egregious to break your bond.

A helpful animal is easier to direct. If your bonded animal is level –1, it gains the minion trait, allowing you to command it more efficiently. The maximum level of creature that can be your minion increases to 3 if you're a master in Nature and to 11 if you're legendary.

**Special** You can't have both a bonded animal and an animal companion (though you can have both a bonded animal and a pet or familiar).

**Source:** `= this.source` (`= this.source-type`)
