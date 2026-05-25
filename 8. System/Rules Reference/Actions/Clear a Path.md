---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wielding a two-handed firearm or two-handed crossbow.

You push outward with your weapon to clear some space before quickly reloading a fresh round. You make an Athletics check to [[Shove]] an opponent within your reach using your weapon, then Interact to reload. For this Shove, you don't need a free hand, and you add the weapon's item bonus on attack rolls (if any) to the Athletics check. If your last action or activity this round included a ranged Strike with the weapon, use the same multiple attack penalty as the last Strike you attempted with the weapon for the Shove; the Shove still counts toward your multiple attack penalty on further attacks.

**Source:** `= this.source` (`= this.source-type`)
