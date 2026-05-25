---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "9"
traits: ["[[Curse]]", "[[Misfortune]]", "[[Mythic]]"]
cast: "3 days"
range: "1 mile"
targets: "1 community, group, or settlement"
duration: "1 year"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You condemn your targets to violent misfortune. At the GM's discretion, you can target a group of individuals within range who serve the same cause, such as a nation's army, or who have a shared identity, such as members of a single faith. You can also choose to target a settlement that's a village or town, or a neighborhood community within a larger settlement.
- **Critical Success** As success, and the targets experience extreme accidents that threaten life, limb, or other loss. The GM adjudicates these occurrences on a case-by-case basis, but in general, the population experiences a disturbing rise in unfortunate casualties.
- **Success** The targets experience misfortune during even routine tasks that result in minor injuries. This bad luck increases when you're close; the first time each round a target within 15 feet of you attempts an attack roll or skill check, they must roll twice and use the worse result.
- **Failure** The ritual has no effect.
- **Critical Failure** You unwittingly curse yourself. For the next 24 hours, each caster must roll all attack rolls and skill checks twice and use the worse result.

**Source:** `= this.source` (`= this.source-type`)
