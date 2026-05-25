---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "1 to 3"
range: "touch"
targets: "1 creature"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your touch projects a surge of magic that launches your target safely away. Make a melee spell attack at mythic proficiency against your target's AC. If you hit, you deal 1d6 bludgeoning damage, and you launch the target into the air and away from you; the target takes falling damage as normal. The number of actions you spend while Casting the Spell determines the damage dealt by your touch and how far the target is launched.

`pf2:1` The target is launched 10 feet into the air and knocked back 10 feet.

`pf2:2` Your touch deals 2d6 bludgeoning damage instead. The target is launched 20 feet into the air and pushed back 10 feet.

`pf2:3` Your touch deals 2d6 bludgeoning damage instead. The target is launched 30 feet into the air and pushed back 20 feet.

**Heightened (4th)** The initial damage increases by 1d6, and all distances increase by 10 feet for the 1-action version or 20 feet for the 2- and 3-action versions.

**Heightened (6th)** The initial damage increases by 2d6, and all distances increase by 20 feet for the 1-action version or 60 feet for the 2- and 3-action versions.

**Heightened (8th)** The initial damage increases by 3d6, and all distances increase by 30 feet for the 1-action version or 100 feet for the 2- and 3-action versions.

**Source:** `= this.source` (`= this.source-type`)
