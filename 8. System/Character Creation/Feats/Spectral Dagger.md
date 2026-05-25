---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Splinter Of Finality|Splinter Of Finality]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Manipulate]]"]
prerequisites: "You have a hand free and aren't already wielding a spectral dagger."
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By touching the splinter of finality in your neck, you conjure a [[Spectral Dagger]] into your hand that resembles the splinter wrapped in a crude hilt. This weapon acts like a *+1 ghost touch dagger*, and each successful Strike with it deals 1 additional spirit damage. If the attack is a critical hit, this damage increases to 1d6.

If the *spectral dagger* ever leaves your hand, it vanishes and you must spend an action to conjure it again. If this occurs as the result of you making a ranged thrown Strike with the dagger, you resolve the attack before the weapon vanishes.

You can increase the power of your *spectral dagger* with runes like you can other weapons, transferring the rune from a *runestone* or other weapon by meditating over the rune as a downtime activity that takes 1 day.

**Source:** `= this.source` (`= this.source-type`)
