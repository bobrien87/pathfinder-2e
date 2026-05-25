---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Aura]]", "[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "emanation up to 40-feet"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You manifest an aura that prevents creatures from approaching you. When casting the spell, you can make the area any radius you choose, up to 40 feet. A creature must attempt a Will save if it's within the area when you Cast the Spell or as soon as it enters the area while the spell is in effect. Once a creature has attempted the save, it uses the same result for that casting of *repulsion*. Any restrictions on a creature's movement apply only if it voluntarily moves toward you. For example, if you move closer to a creature, it doesn't then need to move away.
- **Critical Success** The creature's movement is not restricted.
- **Success** The creature treats each square in the area as difficult terrain when moving closer to you.
- **Failure** The creature can't move closer to you within the area.

**Source:** `= this.source` (`= this.source-type`)
