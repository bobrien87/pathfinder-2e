---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Vitality]]", "[[Wood]]"]
cast: "`pf2:3`"
range: "30 feet; 1 cube 20 feet on each side"
area: "20-foot cube"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an immobile, [[Invisible]] prison of hardened wood suffused with vital energy from the Forge of Creation. The cage is a 20-foot cube made of wooden branches, each a half inch thick and a half inch apart. Each creature in the area where you create the cage must attempt a Reflex save. If such a creature fails, it becomes trapped inside the cage. If it succeeds, it's pushed outside the cage into a space of its choice. If a creature in the area is too big to fit inside the prison, the spell automatically fails.

The cage has AC 10, Hardness 20, and 40 Hit Points, and it's immune to critical hits and precision damage, though it has weakness 5 to void damage. A creature capable of passing through the space between the bars (typically a Tiny creature) can leave; all others are confined within. The vitality energy suffusing the wood prevents incorporeal undead creatures from passing through the beams. Attacks with a weapon too large to fit between the bars can't pass through the cage, and the bars provide standard cover even against attacks that can pass through the gaps. Spells and most area effects (such as dragon breath) can pass through the cage uninhibited.

**Source:** `= this.source` (`= this.source-type`)
