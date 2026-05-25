---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Summon]]"]
cast: "`pf2:3`"
range: "30 feet"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

While deities jealously guard their most powerful servants from the summoning spells of those who aren't steeped in the faith, this spell allows you to conjure an inhabitant of the Outer Sphere with or without the deity's permission. You summon a common celestial, fiend, or monitor of level –1. You can choose to instead summon a common animal of level –1 that hails from the Outer Sphere; you can choose for this animal to gain the celestial and holy traits, the fiend and unholy traits, or the monitor trait. It's anathema to summon a servitor if it has a holy or unholy trait that isn't allowed for your deity's sanctification. For example, Sarenrae's sanctification is "can choose holy," so you couldn't summon an unholy creature, and Pharasma's is "none," so you couldn't summon a holy or unholy creature. The GM might determine that your deity restricts specific types of creatures further, making it anathema to summon them as well.

**Heightened (2nd)** The creature can be level 1 or lower.

**Heightened (3rd)** The creature can be level 2 or lower.

**Heightened (4th)** The creature can be level 3 or lower.

**Source:** `= this.source` (`= this.source-type`)
