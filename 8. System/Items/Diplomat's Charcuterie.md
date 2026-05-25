---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 9}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (manipulate)

A common sight at political gatherings, a diplomat's charcuterie has fine meats, cheeses, nuts, fruits, and other finger foods mixed with reagents to engender friendly feelings between those consuming them. Contents of the plate vary by chef and the intended palates, from the hearty sausages and hard cheese of charcuterie from the Lands of the Linnorm Kings to the hot-pepper cheese curds and smoked almonds of Thuvian platters. After Activating the charcuterie by eating it, you gain a +1 item bonus to Diplomacy checks to [[Make an Impression]] and Perception checks to [[Sense Motive]]. These bonuses last 24 hours or until you make your next daily preparations, whichever comes first.

> [!danger] Effect: Diplomat's Charcuterie

**Source:** `= this.source` (`= this.source-type`)
