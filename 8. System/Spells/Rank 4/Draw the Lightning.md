---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Electricity]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature that is either taller than you or higher than you"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Calling out to the skies, you summon a bolt of lightning to strike through a foe above you and down into your weapon or your body, charging it with electrical power. You must hold your weapon or an empty hand aloft as part of this spell's somatic component. When you do, a bolt of lightning descends from a storm cloud in the air above your and through the target, dealing 3d12 electricity damage with a basic Reflex save. For the rest of the spell's duration, your first Strike each round with the weapon you held aloft (or with your unarmed attacks if you held an empty hand aloft) deals an additional 1d12 electricity damage.

The spell creates its own storm cloud if necessary, so you can cast *draw the lightning* anywhere, even underground. If *draw the lightning* is cast outside under a cloudy or stormy sky, increase the bolt's damage by 2d12 electricity.

> [!danger] Effect: Spell Effect: Draw the Lightning

**Heightened (8th)** The damage dealt to the initial target increases by 4d12, and the additional damage dealt on the first Strike each turn increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
