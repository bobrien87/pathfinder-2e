---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 willing creature"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shroud one creature in a cloak of fierce, howling winds, shielding it from attacks and making it difficult to approach. The twisting shield of wind creates difficult terrain in a @Template[burst|distance:5] surrounding the target. The target also gains a +2 circumstance bonus to its AC against physical ranged attacks, such as attacks made with bows, javelins, or slings. In addition, the sound of the swirling storms makes it easier for the target to ignore anything it doesn't want to hear, granting the target a +2 circumstance bonus to all defenses against auditory effects.

> [!danger] Effect: Spell Effect: Tempest Cloak

**Source:** `= this.source` (`= this.source-type`)
