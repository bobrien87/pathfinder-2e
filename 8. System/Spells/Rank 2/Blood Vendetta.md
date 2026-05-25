---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Curse]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "The triggering creature"
defense: "Will"
duration: "varies"
requirements: "You can bleed"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** You can bleed.

**Trigger** A creature deals piercing, slashing, or persistent bleed damage to you.

You curse the target, punishing it for having the audacity to spill your blood. The target takes 2d6 persistent bleed damage and must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half the persistent bleed damage.
- **Failure** The target takes the full persistent bleed damage. Until the bleeding stops, the target has weakness 1 to piercing and slashing damage. 

> [!danger] Effect: Spell Effect: Blood Vendetta (Failure)
- **Critical Failure** As failure, but the target takes double the persistent bleed damage.

**Heightened (+2)** The persistent bleed damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
