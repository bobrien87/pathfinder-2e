---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Ranger]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 willing living creature or 1 undead creature"
defense: "basic Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth a magical mist that envelops a creature. The mist restores 2d8 Hit Points to a target living creature and ends one source of persistent acid, bleed, fire, poison, or void damage affecting it. If the creature is taking persistent damage from multiple sources, you select which one is removed. Against an undead target, you deal 2d8 vitality damage (basic Fortitude save); if it fails the save, it also takes @Damage[(@item.rank)[persistent,vitality]] damage.

**Heightened (+1)** The amount of healing (or damage to an undead target) increases by 1d8, and the persistent vitality damage to an undead creature increases by 1.

**Source:** `= this.source` (`= this.source-type`)
