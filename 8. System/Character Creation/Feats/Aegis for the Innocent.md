---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "14"
traits: ["[[Manipulate]]", "[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your nimbus is active.

You transfer a portion of your divine spark to an ally, temporarily dimming your nimbus to encase an ally in a barrier of light that repels attackers. Select a willing creature within the bright light of your nimbus. You surround the target in a protective barrier of light; this is a @Template[type:emanation|distance:10] centered on the target. This barrier lasts for 1 minute, or until you Dismiss it. While the Aegis of the Innocent is active, the area of your nimbus is halved.

The target gains a +1 status bonus to AC. Any enemy within the barrier, or entering the barrier, must attempt a [[Fortitude]] save saving throw against your class DC or your spell DC. A creature needs to attempt this save only once each round.

> [!danger] Effect: Aegis for the Innocent
- **Critical Success** The creature is unaffected.
- **Success** The creature becomes [[Dazzled]] for 1 round and treats the space within the barrier as difficult terrain.
- **Failure** The creature becomes dazzled for 1 minute, is pushed 10 feet, and treats the space within the barrier as difficult terrain. If a creature would be pushed into a solid barrier or another creature, it stops at that point and takes @Damage[2d6[bludgeoning]|options:area-damage] damage.
- **Critical Failure** As failure, but the creature is also [[Blinded]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
