---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 willing creature"
duration: "1 minute or until expended"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Reinforcing veins of ore run through the target's arm, letting it ward off blows with its bare skin. It can use the Raise a Shield action to instead raise its arm, gaining a +2 circumstance bonus to AC. It can Shield Block with its Raised arm as well; when it does, the target reduces the damage as if it had a shield with Hardness 4 and 15 Hit Points. This shield doesn't have a Broken Threshold, and the spell ends if the shield's Hit Points are expended.

This spell doesn't modify the target's unarmed attacks and can't be used to make a shield bash Strike. Casting or coming under the effects of this spell also counts as using a metallic item with regards to anathema.

**Heightened (+2)** The Hardness increases by 4, and the Hit Points increase by 15.

**Source:** `= this.source` (`= this.source-type`)
