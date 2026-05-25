---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Force]]", "[[Manipulate]]", "[[Wizard]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
duration: "1 minute (sustained)"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure magical shields of force to protect your allies around you. You and each ally who ends their turn within the emanation gain a +1 circumstance bonus to AC until they leave the emanation or the spell ends, whichever comes first. If an ally takes physical damage or damage from a spell or magical effect while being granted this bonus, they can choose to end the bonus for themselves as a free action to gain resistance 10 to all damage against the triggering damage. If they do, they become temporarily immune to the effects of *shielding formation* for 10 minutes. You can do the same by spending your reaction; if you do, you can't cast *shielding formation* again for 10 minutes, though you can continue Sustaining the benefits for others.

> [!danger] Effect: Spell Effect: Shielding Formation

**Source:** `= this.source` (`= this.source-type`)
