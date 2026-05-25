---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Hungerseed]]", "[[Morph]]", "[[Primal]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Your eyes glow a deep red and your body courses with adrenaline as you obtain a fraction of the power of the kishin oni. You attempt to [[Demoralize]] all creatures within a 10- foot radius; you don't take a penalty when you attempt to Demoralize a creature that doesn't understand your language.

You also gain the following abilities for 1 minute.

- 40 temporary Hit Points.
- A fly Speed equal to your Speed.
- The effects of 6th-rank [[Runic Body]], and your horns deal an additional 1d4 electricity damage.
- Bloodsense as a precise sense with a range of 60 feet, allowing you to detect freshly spilled blood; this allows you to accurately detect creatures taking persistent bleed damage, creatures whose Hit Points are currently at half or less of their maximum, and freestanding puddles or droplets of recently spilled blood.

Kishin Rage lasts for 1 minute. Once it ends, you're [[Stunned]] 3 as you recharge and recenter yourself.

**Source:** `= this.source` (`= this.source-type`)
