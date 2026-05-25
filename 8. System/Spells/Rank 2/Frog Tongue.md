---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your tongue extends unnaturally, flicking out toward a creature within range and dealing 2d8 bludgeoning damage (basic Reflex save). On a failure, the creature is also stuck to the end of the tongue. It is [[Off Guard]] and can't move beyond the reach of your tongue. A creature can sever the tongue with a Strike that deals at least 10 slashing damage or attempt to [[Escape]] against your spell DC. The AC of the tongue is equal to your spell DC. Severing the tongue in this way deals no damage to you but ends the spell. While a creature is stuck to the end of your tongue, actions you take with the auditory trait take a –2 circumstance penalty. If you move so that the affected creature is outside of the tongue's reach, the spell ends.

**Heightened (+1)** The damage increases by 2d8.

**Source:** `= this.source` (`= this.source-type`)
