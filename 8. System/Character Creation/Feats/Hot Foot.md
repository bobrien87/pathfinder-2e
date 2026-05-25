---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pistol Phenom|Pistol Phenom]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Pistol Phenom Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded firearm.

Using a carefully aimed shot, you make a creature "dance." You shoot at the ground near a target's feet, causing them to react involuntarily; even mindless creatures have unconscious responses to dodge an attack, and you can capitalize off those uncontrollable reflexes to achieve your aim. As they dance to the sweet tune of your pistol's retort, you ensure your foe can't use whatever nasty surprise they had planned in store for you and your allies. Make an attack roll against the Reflex DC of a target creature within your firearm's first range increment.
- **Critical Success** The creature can't use reactions, is [[Off Guard]], and takes a -2 circumstance penalty to Reflex saves. These effects last until the start of its next turn.

> [!danger] Effect: Hot Foot (Critical Success)
- **Success** The creature can't use reactions until the start of its next turn.

**Source:** `= this.source` (`= this.source-type`)
