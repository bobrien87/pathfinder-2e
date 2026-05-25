---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your body falls [[Unconscious]] and your spirit projects out of it. While in spirit form, you can't consciously move your body, and you are [[Invisible]] and inaudible, though a creature still might notice the signs of your presence and passing, just like for an invisible creature affected by [[Silence]], or a [[Scouting Eye]]. You can freely move about, though you can't touch or move anything, cast spells, attack, or otherwise affect anything around you. Despite your ghostly form, you are not incorporeal and can't pass through barriers you couldn't in your body. Most effects can't harm your spirit form, though some spells, like [[Spirit Blast]] and [[Spirit Song]], explicitly damage a creature's spirit.

You can return to your body as a free action. If you are in spirit form at the beginning of your turn, you must attempt another backlash check for your deviation, returning to your body if you fail.

> [!danger] Effect: Distant Wandering

**Awakening** Your spirit moves at the speed of thought. You gain a fly Speed and a +20-foot status bonus to your Speed while in spirit form.

*Note: No specific fly speed was given by Paizo for this ability. A fly speed equal to your land speed has been used in the effect.*

**Awakening** Time seems to pass more slowly while you are projecting your spirit, letting you notice things around you. When you enter spirit form, you can Recall Knowledge or Seek. You are [[Quickened]] while in spirit form and can use the extra action only to Recall Knowledge or [[Seek]].

**Source:** `= this.source` (`= this.source-type`)
