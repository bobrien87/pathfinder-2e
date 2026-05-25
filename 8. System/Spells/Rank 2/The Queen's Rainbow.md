---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]"]
cast: "`pf2:3`"
area: "60-foot line"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You tell the story of the Queen of Bees and her retinue trying to pass through a rainbow on their way to visit the King of Spiders. You conjure forth a large, transparent rainbow. Creatures who enter or begin their turn in the rainbow's space must succeed at a Fortitude saving throw or become [[Dazzled]] for 1 round (or [[Blinded]] for 1 round on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
