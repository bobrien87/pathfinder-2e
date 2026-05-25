---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Flourish]]", "[[Monk]]", "[[Occult]]", "[[Water]]"]
prerequisites: "Waterfowl Stance"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in Waterfowl Stance and are wielding a monk weapon from the sword group.

Ganhil developed this technique through observing the sharp-beaked darters fishing Prada Hanam's waters, seeking to match their speed and suppleness with the elemental flash of his blade. Make a melee Strike with the required weapon against each enemy in a @Template[type:line|distance:15] as razor-sharp shadows of water surge from your blade. Each attack counts toward your multiple attack penalty, but you do not increase your penalty until you have made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
