---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

In the darkest hour of the night, a fearsome and terrible steed arrives as a gift from a powerful daemonic patron. You gain an apocalypse mount, which is loyal and follows your commands as long as you work to spread death and destruction. Your apocalypse mount can be any mature animal companion with the mount special ability, though it is obviously touched by daemonic forces. Choose whether your apocalypse mount is a nimble or savage animal companion. During an encounter, even if you don't use the Command an Animal action, your apocalypse mount can still use 1 action on your turn to Stride or Strike.

You also gain the anathema "You forswear any plans to cheat death or build something that will last beyond your own death." If you break this anathema, you lose access to abilities granted by this archetype until you atone or make amends.

**Special** If you already have an animal companion with the mount special ability, it becomes your apocalypse mount as daemonic energies infuse its form. In such a case, one of your companion's unarmed attacks increases one die size.

Apocalypse Rider

**Source:** `= this.source` (`= this.source-type`)
