---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Mental]]", "[[Visual]]"]
prerequisites: "Mortal Herald Dedication, fly Speed of at least 20 feet"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You take to the skies to unveil the full magnificence of your deity's power. Fly straight upward up to your fly Speed and Interact to draw a weapon or to gesture with your hand or a worn holy symbol. Each enemy within a @Template[type:emanation|distance:60] must attempt a [[Will]] save against the higher of your class DC or spell DC. Regardless of the result, the target becomes immune to Glory on High for 1 hour.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 minute.
- **Failure** The creature is [[Blinded]] for 1 round, dazzled for 1 minute, and takes @Damage[10d6[mental]|options:area-damage] damage.
- **Critical Failure** The creature is blinded for 1 minute, dazzled for 1 hour, and takes @Damage[20d6[mental]|options:area-damage] damage.

**Source:** `= this.source` (`= this.source-type`)
