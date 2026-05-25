---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can designate your ikons as movable by only your own hand, leaving them fixed in place as surely as if they were lodged in stone. Whenever you Release an ikon, you can spend an action to command it to remain motionless. While motionless, the ikon can be moved only if 8,000 pounds of pressure are applied to it or if a creature uses Athletics to [[Force Open]] the ikon with a DC equal to your class DC. You can Release your ikon over an adjacent [[Prone]] enemy to hold them down with the ikon's motionlessness—while so Released, you can't use the ikon, but the enemy must succeed at the Athletics check to Stand or to move. The ikon automatically flies back to your hand when the effect is broken or if you spend an Interact action to hold out a hand and draw it back.

**Source:** `= this.source` (`= this.source-type`)
