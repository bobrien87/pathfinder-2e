---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]"]
cast: "1 to 3"
range: "varies"
targets: "1 or more creatures"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

This is a story of four evenly matched hunters who sought to capture a falling star. Each hunter was known by the region they came from, and this spell focuses on one of their attributes. When you cast this spell, you must choose East, North, South, or West.

- **East** was steady and optimistic. The target gains 5 temporary Hit Points and a +1 status bonus to Athletics for 1 round.
- **North** was careful and cautious. The target can Step as a free action and gains a +1 status bonus to Survival for 1 round.
- **South** was clever and cunning. The target becomes [[Concealed]] and gains a +1 status bonus to Stealth for 1 round.
- **West** was bold and competitive. The target gains a +10-foot status bonus to their land Speed and a +1 status bonus to Acrobatics for 1 round.

`pf2:1` You quickly remind yourself of the story, granting only yourself the benefit.

`pf2:2` You tell a trusted ally within 30 feet this story, granting them the benefit.

`pf2:3` You impart this tale on all of your allies within 30 feet, granting them the benefit.

> [!danger] Effect: Spell Effect: The Four Hunters

**Source:** `= this.source` (`= this.source-type`)
