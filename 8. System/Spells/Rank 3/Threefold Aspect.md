---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "1 minute"
duration: "until the next time you make your daily preparations"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

This spell allows you to change between three versions of yourself of different ages: a maiden (young adult), a mother (adult), or a matriarch (elderly). Choose one when you Cast the Spell. While the spell lasts, you can change the age to any of the three or to your natural age by Sustaining the spell. Your form always looks like you regardless of the age, and creatures who know you still recognize you and can tell your age is different.

*Threefold aspect* alters your physical appearance and personality to present an authentic version of yourself at various ages. This grants you a +4 status bonus to Deception checks to pass as the chosen age, and you can add your level as a proficiency bonus to these checks even if you're untrained. Furthermore, unless a creature specifically uses a [[Seek]] action or otherwise carefully examines you, it doesn't get a chance to notice that you aren't at your true age. You can Dismiss this spell.

**Source:** `= this.source` (`= this.source-type`)
