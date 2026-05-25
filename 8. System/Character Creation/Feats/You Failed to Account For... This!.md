---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Inventor]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature you can see targets you with an attack against your AC.

When your foes try to attack you, you always seem to have some outlandish invention you can pull out at the last second to protect you from whatever attack they throw at you. Describe a device you're attempting to use to protect yourself from the foe's attack—for instance, when attacked by an elemental hurricane's lightning lash Strike, you might pull out a specially grounded lightning rod from that time you tried to power an invention by harnessing a thunderstorm! Using an invention to defend in this way means that the attack roll for the triggering attack targets your Crafting DC instead of your AC.

Since you're using your Crafting DC instead of your AC, any penalties to your AC don't apply, but this doesn't remove any conditions or other effects that are causing you such penalties. For instance, if you were [[Off Guard]] and used an invention to defend against a sneak attack, you'd still take the extra precision damage if you were hit, even though the –2 penalty to AC from being off-guard wouldn't apply to your Crafting DC.

**Source:** `= this.source` (`= this.source-type`)
