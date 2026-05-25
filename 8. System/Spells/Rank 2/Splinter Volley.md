---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Wood]]"]
cast: "2 or 3"
range: "60 feet"
targets: "1 or 2 creatures"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You launch a volley of splinters at your foes. Make a spell attack roll against a single creature. On a hit, the splinters deal 4d6 piercing damage. The splinters deal double damage on a critical hit and @Damage[(floor(@item.level/2))[bleed]] damage. You can spend a third action while casting this spell to fire splinters at two different targets instead of one. These attacks each increase your multiple attack penalty, but you don't increase your multiple attack penalty until after you make both spell attack rolls for *splinter volley*.

**Heightened (+2)** Increase the damage dealt to each target by 4d6 and the persistent bleed damage by 1.

**Source:** `= this.source` (`= this.source-type`)
