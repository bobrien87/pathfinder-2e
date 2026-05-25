---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You grasp the animating force within an elemental creature and bend it to your will. Choose a trait matching one of your kinetic elements and target an elemental creature within 30 feet that has the chosen trait. The elemental becomes controlled by you if its level is equal to or lower than your level - 3, or [[Slowed]] 1 for as long as you Sustain the effect if its level is equal to your level - 2 or higher. It can attempt a [[Will]] save saving throw against your class DC to resist being [[Controlled]] by you or to end the slowed effect. If the target is already under someone else's command, it can't be slowed by this ability, and the controlling creature also rolls a saving throw, with the elemental using the better result.
- **Critical Success** The target is unaffected and is temporarily immune for 24 hours.
- **Success** The target is unaffected.
- **Failure** The elemental creature is controlled or slowed as long as you Sustain the impulse, up to 1 minute. This effect ends if you or an ally attacks the elemental.
- **Critical Failure** As failure, but you can Sustain the impulse up to 1 hour.

**Source:** `= this.source` (`= this.source-type`)
