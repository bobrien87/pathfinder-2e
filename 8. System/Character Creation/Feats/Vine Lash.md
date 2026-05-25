---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Deviant]]", "[[Magical]]", "[[Plant]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a free hand.

A long vine sprouts from your arm, which you can temporarily wield like a whip. Make a melee Deviant check{attack roll} against a creature within 30 feet. If you succeed, the vine deals @Damage[(floor(@actor.level/2)d6)[slashing]] damage for every 2 levels you have to the target, or double damage on a success.

**Awakening** The vine coils around your foes, squeezing them lifeless. On a successful hit, the target is [[Grabbed]] by the vine. The DC to [[Escape]] the vine is equal to your Class DC or Spell DC, whichever is higher. Each round on your turn, if the target is still grabbed, the vine squeezes them, dealing @Damage[(floor(@actor.level/2)d6)[bludgeoning]] damage for every 2 levels you have.

**Awakening** Rather than lash at your foes with a single vine, dozens of writhing vines emerge from your hands, lashing all creatures in a large area. You can use Vine Lash as a 2-action activity to damage all creatures in a @Template[cone|distance:30], with a [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
