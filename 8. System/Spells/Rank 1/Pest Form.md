---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transform into the battle form of a Tiny animal, such as a cat, insect, lizard, or rat. You can decide the specific type of animal (such as a rat or praying mantis), but this has no effect on the form's Size or statistics. While in this form, you gain the animal trait and you can't make Strikes. You can Dismiss the spell.

You gain the following statistics and abilities:

- AC = 15 + your level. Ignore your armor's check penalty and Speed reduction.

- Speed 20 feet.

- Weakness 5 to physical damage. (If you take physical damage in this form, you take 5 additional damage.)

- Low-light vision and imprecise scent 30 feet.

- Acrobatics and Stealth modifiers of +10, unless your own modifier is higher; Athletics modifier -4.

**Heightened (4th)** You can turn into a flying creature, such as a bird, which grants you a fly Speed of 20 feet.

> [!danger] Effect: Spell Effect: Pest Form

**Source:** `= this.source` (`= this.source-type`)
