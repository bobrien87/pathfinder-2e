---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Illusion]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 hour"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target consistently detects one thing as another, can't detect something that's there, or detects something that's not there, though it doesn't alter their beliefs. You choose which of these effects applies, and you determine the specifics of the hallucination. For example, you could make the target see all elves as humans, be unable to detect the presence of their brother, see their beloved good luck charm on their person even when it isn't, or see a tower in the center of town.

The target can attempt an initial Will save, with effects below. They also receive a Will save to disbelieve the hallucination every time they [[Seek]] or directly interact with the hallucination. For example, the target could attempt to disbelieve the hallucination each time they interacted with an elf, bumped into their brother accidentally, tried to check their charm, or studied the tower. The target can attempt to disbelieve with a large circumstance bonus in situations determined by the GM, such as if the target attempted to climb the nonexistent tower.
- **Critical Success** The creature is unaffected.
- **Success** The creature perceives what you chose until it disbelieves, but it knows what the hallucination is.
- **Failure** The creature perceives what you chose until it disbelieves.
- **Critical Failure** The creature perceives what you chose until it disbelieves, and it trusts its false senses, taking a -4 circumstance penalty to saves to disbelieve.

**Heightened (6th)** Choose to either target up to 10 creatures or change the spell's duration to until your next daily preparations.

**Heightened (8th)** Choose to either target any number of creatures or change the spell's duration to unlimited.

**Source:** `= this.source` (`= this.source-type`)
