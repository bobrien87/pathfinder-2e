---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
traits: ["[[Trial]]"]
cast: "1 day"
source: "Pathfinder Lost Omens Tian Xia World Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

To simply kill the magical beasts who populate Tian Xia is needless and wasteful. The gods reward a hunter who seeks to truly understand their prey, approaching the creatures on their own level and seeking to gain their strength. Powdering the bones of strong beasts, for use in a soup or wine, is often the first step in the process of capturing part of their power.

Using weapons is anathema to this ritual and immediately ends its benefits. If the ritual is ended in this way, you must conduct an [[Atone]] ritual before attempting this ritual again.
- **Critical Success** As success, except you can defeat three enemies that are only one size larger than you instead.
- **Success** The power begins to take root. Once you've defeated an enemy two or more sizes larger than you in single combat, you gain the [[Titan Wrestler]] feat.
- **Failure** You drink the soup or wine, but the understanding eludes you.
- **Critical Failure** The drink contains shards of bone you didn't grind down properly. You're [[Sickened]] 2 for 1 week, during which the condition can't be reduced.

**Source:** `= this.source` (`= this.source-type`)
