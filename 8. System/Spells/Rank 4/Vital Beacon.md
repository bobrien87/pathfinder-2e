---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "1 minute"
duration: "until your next daily preparations"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Vitality radiates outward from you, allowing others to supplicate and receive healing. Once per round, either you or an ally can use an Interact action to supplicate and lay hands upon you to regain Hit Points. Each time the beacon heals someone, it decreases in strength. It restores @Damage[(@item.rank)d10[healing,vitality]|shortLabel] Hit Points to the first creature, @Damage[(@item.rank)d8[healing,vitality]|shortLabel] Hit Points to the second, @Damage[(@item.rank)d6[healing,vitality]|shortLabel] Hit Points to the third, and @Damage[(@item.rank)d4[healing,vitality]|shortLabel] Hit Points to the fourth, after which the spell ends. You can have only one vital beacon active at a time.

> [!danger] Effect: Spell Effect: Vital Beacon

**Heightened (+1)** The beacon restores one additional die of Hit Points each time it heals, using the same die size as the others for that step.

**Source:** `= this.source` (`= this.source-type`)
