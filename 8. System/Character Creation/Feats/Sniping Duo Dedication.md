---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sniping Duo|Sniping Duo]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in at least one type of weapon in the bow or firearm groups, trained in Stealth"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you take this dedication, choose one willing, non-minion ally to act as your spotter. This character does not need to specialize in ranged attacks; a melee partner can be just as effective and maybe even preferable depending on your preferred tactics and weaponry!

As part of your training in this archetype, you train your spotter in the necessary habits and techniques to use your abilities automatically; your spotter doesn't need to spend any feats of their own to grant the effects. You only gain the benefits of your Sniping Duo archetype feats if both you and your spotter are alive and conscious. You and your spotter don't grant your foes lesser cover against one another's Strikes. Whenever you or your spotter successfully Strikes a target, the other member of your duo gains a +1 circumstance bonus per weapon damage die on the damage roll of their next Strike made against that target before the end of their next turn. You can change your designated spotter by spending 3 days of downtime training with another ally to teach them your techniques and signals.

> [!danger] Effect: Sniping Duo Dedication

**Source:** `= this.source` (`= this.source-type`)
