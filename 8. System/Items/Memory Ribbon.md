---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 20}"
usage: "worn"
bulk: "—"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The time-honored tradition of weaving beautiful, embroidered glory ribbons throughout one's hair and beard remains an important cultural practice among some dwarven clans, with the choice of colors and style of presentation representing status, achievements, and other significant aspects of someone's position. Magical versions also exist that help enhance the wearer's memory. These magical ribbons are especially popular when someone has been invited to serve as a toastmaster at a guild banquet or as a master of ceremonies at an important festival. Their use in final oral exams for high positions is, however, hotly debated.

**Activate—Read the Ribbon's Story** `pf2:f` (concentrate)

**Trigger** You attempt a skill check to Recall Knowledge but haven't rolled yet

**Effect** The memory ribbon grants you a +2 item bonus to the triggering skill check to Recall Knowledge. Afterward, the ribbon becomes non-magical.

**Source:** `= this.source` (`= this.source-type`)
