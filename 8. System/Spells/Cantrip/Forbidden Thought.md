---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]", "[[Mental]]", "[[Psychic]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "basic Will"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You place a psychic lock in a foe's mind that prevents it from a specific action. Choose "Strike," "Stride," "Cast a Spell," or a specific action you know the creature to have (such as a dragon's magic breath). If the creature attempts that action on its next turn, it must surmount your lock to do so, causing it to take 2d6 mental damage (with a basic Will save). The target is then temporarily immune for 1 minute.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
