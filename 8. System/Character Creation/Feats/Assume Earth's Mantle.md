---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Enormous pieces of rock cluster around your body. You can Dismiss this impulse.

- You become Large if you were smaller. This increases your reach by 5 feet (or by 10 feet if you started out Tiny).
- You gain a climb Speed equal to your land Speed, but you can use it only to climb surfaces of earthen matter.
- The armor grants you a +1 circumstance bonus to your Fortitude saves and a +2 circumstance bonus to your Fortitude or Reflex DCs against attempts to [[Shove]] you, [[Trip]] you, or knock you [[Prone]].
- If your Strength is below +4, this armor raises your Strength to +4. If your Strength is +4 or higher, this armor grants you a +1 item bonus to your Strength.
- If you have the [[Armor in Earth]] impulse, you can add its effects to Assume Earth's Mantle.

**Source:** `= this.source` (`= this.source-type`)
