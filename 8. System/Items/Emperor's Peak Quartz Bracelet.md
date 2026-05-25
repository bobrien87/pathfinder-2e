---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 5}"
usage: "worn"
bulk: "—"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While most residents of—and travelers to—the Five Kings Mountains live underground, a significant number of people explore the regions' awe-inspiring peaks. Among their many discoveries on Emperor's Peak is a deposit of rainbow-colored rock crystal quartz with inherent magical properties that aid in survival, especially in the mountains. Dwarven artisans fashion chunks of this translucent quartz into fashionable bracelets.

Wearing such a bracelet grants you a +1 item bonus to Survival checks to [[Sense Direction]] and [[Subsist]]. This bonus increases to +3 when in mountainous terrain. If you attempt a Survival check to Subsist after 8 hours or less of exploration, you take only a –2 penalty instead of a –5 penalty.

**Source:** `= this.source` (`= this.source-type`)
