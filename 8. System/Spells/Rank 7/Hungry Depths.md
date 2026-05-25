---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Void]]", "[[Water]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "5-foot burst"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A spiral of dark, corrupted water appears in the ground, plunging open a door to the depths that seems to descend for miles. Disembodied glowing eyes and gnashing teeth spin within the vortex, consuming anything that crosses their path.

All creatures in the area take 4d8 piercing damage plus 4d4 void damage (basic Reflex save). Each time you Sustain the spell, you can increase the vortex's radius by 5 feet, to a maximum of 15 feet, or you can move the vortex up to 10 feet in a straight line. Each creature the vortex moves through takes the damage with a basic Reflex save. A creature can take damage from *hungry depths* only once per round.

If cast underwater, *hungry depths* instead fills a 40-foot-tall cylinder with a 5-foot radius.

**Heightened (9th)** The vortex deals 5d8 piercing damage and 5d4 void damage.

**Source:** `= this.source` (`= this.source-type`)
