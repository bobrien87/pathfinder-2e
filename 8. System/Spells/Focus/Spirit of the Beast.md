---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Morph]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "your animal companion"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You bring out the spirit of another animal that lives within your companion. Its body morphs slightly to take on an aspect of the animal you choose to have it emulate—for example, it might grow a pair of horns if the spirit is a bull or a tail if the spirit is a monkey. When you Cast this Spell, select from one of the following aspects.

> [!danger] Effect: Spell Effect: Spirit of the Beast

- **Aspect of Might:** Your companion gains a +1 status bonus to Athletics checks, Intimidation checks to [[Demoralize]], and Fortitude saves.

- **Aspect of Swiftness:** Your companion gains a +1 status bonus to Acrobatics checks, Stealth checks to Hide or [[Sneak]], and Reflex saves.

- **Aspect of Insight:** Your companion gains a +1 status bonus to Perception checks to [[Seek]], Survival checks to Sense Direction or [[Track]], and Will saves.

**Heightened (5th)** The status bonuses increase to +2.

**Heightened (8th)** The status bonuses increase to +3.

**Source:** `= this.source` (`= this.source-type`)
