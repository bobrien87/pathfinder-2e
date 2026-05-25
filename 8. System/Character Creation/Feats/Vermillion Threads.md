---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Arcane]]", "[[Magus]]"]
prerequisites: "Arcane Cascade, unfurling brocade hybrid study"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You use [[Arcane Cascade]].

Your Arcane Cascade sends threads to the four directions, creating a web of strings dyed by your skill and your enemies' blood. The web fills a @Template[type:burst|distance:15] centered on you and is difficult terrain. You can ignore the difficult terrain, and the strings can support your weight, allowing you to walk on them as though you were benefiting from [[Fly]].

The web lasts for 1 minute but ends early if your Arcane Cascade ends or you leave the web.

If you Cast a Spell from a spell slot while in the web, the strings glow red until the beginning of your next turn, dealing damage equal to the spell's rank to any creature other than you that moves through the web. The damage occurs at the end of the creature's movement, with a [[Reflex]] save against your spell DC. A creature can take this damage only once each round.

**Source:** `= this.source` (`= this.source-type`)
