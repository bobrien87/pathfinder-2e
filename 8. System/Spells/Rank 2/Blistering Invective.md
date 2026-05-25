---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A heap of insults and invectives spew from your mouth-words so devastating your foes burn from the intensity of your diatribe. Your words deal 2d6 persistent fire damage, and the target must attempt a Will save. If the target doesn't understand the language or you're not speaking a language, it gains a +4 circumstance bonus to its save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half the persistent fire damage.
- **Failure** The target becomes [[Frightened]] 1 and takes the full persistent fire damage.
- **Critical Failure** The target becomes [[Frightened]] 2 and takes double the persistent fire damage.

**Heightened (+2)** You can target two additional creatures, and the persistent damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
