---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pistol Phenom|Pistol Phenom]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Pistol Phenom Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded one-handed firearm.

Your flair keeps foes' attention, as your motions with your gun draw your foes into a deadly game. As you toy with them and performatively brandish your weapon, you build their tunnel vision, leaving them trapped in a perceptual gauntlet of your own making. Attempt a Performance check against the Will DC of a single target within your one-handed firearm's first range increment.
- **Critical Success** The target takes a –2 status penalty to attack rolls against creatures other than you until the beginning of your next turn.
- **Success** The target takes a –1 status penalty to attack rolls against creatures other than you until the beginning of your next turn.

> [!danger] Effect: Gunpowder Gauntlet

**Source:** `= this.source` (`= this.source-type`)
