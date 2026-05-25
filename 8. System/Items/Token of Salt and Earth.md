---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 225}"
usage: "worn"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This charm is usually worn around the neck or hanging from a belt. It consists of a three-part hourglass with individual glass bulbs filled with sea salts, charcoal ash, and minute slivers of silver. It grants the wearer a +1 item bonus to Stealth checks to Hide and Sneak from creatures with the unholy trait.

**Activate—Hide from the Hateful** `pf2:2` (illusion, manipulate, occult, subtle)

**Frequency** once per day

**Effect** By rotating the charm along one of its concentric rings, you become [[Invisible]] to creatures with the fiend, fey, or undead trait (your choice) for 1 minute. If you use a hostile action, you're no longer invisible after the action is completed.

**Source:** `= this.source` (`= this.source-type`)
