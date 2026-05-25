---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You cause minor tremors that topple your enemies. All creatures in a @Template[emanation|distance:30] who are standing on the ground take @Damage[(floor(@actor.level/2)d6)[bludgeoning]|options:area-damage]{1d6 bludgeoning damage for every 2 levels} you have, with a [[Reflex]] save. A creature that fails its save also falls [[Prone]].

**Awakening** Your stomp also ejects large fragments from the ground. You raise up to three stone chunks from the ground in unoccupied squares in the emanation; the stones can't be adjacent to one another. The chunks are 5 feet tall, block movement, and are large enough to [[Take Cover]] behind. They have AC 10, Hardness 8, and Hit Points equal to your level. They are immune to critical hits and precision damage. A stone chunk crumbles away when it has 0 Hit Points, and all of them crumble after 1 minute or when you use Tectonic Stomp again.

**Awakening** Your stomp rattles those who fail horribly. A creature that critically fails its save is also [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
