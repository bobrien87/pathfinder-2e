---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Witch]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "1 ally"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** An ally uses a reaction to grant you a beneficial effect during a combat encounter.

You're unable to leave any debts unpaid. When an ally supports you in a fight, you offer assistance in turn for the favor. The triggering ally gains 12 temporary Hit Points for 1 minute.

**Heightened (+1)** The temporary Hit Points increase by 4.

> [!danger] Effect: Spell Effect: Return the Favor

**Source:** `= this.source` (`= this.source-type`)
