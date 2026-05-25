---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Invested]]", "[[Magical]]", "[[Teleportation]]"]
price: "{'gp': 10000}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Headbands of translocation* are silk bands that come in pairs and usually feature a prominent symbol of a nation or team. If both wearers Invest their headbands at the same time and think of the same symbol while doing so, both headbands change to display that symbol until they are removed. If you both have Invested your headbands, you can Aid each other without taking an action to prepare and when you get a critical failure when attempting to Aid an ally with a paired headband, you get a failure instead.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You remove your headband, which teleports you to a space adjacent to the other Invested wearer's location, if you are within 1 mile of each other.

**Source:** `= this.source` (`= this.source-type`)
