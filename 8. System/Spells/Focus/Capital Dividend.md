---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Wizard]]"]
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You would be reduced to 0 Hit Points but not immediately killed.

Through diet and other strict regimens, you've fortified your body as Kalistrade's teachings have fortified your mind. You remain at 1 Hit Point, and your skin takes on a slight warm glow.

For the next minute, any time you would regain Hit Points from a healing effect, this magic amplifies the effect, and you regain an additional 8 Hit Points.

**Heightened (+1)** The additional healing increases by 2 Hit Points.

> [!danger] Effect: Spell Effect: Capital Dividend

**Source:** `= this.source` (`= this.source-type`)
