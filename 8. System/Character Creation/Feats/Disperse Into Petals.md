---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Deviant]]", "[[Magical]]", "[[Plant]]", "[[Polymorph]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You merge with the blossoms sprouting from you and disperse, becoming a visible cloud of blossoms and petals. You're amorphous. You lose any item bonus to AC and all other effects and bonuses from armor, and you use your proficiency modifier for unarmored defense. You gain resistance to physical damage equal to half your level and are immune to precision damage. You can't cast spells, activate items, or use actions that have the attack or manipulate trait. You gain a fly Speed of 10 feet. You can remain in this form for up to 1 minute. You can Dismiss this effect.

**Awakening** You can maintain your form for a longer time. You can remain in this form for up to 1 hour.

**Awakening** You've learned to harm others, even while in your blossom state. You can occupy the same space as someone else. While occupying someone else's space, you can spend 1 action to spin around in a vortex of blossoms, dealing @Damage[(floor(@actor.level/5)d4)[slashing]]{1d4 slashing} damage for every 5 levels you have to the creature, with a basic Reflex save.

**Source:** `= this.source` (`= this.source-type`)
