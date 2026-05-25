---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
duration: "until your next daily preparations"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an orb of light that sheds bright light in a 20-foot radius (and dim light for the next 20 feet) in a color you choose. If you create the light in the same space as a willing creature, you can attach the light to the creature, causing it to float near that creature as it moves. You can Sustain the spell to move the light up to 60 feet; you can attach or detach it from a creature as part of this movement.

You can Dismiss the spell. If you Cast the Spell while you already have four *light* spells active, you must choose one of the existing spells to end.

> [!danger] Effect: Spell Effect: Light

**Heightened (4th)** The orb sheds light in a 60-foot radius (and dim light for the next 60 feet).

**Source:** `= this.source` (`= this.source-type`)
