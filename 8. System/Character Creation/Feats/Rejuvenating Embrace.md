---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Sarangay]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You rejuvenate your spirit by taking your rest where Mother Earth embraces Father Moon. When you rest outdoors, you can choose one of the following benefits, which lasts until your next sleep cycle and can't be changed.

- **Father Moon's Vigilance** While sleeping, you don't take a penalty to Perception rolls for being [[Unconscious]].
- **Mother Earth's Care** After 8 hours of sleep, you regain additional @Damage[(@actor.level + @actor.system.abilities.con.mod)[healing]]{Hit Points} equal to your Constitution modifier plus your level.

**Source:** `= this.source` (`= this.source-type`)
