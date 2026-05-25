---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Society, Courtly Graces or Streetwise"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know the right people who can get things done for you in certain circles. Once per week, when you're in an area that has an established group of influential nobles, mercantile elites, or the like (if you have Courtly Graces), or a network of unsavory characters such as a thieves' guild (if you have Streetwise), you can use Society to Request a favor or aid from those people as if they were friendly to you. Your request must make sense for the type of people you contact. For instance, a member of the royal court could secure you a proper invitation to a fancy ball, while a local burglar could point out a way to stealthily infiltrate that same party. If you critically succeed this check, your connection gives a piece of helpful advice or lets you in on a small secret, granting you or a member of your party a +2 circumstance bonus to the first skill check you attempt when acting on the favor. If you critically fail this check, you might have to perform some service for your connection to get back in their good graces, as determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
