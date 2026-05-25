---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Cleric]]", "[[Cold]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You fling a hollow icicle filled with winter's wrath. Make a spell attack against the target's AC. The bolt deals 1d8 piercing damage and lodges in the target. At the end of the target's next turn, the bolt shatters, releasing a whirl of snow and ice that deals @Damage[(@item.rank)d12[cold]|options:area-damage] damage to the target and all adjacent creatures. The bolt can be removed with an Interact action, which causes it to melt harmlessly without detonating.
- **Critical Success** The initial bolt deals full damage and is especially well anchored, taking 2 Interact actions to remove. The bolt's explosion deals double damage.
- **Success** The bolt and its explosion deal full damage.

**Heightened (+1)** The bolt's initial damage increases by 1d8 and the explosion damage increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
