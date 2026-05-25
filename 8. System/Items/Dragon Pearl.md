---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (manipulate)

These fermented and dried tea leaves are rolled into a ball shaped like a pearl.

When brewed as a tea and consumed, it promotes an outpouring of vital energy that surges through your body. For the next 10 minutes, you have resistance 15 to void damage, and your unarmed attacks deal an additional 1d6 points of vitality damage on a successful Strike.

While this effect is active, whenever a damaging attack or effect would reduce you to 0 Hit Points, you can use your reaction to immediately end the benefits of dragon pearl and remain conscious and standing with 10 Hit Points, increasing your [[Wounded]] condition by 1.

> [!danger] Effect: Dragon Pearl

**Source:** `= this.source` (`= this.source-type`)
