---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 60}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

One hundred cuts, healed into diamond-shaped scars, represent the ability to withstand the attacks of your enemies. Orc warriors covet these scar patterns and cluster them around what they consider to be their strongest assets—a pattern around the heart signifies a warrior with great endurance, while one along the arms indicates great upper body strength.

You gain a +1 item bonus to Intimidation checks. If you have Ferocity (such as from the [[Orc Ferocity]] feat or a similar ability), the first time each day you use it, instead of remaining at 1 Hit Point, your Hit Points are set to an amount equal to your ancestry Hit Points, even if this amount is more than you had before using Ferocity.

**Source:** `= this.source` (`= this.source-type`)
