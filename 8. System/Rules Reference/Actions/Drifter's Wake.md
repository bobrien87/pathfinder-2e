---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:3`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You drift across the battlefield, striking down foes as you go. You Stride, and you can Strike up to three times at any points during your movement. Each attack must target a different enemy and must be made with a one-handed firearm, crossbow, melee weapon, or unarmed attack. Each attack counts toward your multiple attack penalty, but your multiple attack penalty doesn't increase until you've made all your attacks. Your movement doesn't trigger reactions.

**Source:** `= this.source` (`= this.source-type`)
