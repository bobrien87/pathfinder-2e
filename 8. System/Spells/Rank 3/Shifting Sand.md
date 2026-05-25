---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
area: "20-foot burst"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) a horizontal earthen or sandy surface within a 20-foot burst

You cause the surface to heave. The area becomes difficult terrain, and any tracks in the area are destroyed by the churning ground. Creatures standing in the area take a –1 status penalty to Acrobatics checks to [[Balance]] and [[Tumble Through]] and Athletics checks to [[High Jump]] and [[Long Jump]]. The first time each round you Sustain the Spell, you can move the churning area up to 20 feet in any direction. Creatures [[Immobilized]] by the spell are carried along with the shifting sand in the same direction, if possible. Creatures that enter or begin their turn standing in the shifting sand must attempt a Reflex save.
- **Critical Success** The creature is unaffected and ignores the area's difficult terrain and penalty to skill checks until the end of its turn.
- **Success** The creature ignores the area's penalty to skill checks until the end of its turn.
- **Failure** The creature is affected normally by the spell this turn.
- **Critical Failure** The creature becomes immobilized within the spell's area until it Escapes. If the creature was already immobilized by shifting sand, it also falls [[Prone]].

**Heightened (5th)** The status penalty increases to –2, and the spell's range increases to 60 feet.

**Heightened (7th)** The status penalty increases to –3, the spell's range increases to 60 feet, and the spell's area increases to a 30-foot burst.

**Heightened (9th)** The status penalty increases to –4, the spell's range increases to 60 feet, and the spell's area increases to a 40-foot burst.

**Source:** `= this.source` (`= this.source-type`)
