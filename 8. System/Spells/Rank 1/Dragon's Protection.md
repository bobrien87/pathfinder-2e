---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: "Concentrate, Sanctified, Spirit"
traditions: ""
cast: ""
range: ""
area: ""
targets: ""
defense: ""
duration: ""
trigger: ""
requirements: ""
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traits != null, "<br>**Traits** " + this.traits, "") + choice(this.traditions != null, "<br>**Traditions** " + this.traditions, "")`

`= "**Cast** " + this.cast + choice(this.trigger != null, "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null, "<br>**Requirements** " + this.requirements, "") + choice(this.range != null or this.area != null or this.targets != null, "<br>" + choice(this.range != null, "**Range** " + this.range, "") + choice(this.area != null, choice(this.range != null, "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null, choice(this.range != null or this.area != null, "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null or this.duration != null, "<br>" + choice(this.defense != null, "**Defense** " + this.defense, "") + choice(this.duration != null, choice(this.defense != null, "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** An enemy you can see would reduce this spell's target to 0 Hit Points

**Effect** The dragon intercepts, preventing the spell's target from being knocked out; the spell's target remains at 1 Hit Point. As the dragon disappears, it flies over the triggering enemy and releases its retributive breath, dealing 5d4 spirit damage to it with a [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
