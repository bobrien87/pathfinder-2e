---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Bard]]", "[[Secret]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use a performer's cold reading techniques, aura reading, and other tricks to discover your foe's strengths and weaknesses. The GM rolls a secret [[Occultism]] check for you against the Deception or Stealth DC (whichever is higher) of an enemy of your choice who is not [[Concealed]] from you, [[Hidden]] from you, or [[Undetected]] by you, and who is engaged in combat. The GM might apply a penalty for the distance between you and the enemy. The enemy is then temporarily immune to your Combat Reading for 1 day.
- **Critical Success** The GM chooses and tells you two of the following pieces of information about the enemy: which of the enemy's weaknesses is highest, which of the enemy's saving throws has the lowest modifier, one immunity the enemy has, or which of the enemy's resistances is highest. In the event of a tie, the GM should pick one at random.
- **Success** The GM chooses one piece of information from the above list to tell you about the enemy.
- **Critical Failure** The GM gives you false information (the GM makes up the information).

**Source:** `= this.source` (`= this.source-type`)
