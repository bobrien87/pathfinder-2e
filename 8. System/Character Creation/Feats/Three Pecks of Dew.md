---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Cultivator Dedication, you aren't unholy"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

At this stage of cultivation, your body is as much spirit as flesh. While still fettered to the physical realm, your form flourishes without needing conventional food or drink, and your natural healing now rivals that brought by scalpel and suture.

You become sanctified with the holy trait. When you perform the Subsist downtime activity, you can use Occultism for the skill check (instead of the skills normally associated with your environment). If you do so, this activity gains the vitality trait as you subsist on ambient qi within your environment's dew-laden air and create shelter from solidified emanations of qi.

Additionally, when you Refocus, you can also [[Treat Wounds]] at the same time. If you do so, you can use Occultism for checks to Treat Wounds and disregard the need for a [[Healer's Toolkit]]; this activity gains the vitality trait as you circulate healing qi through your own body or transfuse your ally with healing qi.

**Source:** `= this.source` (`= this.source-type`)
