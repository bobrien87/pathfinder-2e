---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Fungus]]", "[[Magical]]", "[[Poison]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You create a miasma of spores. These spores fill a @Template[burst|distance:20] within 100 feet and remain for 1 round per level you have. All creatures within the spores become [[Concealed]], and all creatures outside the spores become concealed to creatures within it. You can see through the spores without difficulty. You can Dismiss the spores.

**Awakening** The spores smell disgusting. Creatures in the area are [[Sickened]] 1 for as long as they remain in the area, plus 2 rounds.

**Awakening** The spores are toxic. The miasma deals @Damage[(floor(@actor.level/2))[poison]|options:area-damage] damage per 2 levels you have to creatures in the area when you Release Spores, to creatures who begin their turn in the area, and to creatures who enter the area.

**Source:** `= this.source` (`= this.source-type`)
