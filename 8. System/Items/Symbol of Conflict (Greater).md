---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Divine]]", "[[Invested]]"]
price: "{'gp': 900}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This tarnished necklace can be attuned only by someone who is holy or unholy. When you attune it, it transforms into your deity's religious symbol or a personal symbol if you don't have a deity. You receive a +2 item bonus to Religion and a +1 circumstance bonus to saves against holy and unholy effects.

**Activate—Presence** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The symbol casts 4th-rank [[Bane]], [[Bless]], [[Divine Wrath]], or [[Cleanse Affliction]].

The counteract DC of these effects is 27, and the counteract modifier is +17.

**Craft Requirements** You must be holy or unholy.

**Source:** `= this.source` (`= this.source-type`)
