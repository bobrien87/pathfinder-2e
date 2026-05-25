---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:3`"
duration: "sustained"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You extend your senses through a multitude of crawling and flying creatures. You create a crawling swarm in your square. You can hear through the swarm as if using your normal auditory senses. When you Cast this Spell and the first time you Sustain it each round, you can move the swarm 10 feet along the ground in any direction. The swarm has AC 15 and a +0 bonus to its saves. Any damage dealt to the swarm destroys it and ends the spell.

**Heightened (3rd)** The swarm has a climb Speed of 10 feet.

**Heightened (5th)** The swarm has a fly Speed of 10 feet. You can see through the swarm using your visual senses.

**Heightened (7th)** The swarm gains a 10-foot status bonus to its Speeds.

**Source:** `= this.source` (`= this.source-type`)
