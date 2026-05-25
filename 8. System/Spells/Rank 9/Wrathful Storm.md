---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Air]]", "[[Cold]]", "[[Concentrate]]", "[[Electricity]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "800 feet"
area: "400-foot burst"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A massive storm cloud forms in the air above the area, spreading rain and gales. The wind imposes a –4 circumstance penalty to physical ranged attacks. The air in the area is greater difficult terrain for flying creatures. When you Cast this Spell and the first time each round you Sustain it on subsequent rounds, you can choose one of the following storm effects. You can't choose the same effect twice in a row.

- **Blizzard** The driving snow deals 4d8 cold damage to each creature in or below the storm with no save. Everything in or beneath the cloud is [[Concealed]] by driving snow and any ground is difficult terrain.
- **Hail** Each creature in or below the storm takes 4d10 bludgeoning damage with a basic Fortitude save.
- **Lightning** Choose up to 10 creatures in or below the storm to be struck by lightning. Each of them takes 7d6 electricity damage with a basic Reflex save.
- **Tornado** A roughly cylindrical whirlwind appears in or below the cloud in a 30-foot radius. Each creature in the whirlwind is thrown 40 feet upward.

> [!danger] Effect: Spell Effect: Wrathful Storm

**Heightened (10th)** The range increases to 2,000 feet and the cloud is a 1,000-foot burst.

**Source:** `= this.source` (`= this.source-type`)
