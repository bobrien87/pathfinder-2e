---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 9000}"
usage: "worn"
bulk: "L"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When an irritant is caught within a dragon's scales, the dragon's body protects itself by coating the object in layers of dragon scale. Over time, it can form an item called a *dragon pearl*. Such pearls, hard and iridescent, are infused with draconic magic and can be powerful tools in the right hands. They're usually placed in an ornate setting on a pin or necklace. Wearing the dragon pearl grants you a +2 item bonus to Intimidation checks.

**Activate—Pearlescent Shell** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You call protective power from the pearl to form a defensive barrier around yourself. You're affected by an 8th-rank [[Containment]] spell, which takes on the appearance of shimmering translucent dragon scales. The field has resistance 15 to one damage type related to the dragon the pearl came from. When you activate the pearl, you choose the type from all types the dragon has immunity or resistance to plus a type based on their tradition: force for arcane, spirit for divine, mental for occult, or poison for primal.

**Source:** `= this.source` (`= this.source-type`)
