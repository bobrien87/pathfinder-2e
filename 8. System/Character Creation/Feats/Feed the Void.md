---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Deviant]]", "[[Extradimensional]]", "[[Magical]]", "[[Mental]]", "[[Spirit]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The void within you manages to manifest itself temporarily, a black hole opening over your heart and threatening to draw everything in. A @Template[type:cone|distance:60] becomes filled with screaming winds that rush in toward you. All creatures in the cone must attempt a Fortitude saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature is pulled 10 feet toward you.
- **Failure** The creature is pulled 20 feet toward you.
- **Critical Failure** The creature is pulled 30 feet toward you.

Creatures that would be pulled into your square contact the void, which deals @Damage[5d6[spirit]|options:area-damage] damage with no saving throw, and are then spat back out in a square adjacent to you of your choice. At 12th level, and every 2 levels thereafter, the damage increases by 1d6.

**Awakening** The void feeds upon the creature's spirit, transferring you some of their vitality. If one or more creatures are pulled into the void, you gain temporary Hit Points equal to the level of the highest-level creature pulled in. These temporary Hit Points last for 10 minutes.

**Awakening** The void's suction draws in heat and light as well. The first 30 feet of the cone becomes covered in ice as temperatures drop, making the area difficult terrain, and is also plunged into darkness, with the effects of darkness heightened to half your level. Both effects last until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
