---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Trip]]"]
price: "{'gp': 6500}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking decaying scythe* is deathly cold to the touch and exudes an unmistakable aura of menace. As long as you carry this weapon, your presence repels and noticeably unnerves most animals, causing them to avoid you if possible and react to you with a starting attitude one step worse than normal if made to interact with you directly. The one exception is vermin who scavenge corpses; they appear around you with greater frequency. Small mundane plants, such as grass or flowers, wilt and die after spending 24 hours in close proximity to a reaper's toll, crumbling to dust 24 hours after that.

**Activate—Reaper's Claim** `pf2:r`

**Frequency** once per day

**Trigger** A creature within 30 feet is reduced to 0 Hit Points

**Effect** Make a melee Strike with reaper's toll as though you were in the space of the triggering creature. If your Strike hits, you gain temporary Hit Points equal to half the damage dealt, which last for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
