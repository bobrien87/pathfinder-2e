---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Cantrip]]", "[[Concentrate]]", "[[Electricity]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure up a length of sharp copper filament humming with electrical current that strikes out at your foe. The wire deals 1d4 slashing damage and 1d4 electricity damage, depending on your spell attack roll against the target's AC.
- **Critical Success** The target takes double damage and @Damage[(ceil(@item.rank / 2))d4[persistent,electricity]] damage.
- **Success** The target takes full damage.
- **Failure** The target takes the electricity damage, but not the slashing damage.
- **Critical Failure** The target is unaffected.

**Heightened (+2)** The slashing damage, initial electricity damage, and persistent electricity damage on a critical hit each increase by 1d4.

**Source:** `= this.source` (`= this.source-type`)
