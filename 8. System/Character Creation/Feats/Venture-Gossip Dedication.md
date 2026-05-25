---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Venture Gossip|Venture Gossip]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "member of the Pathfinder Society, Pathfinder Agent Dedication"
source: "Paizo Blog: Foolish Housekeeping and Other Articles"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Look, the motto of the Pathfinder Society is "explore, report, cooperate" and you're just reporting what you hear! Is all of it accurate or true? Maybe not, but hey, you can tell a great story and you know how to keep your readers hooked and eating out of the palm of your hand. Ambrus Valsin of the Grand Lodge may disapprove of your methods, but hey, he's not your real boss.

Eando isn't either.

We'll go with Zarta.

Wait, no, Sheila. Sheila appreciates a good gossip column. You're now from Magnimar. Always have been.

You have two identities: your day job as a Pathfinder agent, and your real job, one of the many voices that make up the Venture-Gossip tabloid. If someone attempts to figure out if you're a venture-gossip, they must use a [[Seek]] action to attempt a Perception check against one of your influence skills of your choice: Deception, Diplomacy, or Intimidation. Your DC is 20 + your proficiency modifier.

If you are discovered to be part of Venture-Gossip, you can spend 1 week of downtime convincing others that you've never even read that tabloid, much less contributed to it!

You gain the following action, allowing you to collect more information for your column.

[[Tell Me More]]

Venture-Gossip

**Source:** `= this.source` (`= this.source-type`)
