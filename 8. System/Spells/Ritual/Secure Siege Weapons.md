---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "2 hours"
area: "250-foot burst"
targets: "siege weapons operated by allied crews"
duration: "1 month"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You strengthen your army's siege weapons and prevent them from being commandeered by enemy hands. At the successful conclusion of the ritual, each allied siege weapon in the area gains an increase to its Hardness and Hit Points for the duration. In addition, enemies who try to operate or move an affected mounted siege weapon or pick up an affected portable siege weapon must succeed at a DC 20 [[Will]] save saving throw or be forced to roll twice and take the worse result on any check to Load or Strike with the siege weapon; this is a misfortune effect. Finally, if an enemy Launches an affected siege weapon, their targets can roll twice and take the better result for any resulting saving throw; this is a fortune effect.
- **Critical Success** Each affected siege weapon's Hardness increases by 10, and its maximum Hit Points increase by an amount equal to three times the siege weapon's level.
- **Success** Each affected siege weapon's Hardness increases by 5, and its maximum Hit Points increase by an amount equal to twice the siege weapon's level.
- **Failure** The ritual has no effect.
- **Critical Failure** All allied siege weapons in the area gain the broken condition.

**Source:** `= this.source` (`= this.source-type`)
