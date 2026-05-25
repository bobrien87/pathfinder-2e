---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause the target to see all other creatures as dire threats. The target is stricken by intense paranoia toward all creatures around it and must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target believes everyone it sees is a potential threat. It becomes [[Unfriendly]] to all creatures to which it wasn't already hostile, even those that were previously allies. It treats no one as an ally. The spell ends after 1 round.
- **Failure** As success, but the effect lasts 1 minute.
- **Critical Failure** As failure, except the target believes that everyone it sees is a mortal enemy. It uses its reactions and free actions against everyone, regardless of whether they were previously its allies, as determined by the GM. It otherwise acts as rationally as it normally does and likely prefers to attack creatures that are actively attacking or hindering it over those leaving it alone.

**Heightened (6th)** You can target up to 5 creatures.

**Source:** `= this.source` (`= this.source-type`)
