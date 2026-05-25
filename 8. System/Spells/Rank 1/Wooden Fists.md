---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Morph]]", "[[Wood]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your arms and hands swell with new growth, transforming into tree trunks twice as big as their current size. Your fists deal 1d6 bludgeoning damage, lose the nonlethal trait, and have reach.

**Heightened (3rd)** Your fists gain the magical trait and become a *striking weapon*, increasing the damage your fists deal to 2d6 bludgeoning.

**Heightened (7th)** Your fists gain the magical trait and become a *greater striking weapon*, increasing the damage your fists deal to 3d6 bludgeoning. The duration is 10 minutes.

**Heightened (9th)** Your fists gain the magical trait and become a *major striking weapon*, increasing the damage your fists deal to 4d6 bludgeoning. The duration is 1 hour.

> [!danger] Effect: Spell Effect: Wooden Fists

**Source:** `= this.source` (`= this.source-type`)
