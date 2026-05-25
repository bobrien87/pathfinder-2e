---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Mortal wounds that would kill other warriors are no more than the flutter of butterfly wings to you. When you are reduced to 0 Hit Points, you aren't knocked [[Unconscious]] and you don't gain the [[Dying]] condition. Until the start of your next turn, you become immune to all damage, but you also can't regain Hit Points in any way except the following. If you Strike and damage a foe on this turn, you regain @Damage[(4d8+30)[healing]] Hit Points. Otherwise, your [[Wounded]] value increases by 1 and you remain immune to damage and healing. This cycle continues until you regain Hit Points by damaging a foe or until you reach wounded 4, at which point you lose the wounded condition, fall unconscious, and gain the dying condition.

**Source:** `= this.source` (`= this.source-type`)
