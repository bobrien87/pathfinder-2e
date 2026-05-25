---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Acid]]", "[[Air]]", "[[Cold]]", "[[Concentrate]]", "[[Earth]]", "[[Electricity]]", "[[Fire]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "1,000 feet"
area: "60-foot burst"
defense: "basic Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon the unimaginable power of world-ending cataclysms, ripping a small piece of each cataclysm and combining them together into one horrifically powerful attack. The following effects come down upon all creatures in the area. Treat the resistances of creatures in the area as if they were 10 lower for the purpose of determining the cataclysm's damage. Each creature attempts one basic Reflex save that applies to all five types of damage.

- Flesh-dissolving acid rain deals 3d10 acid damage.

- A roaring earthquake shakes and bludgeons creatures on the ground, dealing 3d10 bludgeoning damage.

- A blast of freezing wind deals 3d10 cold damage.

- Incredible lightning lashes the area, dealing 3d10 electricity damage.

- Beating winds churn across the sky, dealing 3d10 bludgeoning damage to creatures flying in the area.

- An instant tsunami sweeps over creatures in the area, dealing 3d10 bludgeoning damage with the water trait (doubled for creatures swimming in the area).

- A massive wildfire burns in a sudden inferno, dealing 3d10 fire damage.

**Source:** `= this.source` (`= this.source-type`)
