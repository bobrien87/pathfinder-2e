---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transform the target creature into a harmless animal appropriate to the area, with effects based on its Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target's body gains minor features of the harmless animal. Its insides churn as they partially transform, causing it to be [[Sickened]] 1. When it recovers from the sickened condition, its features revert to normal.
- **Failure** The target transforms for 1 minute but keeps its mind. If it spends all its actions on its turn concentrating on its original form, it can attempt a [[Will]] save to end the effect immediately.
- **Critical Failure** The target is transformed into the chosen harmless animal, body and mind, for an unlimited duration.

**Source:** `= this.source` (`= this.source-type`)
