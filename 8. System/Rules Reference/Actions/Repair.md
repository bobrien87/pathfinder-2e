---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Manipulate]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are holding or wearing a Repair Kit

You spend 10 minutes attempting to fix a damaged item, placing the item on a stable surface and using the repair kit with both hands. The GM sets the DC, but it's usually about the same DC to Repair a given item as it is to Craft it in the first place. You can't Repair a destroyed item.
- **Critical Success** You restore 10 Hit Points to the item, plus an additional 10 Hit Points per proficiency rank you have in Crafting (a total of 20 HP if you're trained, 30 HP if you're an expert, 40 HP if you're a master, or 50 HP if you're legendary).
- **Success** You restore 5 Hit Points to the item, plus an additional 5 per proficiency rank you have in Crafting (for a total of 10 HP if you are trained, 15 HP if you're an expert, 20 HP if you're a master, or 25 HP if you're legendary).
- **Critical Failure** You deal 2d6 damage to the item. Apply the item's Hardness to this damage.

**Source:** `= this.source` (`= this.source-type`)
