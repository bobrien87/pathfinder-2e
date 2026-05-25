---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Fungus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Thin hyphae grow from your feet and plunge into the earth, creating a symbiotic fungal network that attaches to plants within 30 feet and connects you to their root systems. You gain an imprecise tremorsense, allowing you to sense anything directly touching plants within that distance. If you move, the hyphae snap, and the spell ends.

**Heightened (4th)** You can control plants in the area to a small degree, allowing you to make Strikes with tree branches, exposed roots, or similarly solid plants. To do so, you use a Strike action, but you can Strike any creature you can detect with your tremorsense. These are spell attacks that deal 3d8 bludgeoning damage. Unusual plants, such as thorny vines, might deal a different type of damage at the GM's discretion. You can't make any other attacks through these plants, or take any other actions through them, other than these Strikes.

**Heightened (6th)** As 4th rank, but you can use other simple manipulate actions through the plants, including having a branch pick an object up or open a door, though more complex actions, such as picking a lock or disabling a trap, remain impossible.

**Source:** `= this.source` (`= this.source-type`)
