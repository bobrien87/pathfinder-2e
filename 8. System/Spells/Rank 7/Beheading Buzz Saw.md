---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
area: "60-foot line"
defense: "Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You compress molten scraps pulled from the Plane of Metal into a spinning disc with gruesome blades protruding from its edges. It wheels forward, slicing through anyone in its path. Each creature in the area takes 5d10 slashing damage and 4d6 persistent bleed damage, with a Reflex save.
- **Success** The creature is unaffected.
- **Failure** The creature takes full damage.
- **Critical Failure** The creature takes double damage. If the creature has a head, it must succeed at a [[Fortitude]] save or be decapitated; this kills any creature except ones that don't require a head to live. For creatures with multiple heads, this usually kills the creature only if you sever its last head. This second save has the death and incapacitation traits.

**Heightened (+1)** The slashing damage increases by 1d10, and the persistent bleed damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
