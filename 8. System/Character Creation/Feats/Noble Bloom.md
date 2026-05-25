---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Emotion]]", "[[Leshy]]", "[[Mental]]", "[[Visual]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** chrysanthemum leshy heritage

**Trigger** An ally within 30 feet would be reduced to 0 Hit Points but not immediately killed.

**Frequency** once per day

Certain plants and flowers hold a reputation throughout Tian Xia for being strong and upstanding, able to weather adversity. In the moment your ally would succumb to their injuries, you stand tall and bloom proudly, radiating this strength for them. Your ally avoids being knocked out and remains at 1 Hit Point, and their [[Wounded]] condition increases by 1, as does your own.

**Source:** `= this.source` (`= this.source-type`)
