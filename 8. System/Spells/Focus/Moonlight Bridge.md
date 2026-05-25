---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Light]]", "[[Manipulate]]", "[[Oracle]]"]
cast: "`pf2:2`"
range: "30 feet"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon a bridge of radiant, shimmering moonlight.

The 10-foot-wide span must start at the ground on a point within range, and it extends as a horizontal plane, either in a straight line or at any angle up to 45 degrees upward or downward, for up to 120 feet.

This bridge has AC 10, Hardness 30, and 60 Hit Points, and it's immune to all damage (except force, spirit, and damage from Strikes with the [[Ghost Touch]] property rune). You and your allies can cross the bridge normally, but other creatures simply pass through it if they try to do so. The bridge blocks physical, ethereal, and incorporeal attacks from crossing, whether from above or below.

You can Dismiss the spell.

**Heightened (+1)** The length of the bridge increases by 20 feet, and its Hit Points increase by 20, and you can increase the width of the span by up to an additional 5 feet.

**Source:** `= this.source` (`= this.source-type`)
