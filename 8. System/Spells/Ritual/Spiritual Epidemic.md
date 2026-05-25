---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]", "[[Spirit]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You curse the target, sapping its spirit and leaving a contagious trap in its essence. The target must attempt a Will save. Any creature that casts a divine or occult spell on the target while it's affected is targeted by spiritual epidemic and must also attempt a Will save. The curse continues to spread in this way.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Enfeebled]] 2 and [[Stupefied 2]] for 1 round.
- **Failure** The target is enfeebled 2 and stupefied 2 for 1 minute and [[Enfeebled]] 1 and [[Stupefied 1]] permanently.
- **Critical Failure** The target is [[Enfeebled]] 3 and [[Stupefied 3]] for 1 minute and enfeebled 2 and stupefied 2 permanently.

**Source:** `= this.source` (`= this.source-type`)
