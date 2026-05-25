---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You conjure metal elemental mounts made of interlocking metal pieces. Target up to 5 Medium or smaller willing creatures within 30 feet. Large mounts appear underneath them, and the targets can immediately [[Mount]] the creatures. Each mount can take four different forms. One form has only a land Speed of 80 feet, and the other forms each have a land Speed of 30 feet with a climb, fly, or swim Speed of 60 feet. Each rider chooses the initial form and can change the form as a single action, which has the concentration trait.

The mounts have AC 40, Fortitude +30, Reflex +30, Will +25, and 180 Hit Points. They're mindless and immune to bleed, healing, [[Paralyzed]], poison, and sleep. They can't attack. They remain for 1 minute or until you use this impulse again. You can use this impulse as a 1-minute exploration activity to make the duration 1 hour, but this halves the mounts' defenses and HP.

**Source:** `= this.source` (`= this.source-type`)
