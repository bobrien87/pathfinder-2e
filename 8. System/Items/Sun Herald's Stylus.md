---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]"]
price: "{'gp': 4000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This writing instrument was made from the spur of one of the giant divine roosters that heralds the presence of Shizuru. While you hold it, you gain a +2 item bonus to Calligraphy Lore and Medicine checks.

**Activate—Rejuvenating Ink** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** Drawing a circle on the ground with your stylus, you cast [[Field of Life]] centered on yourself.

**Craft Requirements** The feathers must be plucked from a living divine rooster or given by the bird to a chosen mortal.

**Source:** `= this.source` (`= this.source-type`)
