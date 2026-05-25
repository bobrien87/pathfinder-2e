---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You zoom from enemy to enemy, striking each in an instant. Stride to an enemy and attempt a Strike against it. If successful, you can add another action to Lightspeed Assault. Stride again and attempt another Strike; if this second Strike is successful, you can spend another action to Stride again and attempt a third Strike. You can use Lightspeed Assault while Burrowing, Climbing, Flying, or Swimming instead of Striding if you have the corresponding movement type. You attempt a backlash check for your deviation only once, regardless of how many actions you end up spending on your Lightspeed Assault.

**Awakening** Your speed allows you to slip the bonds of space. Instead of Striding, you simply teleport to your desired destination. Lightspeed Assault gains the teleportation trait.

**Awakening** You move so quickly that you might as well be in multiple places at once. When you use Lightspeed Assault, you can decide to spend one, two, or three actions up front, selecting your targets ahead of time. You can flank with yourself for any of these Strikes, and if you deal damage to a target more than once, you can add all the damage together for the purpose of overcoming resistances, if it would be more beneficial to you.

**Source:** `= this.source` (`= this.source-type`)
