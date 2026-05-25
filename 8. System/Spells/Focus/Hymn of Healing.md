---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Bard]]", "[[Composition]]", "[[Concentrate]]", "[[Focus]]", "[[Healing]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "you or 1 ally"
duration: "4 rounds (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your glorious singing mends wounds and provides a temporary respite from harm. The target gains fast healing 2. When you Cast the Spell and the first time each round you Sustain the Spell, the target gains 2 temporary Hit Points, which last for 1 round.

> [!danger] Effect: Spell Effect: Hymn of Healing

**Heightened (+1)** The fast healing and temporary Hit Points each increase by 2.

**Source:** `= this.source` (`= this.source-type`)
