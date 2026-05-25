---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]", "[[Mythic]]", "[[Two hand d12]]"]
price: "{'cp': 0, 'gp': 68000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #221: Into the Apocalypse Archive"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Timeflaying blades* are forged around shards of collapsed paradoxes. Their existence is largely an enigma. In the furthest corners of esoteric scholarship, they're mentioned in passing or simply alluded to without ever being named outright. They're associated with Stethelos, the legendary city said to lie at the heart of the Dimension of Time, though it's unclear if they were made there, were discovered there, or are bound to return there at the end of time itself.

A *timeflaying blade* is a *+3 greater striking greater corrosive keen quickstrike orichalcum bastard sword*. Acid damage caused by a *timeflaying blade* appears not to be caused by liquid, but by the act of material simply eroding away into dust as if thousands of years passed in an instant (this doesn't impact a creature or object's acid immunity, resistance, or weakness, though).

**Activate—Flay Time** `pf2:1` (concentrate, incapacitation, manipulate)

**Frequency** once per minute

**Effect** Spend 1 Mythic Point. You swing the *timeflaying blade* through the air as if slicing something while you attempt to sever a creature within 120 feet from time itself. The creature must attempt a DC 43 [[Will]] save.
- **Critical Success** The creature is [[Slowed]] 1 for 1 round.
- **Success** The creature is hurled 1d4 rounds into the future. They disappear in a flash of white light, only to reappear in the same space on their initiative after the duration. If that space is occupied, the creature is shunted harmlessly aside to the closest unoccupied space.
- **Failure** As success, but the creature is hurled forward in time 1d4 minutes.
- **Critical Failure** As success, but the creature is hurled into an entirely alternate timeline. At your discretion, the creature's gear is left behind in your timeline. Whether or not the creature will ever return to your timeline depends on the GM's whim, but at the very least, it should never return within the span of a year's passing.

**Source:** `= this.source` (`= this.source-type`)
