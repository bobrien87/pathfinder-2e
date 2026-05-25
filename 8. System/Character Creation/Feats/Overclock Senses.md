---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your senses speed up to the point that time seems to stand still, allowing you to catch details and incoming attacks. You [[Seek]]. After you Seek, you gain a +2 circumstance bonus to your AC against ranged attacks and to Reflex saving throws until the beginning of your next turn.

**Awakening** When you use Overclock Senses, you can focus even more on the present moment, allowing you more apparent time to observe and plot at the expense of defense. When you use Overclock Senses, you do so with the benefits of darkvision, or if you are at least 14th level, with the benefits of truesight. You can attempt a [[Recall Knowledge]] check as a free action after Seeking. Your senses spent, you then do not gain the normal bonuses to AC and Reflex saving throws.

**Awakening** You hone your senses even further, letting you react to attacks almost before they happen. While you have the bonuses from Overclock Senses, if you would be hit by a ranged attack, you can spend a reaction to have the attacker roll the attack again (this is a misfortune effect), and if you would fail a Reflex save, you can spend a reaction to roll the save again (this is a fortune effect). You must take the second result, even if it is worse.

**Source:** `= this.source` (`= this.source-type`)
