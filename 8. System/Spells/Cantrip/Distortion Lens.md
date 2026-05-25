---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Psychic]]"]
cast: "`pf2:1`"
range: "30 feet"
area: "5-foot square"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a magical lens that distorts space as best suits you. You create the lens in an area in range, even suspended in midair. If your or an ally's ranged attack passes through the lens, the attack gains an additional 10 feet of range; if an enemy's ranged attack would pass through the lens, it requires an additional 10 feet of range to move through, though the enemy knows before using its ability whether the interference puts the target out of range. An ally whose space overlaps the lens can increase the range of its ranged attacks, but an enemy whose space overlaps the lens doesn't reduce the range of its ranged attacks.

The first time each round you Sustain the Spell, you can choose to relocate it to another area within range. The lens disappears if you cast *distortion lens* again.

**Heightened (+3)** The lens increases or decreases the range of abilities by an additional 5 feet.

**Source:** `= this.source` (`= this.source-type`)
