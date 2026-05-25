---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "one club or staff you're wielding"
duration: "1 minute"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transform a bludgeon into a fearsome torch suited to casting undead into the afterlife. One end of the weapon ignites, becoming wreathed in blue flame. While you wield the target weapon, it becomes a +1 weapon, gains the versatile fire trait, and sheds light as brightly as a torch. Whenever you successfully Strike a creature with the weapon, you can Dismiss the spell as a free action to deal 1d6 persistent fire damage to the target; if the target is undead, increase the persistent damage dice to d8s.

> [!danger] Effect: Spell Effect: Funeral Flames

**Heightened (+2)** The persistent fire damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
