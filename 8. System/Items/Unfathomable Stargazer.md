---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Cursed]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An unfathomable stargazer is a handheld brass telescope etched with constellations, the patterns of which form bizarre, shifting runes. You can observe the night sky with an unfathomable stargazer, however, the constellations you glimpse through the telescope distort with expanding and contracting fields of darkness among them. You use Occultism instead of Perception or Astronomy Lore when observing the skies with this item, and gain a +2 item bonus on all checks to do so. Once you use it, it fuses to you, and you must succeed at a DC 35 [[Will]] save to use another device to observe the stars, including your naked eyes. The telescope imposes a –4 circumstance penalty to Survival checks to [[Sense Direction]] or navigate. If you critically fail this Survival check, you're subjected to [[Warp Mind]] (DC 34 [[Will]] save) as you glimpse something horrifying and alien amid the darkness.

**Source:** `= this.source` (`= this.source-type`)
