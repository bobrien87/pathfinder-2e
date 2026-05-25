---
type: feat
source-type: "Remaster"
level: "2"
prerequisites: "Prepare Elemental Medicine, expert in Occultism"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Minkai or Forest of Spirits origin

You learn Minkaian traditions about the void and know how to manipulate the five elements to fortify vitality and void energies in the body. When you [[Prepare Elemental Medicine]], you can choose to use [[Occultism]] check instead of the usual skills. If you do, the medicine also grants the recipient resistance 2 and weakness 2 based on the element you chose. A wood, earth, or water elemental medicine grants resistance to void damage and weakness to vitality damage, and a living recipient loses its immunity to vitality damage for the duration. A fire or metal elemental medicine grants resistance to vitality damage and weakness to void damage, and an undead recipient loses its immunity to void damage for the duration.

If you're a master in Occultism, increase the resistance and weakness to 4. If you're legendary, instead increase them to 8.

**Source:** `= this.source` (`= this.source-type`)
