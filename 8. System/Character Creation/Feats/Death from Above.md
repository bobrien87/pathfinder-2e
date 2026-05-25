---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Verduran Shadow|Verduran Shadow]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Canopy Predator, expert in Athletics"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are standing, climbing, or balancing on a surface at least 10 feet above your target.

You leap down on your target, using their body to cushion your fall and your momentum to empower your attack. Attempt an Athletics check to [[Leap]] to a space adjacent to the target. If you land adjacent to the target, compare the [[Athletics]] check result against your target's Reflex DC.

When you leap onto a creature in this way, you do not also deal damage for falling on a creature. Regardless of your result, the target is temporarily immune to your Death from Above for 1 minute.
- **Critical Success** The target falls and lands [[Prone]], reducing the falling damage you take by an amount equal to twice your level. You then can make a melee Strike against the target. The Strike gains the deadly d8 weapon property and deals an additional 1d6 bludgeoning damage. This additional damage increases to 2d6 if you are a master in Athletics, and to 3d6 if you are legendary in Athletics.
- **Success** The target is [[Off Guard]] until the beginning of your next turn, reducing the falling damage you take by an amount equal to your level. You can then make a melee Strike against the target, adding the deadly d8 weapon property to the attack.
- **Failure** You can make a Strike against the target.
- **Critical Failure** You fall prone, whether you take falling damage or not.

**Source:** `= this.source` (`= this.source-type`)
