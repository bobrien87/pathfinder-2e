---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Air]]", "[[Attack]]", "[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 or 2 creatures"
requirements: "You have at least one free hand."
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You slash your hand through the air, channeling miniature ripples of air from each finger to slice your enemy. If you have two hands free, you can target two creatures with this spell; otherwise, you target one.

Make a spell attack roll against each target's AC. This deals 2d4 slashing damage. On a critical success, a target also takes @Damage[(@item.level)d4[bleed]] damage. If you're attacking two creatures, this counts as two attacks for your multiple attack penalty, but the penalty doesn't increase until after both attacks.
- **Critical Success** The target takes double damage and 1d4 persistent bleed damage.
- **Success** The target takes full damage.

**Heightened (+1)** The damage increases by 1d4, and the persistent damage on a critical hit increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
