---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:3`"
range: "120 feet"
duration: "10 minutes"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure several metal structures that consist of angled beams attached to one another at a central point, which can help block attacks. You creature up to three Large structures within range in unoccupied squares; each fortification is 8 feet long, 8 feet wide, and 8 feet tall. There must be enough room for a fortification in order to conjure it. A single fortification has an AC of 10 and is immune to critical hits and precision damage. It has Hardness 9, 60 Hit Points, and a BT of 30. Once a fortification is broken, it crumbles into sharp metal bits. Any creature adjacent to or sharing a space with a fortification when it is broken must attempt a Reflex save or take 2d6 persistent bleed damage.

Creatures can pass through the spaces of a fortification, though Medium and larger creatures treat these spaces as difficult terrain. A Small or smaller creature can occupy the same spaces as a fortification; doing so grants them standard cover. Similarly, a [[Prone]] Medium creature can occupy the same spaces as a fortification, gaining standard cover in the process. A Medium or smaller creature can climb a fortification with a successful DC 15 [[Athletics]] check.

**Source:** `= this.source` (`= this.source-type`)
