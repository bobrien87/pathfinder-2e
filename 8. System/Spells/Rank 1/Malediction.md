---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Aura]]", "[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "10-foot emanation"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You incite distress in the minds of your enemies, making it more difficult for them to defend themselves. Enemies in the area must succeed at a Will save or take a –1 status penalty to AC as long as they're in the area.

Once per round on subsequent turns, you can Sustain the spell to increase the emanation's radius by 10 feet and force enemies in the area that weren't yet affected to attempt a saving throw.

Malediction can counteract benediction.

> [!danger] Effect: Spell Effect: Malediction

**Source:** `= this.source` (`= this.source-type`)
