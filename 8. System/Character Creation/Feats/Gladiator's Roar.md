---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Gladiator|Gladiator]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Sonic]]"]
prerequisites: "Gladiator Dedication, master in Intimidation"
frequency: "once per day"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can project your voice into a high-pitched screech that damages your foes. Your roar can be heard twice as far as normal, and creatures within a @Template[cone|distance:15] take @Damage[6d10[sonic]|options:area-damage] damage and must attempt a [[Fortitude]] save against your class DC or spell DC, whichever is higher. If your Gladiator's Roar triggers Play to the Crowd, you gain a +2 status bonus to your Performance check to do so.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and becomes [[Frightened]] 1
- **Failure** The creature takes full damage and becomes [[Frightened]] 2.
- **Critical Failure** The creature takes double damage, becomes [[Frightened]] 3, and is [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
