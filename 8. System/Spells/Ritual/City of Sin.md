---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "7"
traits: ["[[Emotion]]", "[[Mental]]", "[[Mythic]]"]
cast: "7 days"
duration: "1 month"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 7-mile-radius circle centered on you

Each day during the casting of this ritual, intelligent creatures within range become increasingly prone to shed their inhibitions and give in to whatever tempts them. Exposed communities experience increases in crime, vice, and violence (however the community defines those vices). At the ritual's culmination, chaos ensues as everyone from every walk of life chooses temptation over faithfulness to their convictions.
- **Critical Success** Intelligent creatures in the ritual's area might betray even their most closely held convictions, including behaviors anathema to their class or faith. They take a –4 circumstance penalty to saves against mental effects and to their [[Coerce]] and [[Request]] DCs.
- **Success** Intelligent creatures in the ritual's area become more likely to give in to temptation, indulging vices and violating all but the strongest convictions. They take a –2 circumstance penalty to saves against mental effects and to their Coerce and Request DCs.
- **Failure** Intelligent creatures in the ritual's radius behave normally but gain the general sense that something unnatural tried to manipulate their actions.
- **Critical Failure** As failure above, except communities of intelligent creatures in the ritual's area bond over any events they experienced during the ritual's casting. They commit themselves to shared principles for behavior, gaining a +2 circumstance bonus to saves against mental effects and to their Coerce and Request DCs for 1 week.

**Source:** `= this.source` (`= this.source-type`)
