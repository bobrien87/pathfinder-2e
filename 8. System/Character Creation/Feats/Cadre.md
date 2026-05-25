---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Captain|Captain]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Captain Dedication, expert in Diplomacy or Intimidation"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Between your daring adventures, people seek you out. A loyal cadre of retainers joins you. These individuals don't function as followers and won't accompany you into dangerous areas or situations. However, they can train by your side, assist you in creating items, or help you spread your heroic tales.

When you are in a place where your cadre could reasonably assist you, you gain a +1 circumstance bonus to all skill checks to Craft, Create a Forgery, [[Earn Income]], and Subsist, as well as other downtime activities at the GM's discretion. Your cadre also helps you train, making retraining faster than normal. For every 5 days you spend retraining, you make a week's worth of progress.

**Source:** `= this.source` (`= this.source-type`)
