---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 100}"
usage: "worn"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A combination of waterproof leather, durable glass, and a system of copper tubes allows aquatic creatures who wear this suit to be able to spend time on land. They're custom-tailored to fit a wide variety of body types and needs. Part of the system of tubes is set up in a way to allow the wearer to speak and hear as well as they normally would with creatures outside the suit. Water, either fresh or salt, is kept moving throughout the system to keep the wearer moisturized. The moving water allows for easier flow to the gills or breathing apparatus of the creature. It also means that the water will slowly run out. Each suit must be refilled with the proper type of water for a creature every 24 hours. It takes 2 gallons of water to refill a suit.

**Source:** `= this.source` (`= this.source-type`)
