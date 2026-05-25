---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "9"
cast: "7 days"
range: "touch"
targets: "1 living creature up to 20th level"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You collect hair, nail clippings, and samples of skin and blood from the target, who must be present throughout the ritual and can be one of the casters. You then use those samples to grow a duplicate of the target's physical form that will house the target's soul upon death. This duplicate is physically identical to the original creature.

In order to perform the ritual, you need an expanded alchemist's lab or a superior set of equipment. Once the ritual is successfully completed, the duplicate grows within the laboratory equipment for `r 2d4` months. Though direct involvement isn't required during this period of growth, you must prevent any interference or interruption, or the ritual fails. When the duplicate is complete, the original creature's soul enters it as soon as their original body dies, or immediately if the creature died during the intervening months, as long as the soul is free and willing. If Pharasma has decided that the target's time has come or the target's soul is trapped or doesn't wish to return, the duplicate remains empty until the impediment is removed. While unoccupied, the inert duplicate must be preserved in suitable alchemical equipment to prevent it from rotting.
- **Critical Success** The cloning process is successful. When the soul occupies the completed clone, it is [[Clumsy]] 1, [[Drained]] 1, [[Doomed]] 1, and [[Enfeebled]] 1 for 1 week; these conditions can't be removed or reduced by any means until the week has passed.
- **Success** As critical success, but each condition value is 2.
- **Failure** You fail to form the clone.
- **Critical Failure** The clone appears to be successful, but something went horribly wrong. Once it grows to its full size, it can't hold the target's soul and instead houses a malevolent intelligence or an invasive creature (such as a powerful demon).

**Source:** `= this.source` (`= this.source-type`)
