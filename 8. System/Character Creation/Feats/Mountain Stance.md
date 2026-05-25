---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]", "[[Stance]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are unarmored and touching the ground

You enter the stance of an implacable mountain—a technique created by dwarven monks—allowing you to strike with the weight of an avalanche and block blows with your garments. The only Strikes you can make are falling stone unarmed attacks. These deal 1d8 bludgeoning damage; are in the brawling group; and have the forceful, nonlethal, and unarmed traits.

While in Mountain Stance, you gain a +4 item bonus to AC and a +2 circumstance bonus to any defenses against [[Reposition]], [[Shove]], [[Trip]], and other forced movement effects. You have a Dexterity modifier cap to your AC of +0, meaning you don't add your Dexterity to your AC, and your Speeds are all reduced by 5 feet. The item bonus to AC from Mountain Stance is cumulative with armor potency runes on your explorer's clothing, mystic armor, and bands of force.

**Source:** `= this.source` (`= this.source-type`)
