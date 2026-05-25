---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

An invisible arm extends from you to grab and manipulate objects. The arm reaches up to 15 feet, grabs an unattended object of 1 Bulk or less, and immediately deposits it in one of your free hands or at your feet. Alternatively, it reaches up to 15 feet and performs a simple Interact action like pushing open a window, though it can't perform actions that require significant mechanical dexterity. For every 5 levels you have, the amount the hand can lift increases by 1 Bulk, and the arm's range increases by 15 feet. Being ghostly, the arm can affect ghosts, spirits, and other incorporeal entities, though in most cases, you need an awakening for this to be useful.

**Awakening** Your invisible arm can grab on to an unsuspecting target. You can modify the power's target to be 1 creature within range. You make an Deviant check{attack roll} against the creature's Fortitude DC and add the attack trait to the action. On a success, the target is [[Grabbed]] by the arm (or [[Restrained]] on a critical success). This lasts for 1 round or until the creature Escapes.

**Awakening** You summon additional ghostly arms that entwine together to push targets. You can modify the power's target to be 1 creature within range. You make an Deviant check{attack roll} against the creature's Fortitude DC and add the attack trait to the action. On a success, you can move the target 5 feet in any direction (10 feet on a critical success).

**Source:** `= this.source` (`= this.source-type`)
