---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Arcane]]", "[[Automaton]]"]
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You redirect energy from your core to ports on your back or feet, allowing you to fly for a short time. You can maintain this redirected energy for 5 minutes. You gain a fly Speed equal to your Speed while redirecting the energy.

**Enhancement** You can maintain your flight for longer. You can redirect your energy at all times, allowing you to fly whenever you want, rather than just once per day for 5 minutes.

**Source:** `= this.source` (`= this.source-type`)
