---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Contingency]]", "[[Manipulate]]", "[[Sanctified]]", "[[Spirit]]"]
cast: "10 minutes"
range: "touch"
targets: "1 creature"
duration: "24 hours"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon an invisible divine draconic spirit to watch over your target. When the spell is complete, you gain the [[Dragon's Protection]] reaction; once you use the reaction, the spell ends.

**Dragon's Protection** R (concentrate, sanctified, spirit)

@Embed[Compendium.pf2e.actionspf2e.Item.Zt9bo3FYLQihmpAz inline]

**Heightened (+1)** The damage increases by 1d4.

> [!danger] Effect: Spell Effects: Divine Dragon's Watch

**Source:** `= this.source` (`= this.source-type`)
