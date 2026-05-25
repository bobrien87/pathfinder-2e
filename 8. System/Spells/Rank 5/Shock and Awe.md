---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]", "[[Visual]]"]
cast: "`pf2:3`"
range: "100 feet"
area: "50-foot burst"
defense: "Will"
duration: "1 round"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create the illusion of cannons exploding, bullets and arrows flying, and magical ballistics firing, as an overwhelming torrent of information, both visual and auditory. Enemies in the area must attempt a Will save.
- **Critical Success** The enemy is unaffected.
- **Success** The target is [[Frightened]] 1.
- **Failure** The enemy is [[Frightened]] 2 and [[Stunned]] 1.
- **Critical Failure** The enemy is [[Frightened]] 3 and [[Stunned]] 2.

**Source:** `= this.source` (`= this.source-type`)
