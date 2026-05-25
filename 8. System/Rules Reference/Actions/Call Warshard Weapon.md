---
type: action
source-type: "Remaster"
traits: ["[[Magical]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:1`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are not holding your warshard weapon, and you have a hand or hands free to be able to wield your warshard weapon

**Effect** Your warshard weapon teleports into your hand, as long as you and your warshard weapon are on the same planet. At 15th level, you need only be on the same plane as your warshard weapon to call it, and at 18th level, you can call your warshard weapon across any distance. If your warshard weapon is in the possession of a mythic creature that's higher level than you or placed in an area where teleportation magic doesn't function, attempt a DC 16 flat check. On a success, your warshard weapon still teleports to your hand.

**Source:** `= this.source` (`= this.source-type`)
