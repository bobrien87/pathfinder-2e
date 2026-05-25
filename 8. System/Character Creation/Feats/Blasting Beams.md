---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a free hand.

A directed beam of heat or an arc of lightning is one of the simplest ways to project energy. You fire a blast or beam from one hand. Make an Deviant check{attack roll} against a creature within 30 feet. If you succeed, the beam deals @Damage[(floor(@actor.level/2)d6)[@actor.flags.system.deviantAbilities.dragon.damageType]]{1d6 damage for every 2 levels} you have to the target, or double damage on a critical success.

**Awakening** Your beams blast through targets. Instead of making an attack roll to damage a single creature within 30 feet, you can use Blasting Beams as a 2-action activity to damage all creatures in a @Template[line|distance:60], with a [[Reflex]] save.

**Awakening** You can choose to launch smaller, quicker beams from your eyes instead. These deal @Damage[(floor(@actor.level/2)d4)[@actor.flags.system.deviantAbilities.dragon.damageType]]{d4s} instead of d6s, but the attack has the agile trait, and you don't need a hand free to make it, though your eyes must be uncovered.

**Source:** `= this.source` (`= this.source-type`)
